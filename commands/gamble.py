from classes import Deck
from discord import Embed
from discord.ext import commands
from commands.utility import clean_float


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
    async def slot(self, ctx, input_string: str = "help", spins: str = "1", multiplier: int = 1, testing: bool = False):
        if input_string == "help":
            des = []
            for machine in self.bot.slot_machines.keys():
                des.append(self.bot.slot_machines[machine].print())
            des.append("Enter the slot command, followed by the name of the slot machine you'd like to play!")
            await ctx.send(embed=Embed(title="Slot Machine List", description="\n".join(des), color=0x00ff00))
        else:
            spins = clean_float(spins)
            try:
                user = self.bot.account_list[ctx.author.id]
            except KeyError:
                user = await self.bot.insert_account(ctx.author.id)
                await ctx.send("Welcome to the bot! We've given you 1000 credits to get started!")
            try:
                machine = self.bot.slot_machines[input_string.lower()]
            except KeyError:
                return await ctx.send('Machine Not Recognized! Please reissue command.')

            if machine.cost * multiplier * spins <= user.balance:
                user.balance -= machine.cost * multiplier * spins
                user.balance += await machine.spin(ctx, spins, multiplier, testing)
                await self.bot.update_slot_machines()
                await self.bot.update_account_list()
                output = f'Spun {spins} times at {machine.cost * multiplier} per spin.' \
                         f'\nCoins In: {machine.coins_in:,}' \
                         f'\nCoins Out: {machine.coins_out:,}' \
                         f'\nProfit: {machine.coins_in - machine.coins_out:,}' \
                         f'\nPayout: {machine.coins_out * 100 / machine.coins_in:,.2f}%'
                if machine.coins_out * 100 / machine.coins_in > 97:
                    output += "\n:redAlarm: :redAlarm: :redAlarm: :redAlarm:"
                await ctx.send(output)
            else:
                await ctx.send('You do not have enough points!\nMaybe try to get some charity.')
            return

    @commands.command(name='points', aliases=['pts', 'check_points'])
    async def points(self, ctx):
        assert self.bot.account_list[ctx.author.id], await ctx.send("Current user does not have an account yet.")
        points = str(self.bot.account_list[ctx.author.id].balance)
        await ctx.send(f'{ctx.author.name} currently has {points} points!')
        return points

    @commands.command(name='reset_slot', aliases=['rm', 'rs', 'reset_machine', 'reset_slot_machine'])
    @commands.has_permissions(administrator=True)
    async def reset_slot(self, ctx, machine_name: str = "classic"):
        try:
            await self.bot.slot_machines[machine_name.lower()].reset()
            await ctx.send(f"Reset the following for the {machine_name} Slot Machine:"
                           f"\nCoins In, Coins Out, Play Count, Jackpots")
            await self.bot.update_slot_machines()
        except KeyError:
            await ctx.send('Machine Not Recognized! Please reissue command.')


def setup(bot):
    bot.add_cog(Gamble(bot))
