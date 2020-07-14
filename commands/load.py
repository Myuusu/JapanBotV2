import discord
from discord.ext import commands


class Load(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def load(self, ctx, extension):
        self.bot.load_extension(f'commands.{extension}')


def setup(bot):
    bot.add_cog(Load(bot))
