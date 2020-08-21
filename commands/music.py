import asyncio
import datetime
import discord
import humanize
import itertools
import re
import sys
import traceback
import wavelink
from config import node_settings
from discord.ext import commands
from typing import Union


async def cog_check(ctx):
    if not ctx.guild:
        raise commands.NoPrivateMessage
    return True


async def cog_command_error(ctx, error):
    if isinstance(error, commands.NoPrivateMessage):
        try:
            return await ctx.send('This command can not be used in Private Messages.')
        except discord.HTTPException:
            pass

    print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
    traceback.print_exception(
        type(error), error, error.__traceback__, file=sys.stderr
    )


class MusicController:
    def __init__(self, bot, guild_id):
        self.bot = bot
        self.guild_id = guild_id
        self.channel = None
        self.next = asyncio.Event()
        self.queue = asyncio.Queue()
        self.volume = 40
        self.now_playing = None
        self.bot.loop.create_task(self.controller_loop())

    async def controller_loop(self):
        await self.bot.wait_until_ready()
        player = self.bot.wavelink.get_player(self.guild_id)
        await player.set_volume(self.volume)
        while True:
            if self.now_playing:
                await self.now_playing.delete()
            self.next.clear()
            song = await self.queue.get()
            await player.play(song)
            try:
                self.now_playing = await self.channel.send(f'Now playing: `{song}`')
                await self.next.wait()
            except AttributeError as error:
                print(error)


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.station_list = bot.station_list
        self.controllers = {}
        if not hasattr(bot, 'wavelink'):
            self.bot.wavelink = wavelink.Client(bot=self.bot)
        self.bot.loop.create_task(self.start_nodes())

    async def start_nodes(self):
        await self.bot.wait_until_ready()
        try:
            node = await self.bot.wavelink.initiate_node(
                host=node_settings['host'],
                port=node_settings['port'],
                rest_uri=node_settings['rest_uri'],
                password=node_settings['password'],
                identifier=node_settings['identifier'],
                region=node_settings['region']
            )
            node.set_hook(self.on_event_hook)
        except wavelink.errors.NodeOccupied:
            pass

    async def on_event_hook(self, event):
        if isinstance(event, (wavelink.TrackEnd, wavelink.TrackException)):
            controller = self.get_controller(event.player)
            controller.next.set()

    def get_controller(self, value: Union[commands.Context, wavelink.Player]):
        if isinstance(value, commands.Context):
            gid = value.guild.id
        else:
            gid = value.guild_id
        try:
            controller = self.controllers[gid]
        except KeyError:
            controller = MusicController(self.bot, gid)
            self.controllers[gid] = controller

        return controller

    @commands.command(name='connect')
    async def connect_(self, ctx, channel: discord.VoiceChannel = None):
        if channel:
            player = self.bot.wavelink.get_player(ctx.guild.id)
            await ctx.send(f'Connecting to **`{channel.name}`**', delete_after=15)
            await player.connect(channel.id)
            await player.set_volume(40)
            controller = self.get_controller(ctx)
            controller.channel = ctx.channel
        else:
            try:
                channel = ctx.author.voice.channel
            except AttributeError:
                return await ctx.send('No channel to join. Please either specify a valid channel or join one.')
            player = self.bot.wavelink.get_player(ctx.guild.id)
            await ctx.send(f'Connecting to **`{channel.name}`**', delete_after=15)
            await player.connect(channel.id)
            await player.set_volume(40)
            controller = self.get_controller(ctx)
            controller.channel = ctx.channel

    @commands.command()
    async def play(self, ctx, *, query: str):
        if not re.compile('https?://.+').match(query):
            query = f'ytsearch:{query}'
        tracks = await self.bot.wavelink.get_tracks(f'{query}')
        if not tracks:
            return await ctx.send('Could not find any songs with that query.')
        player = self.bot.wavelink.get_player(ctx.guild.id)
        if not player.is_connected:
            await ctx.invoke(self.connect_)
        track = tracks[0]
        controller = self.get_controller(ctx)
        await controller.queue.put(track)
        await ctx.send(f'Added {str(track)} to the queue.', delete_after=15)

    @commands.command()
    async def play_station(self, ctx, url: str):
        station = await self.bot.wavelink.get_tracks(url)
        player = self.bot.wavelink.get_player(ctx.guild.id)
        if not player.is_connected:
            await ctx.invoke(self.connect_)
        stream = station[0]
        controller = self.get_controller(ctx)
        await controller.queue.put(stream)

    @commands.command()
    async def pause(self, ctx):
        player = self.bot.wavelink.get_player(ctx.guild.id)
        if not player.is_playing:
            return await ctx.send('I am not currently playing anything!', delete_after=15)
        await ctx.send('Pausing the song!', delete_after=15)
        await player.set_pause(True)

    @commands.command()
    async def resume(self, ctx):
        player = self.bot.wavelink.get_player(ctx.guild.id)
        if not player.paused:
            return await ctx.send('I am not currently paused!', delete_after=15)
        await ctx.send('Resuming the player!', delete_after=15)
        await player.set_pause(False)

    @commands.command(aliases=['next'])
    async def skip(self, ctx):
        player = self.bot.wavelink.get_player(ctx.guild.id)
        if not player.is_playing:
            return await ctx.send('I am not currently playing anything!', delete_after=15)
        await ctx.send('Skipping the song!', delete_after=15)
        await player.stop()

    @commands.command()
    async def volume(self, ctx, *, vol: int):
        player = self.bot.wavelink.get_player(ctx.guild.id)
        controller = self.get_controller(ctx)
        vol = max(min(vol, 1000), 0)
        controller.volume = vol
        await ctx.send(f'Setting the player volume to `{vol}`')
        await player.set_volume(vol)

    @commands.command(aliases=['np', 'current', 'nowplaying'])
    async def now_playing(self, ctx):
        player = self.bot.wavelink.get_player(guild_id=ctx.guild.id, context=ctx)
        if not player.is_connected:
            return await ctx.send('Could not locate the player! Please restart Lavalink')
        if not player.current:
            return await ctx.send('I am not currently playing anything!')
        controller = self.get_controller(ctx)
        controller.now_playing = await ctx.send(f'Now playing: `{player.current}`')

    @commands.command(aliases=['q'])
    async def queue(self, ctx):
        player = self.bot.wavelink.get_player(ctx.guild.id)
        controller = self.get_controller(ctx)
        if not player.current or not controller.queue._queue:
            return await ctx.send('There are no songs currently in the queue.', delete_after=20)
        upcoming = list(itertools.islice(controller.queue._queue, 0, 5))
        fmt = '\n'.join(f'**`{str(song)}`**' for song in upcoming)
        embed = discord.Embed(title=f'Upcoming - Next {len(upcoming)}', description=fmt)
        await ctx.send(embed=embed)

    @commands.command(aliases=['leave', 'disconnect', 'dc'])
    async def stop(self, ctx):
        player = self.bot.wavelink.get_player(ctx.guild.id)
        try:
            del self.controllers[ctx.guild.id]
        except KeyError:
            await player.disconnect()
            return await ctx.send('There was no controller to stop.')

        await player.disconnect()
        await ctx.send('Disconnected player and killed controller.', delete_after=20)

    @commands.command()
    async def info(self, ctx):
        player = self.bot.wavelink.get_player(ctx.guild.id)
        node = player.node

        used = humanize.naturalsize(node.stats.memory_used)
        total = humanize.naturalsize(node.stats.memory_allocated)
        free = humanize.naturalsize(node.stats.memory_free)
        cpu = node.stats.cpu_cores

        fmt = f'**WaveLink:** `{wavelink.__version__}`\n\n' \
              f'Connected to `{len(self.bot.wavelink.nodes)}` nodes.\n' \
              f'Best available Node `{self.bot.wavelink.get_best_node().__repr__()}`\n' \
              f'`{len(self.bot.wavelink.players)}` players are distributed on nodes.\n' \
              f'`{node.stats.players}` players are distributed on server.\n' \
              f'`{node.stats.playing_players}` players are playing on server.\n\n' \
              f'Server Memory: `{used}/{total}` | `({free} free)`\n' \
              f'Server CPU: `{cpu}`\n\n' \
              f'Server Uptime: `{datetime.timedelta(milliseconds=node.stats.uptime)}`'
        await ctx.send(fmt)

    @commands.command(aliases=['s', 'st'])
    async def stations(self, ctx, *, station_id: int = 0):
        if station_id == 0:
            des = await self.get_station_descriptions()
            des.append("*Please Respond With The Station Number!*")
            await ctx.send(
                embed=discord.Embed(
                    title="Station List", description="\n".join(des), color=0x00ff00
                ),
                delete_after=30
            )

            def test(m):
                return ctx.channel == m.channel and ctx.author == m.author
            try:
                response = await self.bot.wait_for('message', check=test, timeout=10)
                try:
                    player = self.bot.wavelink.get_player(ctx.guild.id)
                    if player.is_connected:
                        await player.stop()
                    await self.play_station(ctx, self.bot.station_list[int(response.content)].url)
                except KeyError:
                    await ctx.send(f'Please make sure that your entry is a valid station number.')
            except asyncio.TimeoutError:
                await ctx.send('Timed Out. Please reissue command.')
        else:
            player = self.bot.wavelink.get_player(ctx.guild.id)
            if player.is_connected:
                await player.stop()
            await self.play_station(ctx, self.bot.station_list[station_id].url)

    @commands.command()
    async def get_station_descriptions(self):
        des = []
        for i in self.bot.station_list:
            des.append(
                f'**{self.bot.station_list[i].station_id}.** {self.bot.station_list[i].name}'
            )
        return des


def setup(bot):
    bot.add_cog(Music(bot))
