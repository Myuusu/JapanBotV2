import aiohttp
import asyncio
import discord
import random
from classes.account import Account
from classes.machine import Machine
from classes.card import Card
from discord.ext import commands
from discord import Embed


async def check_point_balance(account: Account, machine: Machine):
    return machine.get_cost() >= account.get_balance()


async def alter_point_balance(account: Account, qty):
    return account.set_balance(account.get_balance() + qty)


class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.deck = [Card(value, color) for value in range(1, 14) for color in ['heart', 'diamonds', 'spades', 'clubs']]
        self.slot_machines = bot.slot_machines

    async def lookup_account(self, user_id):
        for user in self.bot.account_list:
            if user.get_user_id() == user_id:
                return user

    @commands.command(aliases=['slots', 'bet'])
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def slot(self, ctx, input_string: str = "help"):
        if input_string == "help":
            des = []
            for machine in self.slot_machines:
                des.append(machine.print())
            col_width = max(len(word) for row in des for word in row) + 2
            for row in des:
                "".join(word.ljust(col_width) for word in row)
            des.append("Enter the slot command, followed by the name of the slot machine you'd like to play!")
            await ctx.send(embed=Embed(title="Slot Machine List", description="\n".join(des), color=0x00ff00))
        else:
            for machine in self.slot_machines:
                if machine.get_name() == input_string:
                    user = await self.lookup_account(ctx.author.id)
                    if machine.get_cost() <= user.get_balance():
                        result = await machine.spin(ctx)
                        user.set_balance(user.get_balance() - machine.get_cost() + result)
                    else:
                        await ctx.send('You do not have enough points!\nMaybe try to get some charity.')
                    return

    @commands.command(aliases=['pts', 'check_points'])
    async def points(self, ctx):
        user = await self.lookup_account(ctx.author.id)
        points = user.get_balance()
        await ctx.send(f'{ctx.author.name} currently has {points} points!')
        return points


def setup(bot):
    bot.add_cog(Gamble(bot))
