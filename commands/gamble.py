import asyncio
from classes import Deck
from commands.utility import clean_float
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
            await ctx.send(f'Increased credits by 500!')
        except KeyError:
            await self.bot.insert_account(ctx.author.id)
            await ctx.send("Welcome to the bot! We've given you 1500 credits!")
            self.bot.account_list[ctx.author.id].balance += 500

    @commands.command(name='slot', aliases=['slots', 'bet'])
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def slot(self, ctx, input_string="help", spins="1", multiplier="1", testing="False"):
        if input_string == "help":
            des = []
            for machine in self.bot.slot_machines.keys():
                des.append(self.bot.slot_machines[machine].print())
            des.append("Enter the slot command, followed by the name of the slot machine you'd like to play!")
            await ctx.send(embed=Embed(title="Slot Machine List", description="\n".join(des), color=0x00ff00))
        else:
            spins = await clean_float(spins)
            multiplier = await clean_float(multiplier)
            try:
                user = self.bot.account_list[ctx.author.id]
            except KeyError:
                user = await self.bot.insert_account(ctx.author.id)
                await ctx.send("Welcome to the bot! We've given you 1000 credits to get started!")
            try:
                machine = self.bot.slot_machines[input_string.lower()]
            except KeyError:
                return await ctx.send('Machine Not Recognized! Please reissue command.')

            cost_to_play = machine.cost * multiplier * spins
            if cost_to_play <= user.balance:
                user.balance -= cost_to_play
                user.balance += await machine.spin(ctx, spins, multiplier, testing)
                output = f'Spun {spins} times at {machine.cost * multiplier} per spin.' \
                         f'\nCoins In: {machine.coins_in:,}' \
                         f'\nCoins Out: {machine.coins_out:,}' \
                         f'\nProfit: {machine.coins_in - machine.coins_out:,}' \
                         f'\nPayout: {machine.coins_out * 100 / machine.coins_in:,.2f}%'
                if machine.coins_out * 100 / machine.coins_in > 97:
                    output += "\n:redAlarm: :redAlarm: :redAlarm: :redAlarm:"
                await ctx.send(output)
            else:
                await ctx.send('You do not have enough points!\nMaybe try to use the daily command!')
            return

    @commands.command(name='points', aliases=['pts', 'check_points'])
    async def points(self, ctx):
        assert self.bot.account_list[ctx.author.id], await ctx.send("Current user does not have an account yet.")
        points = str(self.bot.account_list[ctx.author.id].balance)
        await ctx.send(f'{ctx.author.name} currently has {points} points!')
        return points

    @commands.command(name='reset_slot', aliases=['rm', 'rs', 'reset_machine', 'reset_slot_machine'])
    @commands.has_permissions(administrator=True)
    async def reset_slot(self, ctx, machine_name: str = "classic", confirm: str = ""):
        try:
            current = self.bot.slot_machines[machine_name.lower()]
        except KeyError:
            return await ctx.send('Slot Machine Not Found!')

        if confirm in ["confirm", "cf", "--cf", "--confirm"]:
            await current.reset()
            await ctx.send(f"Reset the following for the {machine_name} Slot Machine:"
                           f"\nCoins In, Coins Out, Play Count, Jackpots")
        else:
            def test(m):
                return ctx.channel == m.channel and ctx.author == m.author and "confirm" == m.content
            await ctx.send(f'Please type "confirm" to reset the {machine_name}!')
            try:
                response = await self.bot.wait_for('message', check=test, timeout=10)
                if response.content.lower() == "confirm":
                    await current.reset()
                    await ctx.send(f"Reset the following for the {machine_name} Slot Machine:"
                                   f"\nCoins In, Coins Out, Play Count, Jackpots")
            except asyncio.TimeoutError:
                return await ctx.send('Timed Out. Please reissue command.')


def setup(bot):
    bot.add_cog(Gamble(bot))
