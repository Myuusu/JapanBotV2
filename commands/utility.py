import asyncio
import secrets
import discord
import os
import random
from discord.ext import commands
from storage.eight_ball_responses import responses
from storage.slot_machines import slot_machines


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='load', aliases=['reload'])
    @commands.has_permissions(administrator=True)
    async def load(self, ctx):
        with os.scandir('./commands') as active_directory:
            for current_file in active_directory:
                if current_file.name.endswith('.py') and current_file.is_file():
                    try:
                        self.bot.reload_extension(f'commands.{current_file.name[:-3]}')
                    except (AttributeError, ImportError) as err:
                        await ctx.say("```py\n{}: {}\n```".format(type(err).__name__, str(err)))
                        pass
        await ctx.send('Reloaded Commands With Changes.')

    @commands.command(name='clear', aliases=['cls', 'empty'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)

    @commands.command(name='ban', aliases=['banned'])
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')

    @commands.command(name='eight_ball', aliases=['8ball', 'eightball', '8_ball', '8'])
    async def eight_ball(self, ctx, *, question):
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command(name='ping', aliases=['ding'])
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

    @commands.command(name='hack', aliases=['code', 'initiate_hack'])
    async def hack(self, ctx, user: discord.Member):
        msg = await ctx.send(f"Hacking! Target: {user}")
        await asyncio.sleep(2)
        await msg.edit(content="Accessing Discord Files... [▓▓    ]")
        await asyncio.sleep(2)
        await msg.edit(content="Accessing Discord Files... [▓▓▓   ]")
        await asyncio.sleep(2)
        await msg.edit(content="Accessing Discord Files... [▓▓▓▓▓ ]")
        await asyncio.sleep(2)
        await msg.edit(content="Accessing Discord Files COMPLETE! [▓▓▓▓▓▓]")
        await asyncio.sleep(2)
        await msg.edit(content="Retrieving Login Info... [▓▓▓    ]")
        await asyncio.sleep(3)
        await msg.edit(content="Retrieving Login Info... [▓▓▓▓▓ ]")
        await asyncio.sleep(3)
        await msg.edit(content="Retrieving Login Info... [▓▓▓▓▓▓ ]")
        await asyncio.sleep(4)
        await msg.edit(content=f"Completed hacking of {user}'s account. Please check log for Information. :pepohack:")

    @commands.command(name='reverse', aliases=['rev', 'backwards'])
    async def reverse(self, ctx, *, text: str):
        t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        await ctx.send(f"🔁 {t_rev}")

    @commands.command(name="password", aliases=['generate', 'new_password'])
    async def password(self, ctx, num_bytes: int = 18):
        if num_bytes not in range(3, 1401):
            return await ctx.send("I only accept any numbers between 3-1400")
        if hasattr(ctx, 'guild') and ctx.guild is not None:
            await ctx.send(f"Sending you a private message with your random generated password **{ctx.author.name}**")
        await ctx.author.send(f"🎁 **Here is your password:**\n{secrets.token_urlsafe(num_bytes)}")

    @commands.command(aliases=['slots', 'bet'])
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def slot(self, ctx, input_string: str = "help"):
        if input_string == "help":
            des = ["Enter the slot command, followed by the name of the slot machine you'd like to play!"]
            for current in slot_machines:
                des.append(f'Name: {current["name"]}\n Emojis: {current["emojis"]}')
            return await ctx.send("\n".join(des))
        else:
            for machine in slot_machines:
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


async def trim(output: str = "", length: int = 2048):
    if len(output) > length:
        return output[:length - len(output) - 3] + '...'
    return output


def setup(bot):
    bot.add_cog(Utility(bot))
