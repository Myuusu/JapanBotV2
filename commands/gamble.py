from classes import Account, Machine, Card, Deck
from discord import Embed
from discord.ext import commands


class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.slot_machines = bot.slot_machines
        self.account_list = bot.account_list
        self.deck = Deck()

    @commands.command(name='slot', aliases=['slots', 'bet'])
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def slot(self, ctx, input_string: str = "help", multiplier: int = 1):
        if input_string == "help":
            des = []
            for machine in self.slot_machines.keys():
                des.append(self.slot_machines[machine].print())
            des.append("Enter the slot command, followed by the name of the slot machine you'd like to play!")
            await ctx.send(embed=Embed(title="Slot Machine List", description="\n".join(des), color=0x00ff00))
        else:
            user = self.account_list[str(ctx.author.id)]
            machine = self.slot_machines[input_string]
            if user and machine:
                if machine.cost <= user.balance:
                    user.balance += await machine.spin(ctx, multiplier)
                else:
                    await ctx.send('You do not have enough points!\nMaybe try to get some charity.')
                return
            else:
                await ctx.send('Machine Not Recognized! Please reissue command.')

    @commands.command(name='points', aliases=['pts', 'check_points'])
    async def points(self, ctx):
        points = self.account_list[str(ctx.author.id)].balance
        await ctx.send(f'{ctx.author.name} currently has {points} points!')
        return points


def setup(bot):
    bot.add_cog(Gamble(bot))
