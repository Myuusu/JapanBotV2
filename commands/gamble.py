from classes import Deck, Account
from discord import Embed
from discord.ext import commands


class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.slot_machines = bot.slot_machines
        self.account_list = bot.account_list
        self.deck = Deck()

    async def update_account_list(self):
        output = []
        for account_id in self.account_list.keys():
            output.append(self.account_list[account_id].get_json())
        else:
            with open('storage/account_list.py', mode='w+') as fp:
                string_output = ", ".join(output)
                fp.write(f'from classes import Account\n\naccount_list = [{string_output}]')

    @commands.command(name='daily', aliases=['dailies'])
    @commands.cooldown(rate=1, per=86400, type=commands.BucketType.user)
    async def daily(self, ctx):
        try:
            self.account_list[str(ctx.author.id)].balance += 500
            await self.update_account_list()
            await ctx.send(f'Increased credits by 500!')
        except KeyError:
            self.account_list[str(ctx.author.id)] = Account(str(ctx.author.id), 1500)
            await ctx.send("Welcome to the bot! We've given you 1500 credits!")
            await self.update_account_list()

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
            try:
                user = self.account_list[str(ctx.author.id)]
            except KeyError:
                self.account_list[str(ctx.author.id)] = Account(str(ctx.author.id), 1000)
                await self.update_account_list()
                user = self.account_list[str(ctx.author.id)]
                await ctx.send("Welcome to the bot! We've given you 1000 credits to get started!")
            try:
                machine = self.slot_machines[input_string.lower()]
            except KeyError:
                return await ctx.send('Machine Not Recognized! Please reissue command.')

            if machine.cost <= user.balance:
                user.balance += await machine.spin(ctx, multiplier)
                await self.update_account_list()
            else:
                await ctx.send('You do not have enough points!\nMaybe try to get some charity.')
            return

    @commands.command(name='points', aliases=['pts', 'check_points'])
    async def points(self, ctx):
        points = self.account_list[str(ctx.author.id)].balance
        await ctx.send(f'{ctx.author.name} currently has {points} points!')
        return points


def setup(bot):
    bot.add_cog(Gamble(bot))
