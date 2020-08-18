from classes import Deck
from discord import Embed
from discord.ext import commands


class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.deck = Deck()

    @commands.command(name='daily', aliases=['dailies'])
    @commands.cooldown(rate=1, per=86400, type=commands.BucketType.user)
    async def daily(self, ctx):
        try:
            self.bot.account_list[ctx.author.id].balance += 500
            await self.bot.update_account_list()
            await ctx.send(f'Increased credits by 500!')
        except KeyError:
            await self.bot.insert_account(ctx.author.id)
            await ctx.send("Welcome to the bot! We've given you 1500 credits!")
            self.bot.account_list[ctx.author.id].balance += 500
            await self.bot.update_account_list()

    @commands.command(name='slot', aliases=['slots', 'bet'])
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def slot(self, ctx, input_string: str = "help", multiplier: int = 1):
        if input_string == "help":
            des = []
            for machine in self.bot.slot_machines.keys():
                des.append(self.bot.slot_machines[machine].print())
            des.append("Enter the slot command, followed by the name of the slot machine you'd like to play!")
            await ctx.send(embed=Embed(title="Slot Machine List", description="\n".join(des), color=0x00ff00))
        else:
            try:
                user = self.bot.account_list[ctx.author.id]
            except KeyError:
                user = await self.bot.insert_account(ctx.author.id)
                await ctx.send("Welcome to the bot! We've given you 1000 credits to get started!")
            try:
                machine = self.bot.slot_machines[input_string.lower()]
            except KeyError:
                return await ctx.send('Machine Not Recognized! Please reissue command.')

            if machine.cost <= user.balance:
                user.balance += await machine.spin(ctx, multiplier)
                await self.bot.update_slot_machines()
                await self.bot.update_account_list()
            else:
                await ctx.send('You do not have enough points!\nMaybe try to get some charity.')
            return

    @commands.command(name='points', aliases=['pts', 'check_points'])
    async def points(self, ctx):
        assert self.bot.account_list[ctx.author.id], await ctx.send("Current user does not have an account yet.")
        points = str(self.bot.account_list[ctx.author.id].balance)
        await ctx.send(f'{ctx.author.name} currently has {points} points!')
        return points


def setup(bot):
    bot.add_cog(Gamble(bot))
