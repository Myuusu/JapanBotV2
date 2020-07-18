import discord
from discord.ext import commands
import asyncio
import wavelink


class Stations(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def connect_(self, ctx, *, channel: discord.VoiceChannel = None):
        """Connect to a valid voice channel."""
        if not channel:
            try:
                channel = ctx.author.voice.channel
            except AttributeError:
                raise discord.DiscordException(
                    'No channel to join. Please either specify a valid channel or join one.')

        player = self.bot.wavelink.get_player(ctx.guild.id)
        await ctx.send(f'Connecting to **`{channel.name}`**', delete_after=15)
        await player.connect(channel.id)

        controller = self.bot.get_controller(ctx)
        controller.channel = ctx.channel

    @commands.command(aliases=['s', 'st'])
    async def stations(self, ctx):
        embedable = discord.Embed(
            title="Station List",
            description="Please use the following commands depending on the station you want to listen to",
            color=0x00ff00)
        embedable.add_field(name="1. Anime Radio", value='1', inline=False)
        embedable.add_field(name="2. Jazz Sakura - Asia Dream Radio", value="2", inline=False)
        embedable.add_field(name="Japan Hits - Asia Dream Radio", value="3", inline=False)
        embedable.add_field(name="J-Pop Powerplay", value="4", inline=False)
        embedable.add_field(name="J-Club Powerplay Hip-Hop", value="5", inline=False)
        embedable.add_field(name="J-Pop Sakura 懐かしい", value="6", inline=False)
        embedable.add_field(name="J-Pop Powerplay Kawaii", value="7", inline=False)
        embedable.add_field(name="J-Rock Powerplay", value="8", inline=False)
        embedable.add_field(name="Vocaloid Radio", value="9", inline=False)
        embedable.add_field(name="Japanimradio", value="10", inline=False)
        embedable.add_field(name="FM 845", value="11", inline=False)
        embedable.add_field(name="Bitter Sweet Music JP", value="12", inline=False)
        embedable.add_field(name="Banana FM", value="13", inline=False)
        embedable.add_field(name="Musashino FM", value="14", inline=False)
        embedable.add_field(name="Radio Kanazawa", value="15", inline=False)
        await ctx.send(embed=embedable)

        def pred(m):
            return ctx.channel == m.channel and ctx.author == m.author

        try:
            response = await self.bot.wait_for('message', check=pred, timeout=10)
            tracks = ''
            if response == "1":
                tracks = await self.bot.wavelink.get_tracks('http://87.98.217.63:23612/:stream/1')
            else:
                await ctx.send('Bad Input')
            if not tracks:
                return await ctx.send('Could not find any songs with that query.')
            player = await self.bot.wavelink.get_player(ctx.guild.id)
            if not player.is_connected:
                await ctx.invoke(self.connect_)
        except asyncio.TimeoutError:
            await ctx.send('Too Slow')


def setup(bot):
    bot.add_cog(Stations(bot))
