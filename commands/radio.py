import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio


class Radio(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['r'])
    async def radio(self, ctx, url: str = 'http://87.98.217.63:23612/:stream/1'):
        global player
        try:
            player = await get(self.bot.voice_clients, guild=ctx.guild)
            player.play(FFmpegPCMAudio(url))
            player.source = discord.PCMVolumeTransformer(player.source)
            player.source.volume = 0.07
            await ctx.channel.send(f'You are now listening to Anime Radio!')
            if player.is_playing():
                player.stop()
        except:
            pass


def setup(bot):
    bot.add_cog(Radio(bot))
