from classes import Account, Machine, Card, Deck
from discord import Embed
from discord.ext import commands


class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.slot_machines = bot.slot_machines
        self.deck = Deck()

    async def lookup_account(self, user_id):
        for user in self.bot.account_list:
            if user.user_id == user_id:
                return user

    @commands.command(name='slot', aliases=['slots', 'bet'])
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def slot(self, ctx, input_string: str = "help"):
        if input_string == "help":
            des = []
            for machine in self.slot_machines:
                des.append(machine.print())
            des.append("Enter the slot command, followed by the name of the slot machine you'd like to play!")
            await ctx.send(embed=Embed(title="Slot Machine List", description="\n".join(des), color=0x00ff00))
        else:
            for machine in self.slot_machines:
                if machine.name == input_string:
                    user = await self.lookup_account(ctx.author.id)
                    if machine.cost <= user.balance:
                        user.balance += await machine.spin(ctx)
                    else:
                        await ctx.send('You do not have enough points!\nMaybe try to get some charity.')
                    return

    @commands.command(name='points', aliases=['pts', 'check_points'])
    async def points(self, ctx):
        user = await self.lookup_account(ctx.author.id)
        points = user.balance
        await ctx.send(f'{ctx.author.name} currently has {points} points!')
        return points


def setup(bot):
    bot.add_cog(Gamble(bot))
