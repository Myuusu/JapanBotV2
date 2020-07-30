import asyncio
import secrets

import discord
import os
import random
from discord.ext import commands
from storage.eight_ball_responses import responses


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

    @commands.command()
    async def reverse(self, ctx, *, text: str):
        """ !poow ,ffuts esreveR
        Everything you type after reverse will of course, be reversed
        """
        t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        await ctx.send(f"🔁 {t_rev}")

    @commands.command()
    async def password(self, ctx, nbytes: int = 18):
        """ Generates a random password string for you
        This returns a random URL-safe text string, containing nbytes random bytes.
        The text is Base64 encoded, so on average each byte results in approximately 1.3 characters.
        """
        if nbytes not in range(3, 1401):
            return await ctx.send("I only accept any numbers between 3-1400")
        if hasattr(ctx, 'guild') and ctx.guild is not None:
            await ctx.send(f"Sending you a private message with your random generated password **{ctx.author.name}**")
        await ctx.author.send(f"🎁 **Here is your password:**\n{secrets.token_urlsafe(nbytes)}")

    @commands.command(aliases=['slots', 'bet'])
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def slot(self, ctx):
        """ Roll the slot machine """
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

        if (a == b == c):
            await ctx.send(f"{slotmachine} All matching, you won! 🎉")
        elif (a == b) or (a == c) or (b == c):
            await ctx.send(f"{slotmachine} 2 in a row, you won! 🎉")
        else:
            await ctx.send(f"{slotmachine} No match, you lost 😢")


def setup(bot):
    bot.add_cog(Utility(bot))
