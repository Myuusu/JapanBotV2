from discord.ext import commands
from classes.machine import Machine
from classes.account import Account
import asyncio
import aiohttp
import random
import discord


class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.slot_machines = bot.slot_machines
        self.account_list = bot.account_list

    async def check_point_requirements(self, machine_cost: int, user: discord.User):
        print(f'Current User Points: {await self.bot.lookup_user_balance(user)}')
        return machine_cost <= await self.bot.lookup_user_balance(user)

    async def get_user(self, user: discord.User):
        for i in self.account_list:
            if i["user_id"] == user.id:
                return i
        return None

    async def update_user_points(self, user: discord.User, amount: int):
        current = await self.get_user(user)
        if current:
            current["balance"] += amount
            return current["balance"]
        else:
            return None

    @commands.command(aliases=['slots', 'bet'])
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def slot(self, ctx, *, input_string: str = "help"):
        if input_string == "help":
            des = ["Enter the slot command, followed by the name of the slot machine you'd like to play!"]
            for machine in self.slot_machines:
                des.append(f'Name: {machine["name"]}\n Emojis: {machine["emojis"]}')
            return await ctx.send("\n".join(des))
        else:
            for machine in self.slot_machines:
                if machine["name"] == input_string:
                    if await self.check_point_requirements(machine["cost"], ctx.author):
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
                            current = await self.update_user_points(ctx.author, machine['cost'] * 3)
                            await msg.edit(
                                content=f"**[{a} {b} {c}]**"
                                        f"\n{ctx.author.name} All matching, you won {machine['cost']*3} points! {current}🎉"
                            )
                        elif a == b or a == c or b == c:
                            current = await self.update_user_points(ctx.author, machine['cost'] * 2)
                            await msg.edit(
                                content=f"**[{a} {b} {c}]**"
                                        f"\n{ctx.author.name} 2 in a row, you won {machine['cost']*2} points! {current}🎉"
                            )
                        else:
                            current = await self.update_user_points(ctx.author, -machine['cost'])
                            await msg.edit(
                                content=f"**[{a} {b} {c}]**"
                                        f"\n{ctx.author.name} No match, you lost {machine['cost']} points! {current}😢"
                            )
                        return
                    else:
                        await ctx.send("You don't have enough points for that machine."
                                       "\nYou could always just ask for charity.")


def setup(bot):
    bot.add_cog(Gamble(bot))
