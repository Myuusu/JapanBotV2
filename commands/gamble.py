from discord.ext import commands
from classes.machine import Machine
from classes.account import Account
import asyncio
import aiohttp
import random


async def check_point_balance(account: Account, machine: Machine):
    return machine.cost >= account.balance


class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.slot_machines = bot.slot_machines
        self.account_list = bot.account_list

    @commands.command(aliases=['slots', 'bet'])
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def slot(self, ctx, input_string: str = "help"):
        if input_string == "help":
            des = ["Enter the slot command, followed by the name of the slot machine you'd like to play!"]
            for machine in self.slot_machines:
                des.append(f'Name: {machine["name"]}\n Emojis: {machine["emojis"]}')
            return await ctx.send("\n".join(des))
        else:
            for machine in self.slot_machines:
                if machine["name"] == input_string:
                    a = random.choice(machine["emojis"])
                    b = random.choice(machine["emojis"])
                    c = random.choice(machine["emojis"])

                    msg = await ctx.send(f"**[ ? ? ? ] Spinning! Good luck!\n{ctx.author.name}**")
                    await asyncio.sleep(3)
                    await msg.edit(content=f"**[ {a} ? ? ]\n{ctx.author.name}**")
                    await asyncio.sleep(1)
                    await msg.edit(content=f"**[ {a} {b} ? ]\n{ctx.author.name}**")
                    await asyncio.sleep(2.5)
                    await msg.edit(content=f"**[ {a} {b} ? ]\n{ctx.author.name}**")
                    if a == b == c:
                        await msg.edit(content=f"**[{a} {b} {c}]**\n{ctx.author.name} All matching, you won! 🎉")
                    elif a == b or a == c or b == c:
                        await msg.edit(content=f"**[{a} {b} {c}]**\n{ctx.author.name} 2 in a row, you won! 🎉")
                    else:
                        await msg.edit(content=f"**[{a} {b} {c}]**\n{ctx.author.name} No match, you lost 😢")
                    return


def setup(bot):
    bot.add_cog(Gamble(bot))
