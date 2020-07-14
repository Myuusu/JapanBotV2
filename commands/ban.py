import discord
from discord.ext import commands


class Ban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')


def setup(bot):
    bot.add_cog(Ban(bot))
