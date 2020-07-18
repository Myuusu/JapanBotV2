import asyncio
import datetime
import discord
import humanize
import itertools
import re
import sys
import traceback
import wavelink
from discord.ext import commands
from typing import Union

RURL = re.compile('http:\/\/.+')


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
            self.now_playing = await self.channel.send(f'Now playing: `{song}`')

            await self.next.wait()


class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.controllers = {}

        if not hasattr(bot, 'wavelink'):
            self.bot.wavelink = wavelink.Client(bot=self.bot)

        self.bot.loop.create_task(self.start_nodes())

    async def start_nodes(self):
        await self.bot.wait_until_ready()

        # Initiate our nodes. For this example we will use one server.
        # Region should be a discord.py guild.region e.g sydney or us_central (Though this is not technically required)
        node = await self.bot.wavelink.initiate_node(
            host='127.0.0.1',
            port=80,
            rest_uri='http://127.0.0.1:80',
            password='testing',
            identifier='TEST',
            region='europe')

        # Set our node hook callback
        node.set_hook(self.on_event_hook)

    async def on_event_hook(self, event):
        """Node hook callback."""
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

    async def cog_check(self, ctx):
        """A local check which applies to all commands in this cog."""
        if not ctx.guild:
            raise commands.NoPrivateMessage
        return True

    async def cog_command_error(self, ctx, error):
        """A local error handler for all errors arising from commands in this cog."""
        if isinstance(error, commands.NoPrivateMessage):
            try:
                return await ctx.send('This command can not be used in Private Messages.')
            except discord.HTTPException:
                pass

        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    @commands.command(name='connect')
    async def connect_(self, ctx, *, channel: discord.VoiceChannel = None):
        """Connect to a valid voice channel."""
        if not channel:
            try:
                channel = ctx.author.voice.channel
            except AttributeError:
                raise discord.DiscordException('No channel to join. Please either specify a valid channel or join one.')

        player = self.bot.wavelink.get_player(ctx.guild.id)
        await ctx.send(f'Connecting to **`{channel.name}`**', delete_after=15)
        await player.connect(channel.id)

        controller = self.get_controller(ctx)
        controller.channel = ctx.channel

    @commands.command()
    async def play(self, ctx, *, query: str):
        """Search for and add a song to the Queue."""
        if not re.compile('http:\/\/.+').match(query):
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
    async def radio(self, ctx, *, query: str):
        tracks = await self.bot.wavelink.get_tracks('https://musicbird.leanstream.co/JCB061-MP3')
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
    async def pause(self, ctx):
        """Pause the player."""
        player = self.bot.wavelink.get_player(ctx.guild.id)
        if not player.is_playing:
            return await ctx.send('I am not currently playing anything!', delete_after=15)

        await ctx.send('Pausing the song!', delete_after=15)
        await player.set_pause(True)

    @commands.command()
    async def resume(self, ctx):
        """Resume the player from a paused state."""
        player = self.bot.wavelink.get_player(ctx.guild.id)
        if not player.paused:
            return await ctx.send('I am not currently paused!', delete_after=15)

        await ctx.send('Resuming the player!', delete_after=15)
        await player.set_pause(False)

    @commands.command()
    async def skip(self, ctx):
        """Skip the currently playing song."""
        player = self.bot.wavelink.get_player(ctx.guild.id)

        if not player.is_playing:
            return await ctx.send('I am not currently playing anything!', delete_after=15)

        await ctx.send('Skipping the song!', delete_after=15)
        await player.stop()

    @commands.command()
    async def volume(self, ctx, *, vol: int):
        """Set the player volume."""
        player = self.bot.wavelink.get_player(ctx.guild.id)
        controller = self.get_controller(ctx)

        vol = max(min(vol, 1000), 0)
        controller.volume = vol

        await ctx.send(f'Setting the player volume to `{vol}`')
        await player.set_volume(vol)

    @commands.command(aliases=['np', 'current', 'nowplaying'])
    async def now_playing(self, ctx):
        """Retrieve the currently playing song."""
        player = self.bot.wavelink.get_player(ctx.guild.id)

        if not player.current:
            return await ctx.send('I am not currently playing anything!')

        controller = self.get_controller(ctx)
        await controller.now_playing.delete()

        controller.now_playing = await ctx.send(f'Now playing: `{player.current}`')

    @commands.command(aliases=['q'])
    async def queue(self, ctx):
        """Retrieve information on the next 5 songs from the queue."""
        player = self.bot.wavelink.get_player(ctx.guild.id)
        controller = self.get_controller(ctx)

        if not player.current or not controller.queue._queue:
            return await ctx.send('There are no songs currently in the queue.', delete_after=20)

        upcoming = list(itertools.islice(controller.queue._queue, 0, 5))

        fmt = '\n'.join(f'**`{str(song)}`**' for song in upcoming)
        embed = discord.Embed(title=f'Upcoming - Next {len(upcoming)}', description=fmt)

        await ctx.send(embed=embed)

    @commands.command(aliases=['disconnect', 'dc'])
    async def stop(self, ctx):
        """Stop and disconnect the player and controller."""
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
        """Retrieve various Node/Server/Player information."""
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
    async def stations(self, ctx):
        des = [
            "**1.**  Anime Radio",
            "**2.**  Jazz Sakura - Asia Dream Radio",
            "**3.**  Japan Hits - Asia Dream Radio",
            "**4.**  J-Pop Powerplay",
            "**5.**  J-Club Powerplay Hip-Hop",
            "**6.**  J-Pop Sakura 懐かしい",
            "**7.**  J-Pop Powerplay Kawaii",
            "**8.**  J-Rock Powerplay",
            "**9.**  Vocaloid Radio",
            "**10.** Japanimradio",
            "**11.** FM 845",
            "**12.** Bitter Sweet Music JP",
            "**13.** Banana FM",
            "**14.** Musashino FM",
            "**15.** Radio Kanazawa",
            "**Enter the number corresponding to the Radio you want to listen to:**"
        ]
        embedable = discord.Embed(
            title="Station List",
            description="\n".join(des),
            color=0x00ff00)
        await ctx.send(embed=embedable)

        def pred(m):
            return ctx.channel == m.channel and ctx.author == m.author

        try:
            response = await self.bot.wait_for('message', check=pred, timeout=10)
            tracks = ''
            if response.content == "1":
                tracks = await self.bot.wavelink.get_tracks('http://87.98.217.63:23612/:stream/1')
                await ctx.send('You are now listening to Anime Radio!')
            elif response.content == "2":
                tracks = await self.bot.wavelink.get_tracks('http://agnes.torontocast.com:8087/;.mp3')
                await ctx.send('You are now listening to Jazz Sakura - Asia DREAM Radio!')
            elif response.content == "3":
                tracks = await self.bot.wavelink.get_tracks('http://agnes.torontocast.com:8102/;')
                await ctx.send('You are now listening to Japan Hits - Asia DREAM Radio!')
            elif response.content == "4":
                tracks = await self.bot.wavelink.get_tracks('http://bluford.torontocast.com:8526/;')
                await ctx.send('You are now listening to J-Pop Powerplay!')
            elif response.content == "5":
                tracks = await self.bot.wavelink.get_tracks('http://agnes.torontocast.com:8051/;')
                await ctx.send('You are now listening to J-Club Powerplay Hip-Hop!')
            elif response.content == "6":
                tracks = await self.bot.wavelink.get_tracks('http://bluford.torontocast.com:8519/;')
                await ctx.send('You are now listening to J-Pop Sakura 懐かしい!')
            elif response.content == "7":
                tracks = await self.bot.wavelink.get_tracks('http://sky1.torontocast.com:9029/;')
                await ctx.send('You are now listening to J-Pop Powerplay Kawaii!')
            elif response.content == "8":
                tracks = await self.bot.wavelink.get_tracks('http://cristina.torontocast.com:8057/;.mp3')
                await ctx.send('You are now listening to J-Rock Powerplay!')
            elif response.content == "9":
                tracks = await self.bot.wavelink.get_tracks('http://curiosity.shoutca.st:8019/stream')
                await ctx.send('You are now listening to Vocaloid Radio!')
            elif response.content == "10":
                tracks = await self.bot.wavelink.get_tracks('http://vps-8ef514a5.vps.ovh.net:8000/stream')
                await ctx.send('You are now listening to Japanimradio!')
            elif response.content == "11":
                tracks = await self.bot.wavelink.get_tracks('https://musicbird.leanstream.co/JCB104-MP3')
                await ctx.send('You are now listening to FM 845!')
            elif response.content == "12":
                tracks = await self.bot.wavelink.get_tracks('http://5.196.244.141:8600/live.jp')
                await ctx.send('You are now listening to Bitter Sweet Music JP!')
            elif response.content == "13":
                tracks = await self.bot.wavelink.get_tracks('https://musicbird.leanstream.co/JCB075-MP3')
                await ctx.send('You are now listening to Banana FM!')
            elif response.content == "14":
                tracks = await self.bot.wavelink.get_tracks('https://musicbird.leanstream.co/JCB032-MP3')
                await ctx.send('You are now listening to Musashino FM!')
            elif response.content == "15":
                tracks = await self.bot.wavelink.get_tracks('https://musicbird.leanstream.co/JCB061-MP3')
                await ctx.send('You are now listening to Radio Kanazawa!')

            else:
                await ctx.send('Bad Input')
            if not tracks:
                return await ctx.send('Could not find any songs with that query.')
            player = self.bot.wavelink.get_player(ctx.guild.id)
            if not player.is_connected:
                try:
                    channel = ctx.author.voice.channel
                except AttributeError:
                    raise discord.DiscordException(
                        'No channel to join. Please either specify a valid channel or join one.')

                await ctx.send(f'Connecting to **`{channel.name}`**', delete_after=15)
                await player.connect(channel.id)
                await player.play(tracks[0])

        except asyncio.TimeoutError:
            await ctx.send('Too Slow')


def setup(bot):
    bot.add_cog(Music(bot))
