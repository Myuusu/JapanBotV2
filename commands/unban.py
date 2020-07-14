import discord
from discord.ext import commands


class Unban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.disciminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return


def setup(bot):
    bot.add_cog(Unban(bot))
