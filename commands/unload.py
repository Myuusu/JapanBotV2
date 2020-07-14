import discord
from discord.ext import commands


class Unload(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unload(self, ctx, extension):
        self.bot.unload_extension(f'commands.{extension}')


def setup(bot):
    bot.add_cog(Unload(bot))
