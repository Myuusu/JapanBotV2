import asyncio
import os
import random
import re
import secrets
import urllib
from datetime import datetime, timezone
from urllib.parse import quote_plus

import aiohttp
import discord
import psutil
from discord.ext import commands

from classes import Guild


async def one_in(sides: int = 6):
    return random.randint(1, sides)


async def clean_float(string_to_process):
    string_to_process = str(string_to_process).replace(",", "").lower()
    multiply_by_ten = 0
    if "k" in string_to_process:
        multiply_by_ten += 3
    if "m" in string_to_process:
        multiply_by_ten += 6
    if "b" in string_to_process:
        multiply_by_ten += 9
    base = float(re.sub("[.,kmb]", "", string_to_process))
    if "." in string_to_process:
        output_string = string_to_process.split(".")
        return base * pow(10, multiply_by_ten - len(output_string[1]))
    else:
        return base * pow(10, multiply_by_ten)


def check_process_running(process_name):
    for proc in psutil.process_iter():
        try:
            if process_name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        finally:
            return False


def url_encode(query: str):
    return urllib.parse.quote_plus(query)


async def trim(output: str = "", length: int = 2000):
    if len(output) > length:
        return output[:length - len(output) - 3] + '...'
    return output


async def read_website(url: str, format: str = "text", method: str = "GET", params=None, headers=None, data=None):
    if data is None:
        data = {}
    if headers is None:
        headers = {}
    if params is None:
        params = {}
    if headers != {}:
        async with aiohttp.ClientSession(headers=headers) as session:
            if method == "POST":
                return await session_post(session=session, url=url, format=format, data=data)
            else:
                return await session_get(session=session, url=url, format=format, params=params)
    else:
        async with aiohttp.ClientSession() as session:
            if method == "POST":
                return await session_post(session=session, url=url, format=format, data=data)
            else:
                return await session_get(session=session, url=url, format=format, params=params)


async def session_get(session, url: str, format: str = "text", params=None):
    if params is None:
        params = {}
    async with session.get(url=url, params=params) as resp:
        if format == "json":
            output = await resp.json()
        elif format == "read":
            output = await resp.read()
        else:
            output = await resp.text()
    await session.close()
    return output


async def session_post(session, url: str, format: str, data=None):
    if data is None:
        data = {}
    async with session.post(url=url, data=data) as resp:
        if format == "json":
            output = await resp.json()
        elif format == "read":
            output = await resp.read()
        else:
            output = await resp.text()
    await session.close()
    return output


async def find_in_site_text(html_element, xpath_location=None):
    if xpath_location is None:
        xpath_location = ['/']
    output_string = ""
    for child in html_element.xpath(xpath_location):
        try:
            if child.get('href'):
                output_string += child.get('href')
            elif child.get('src'):
                output_string += child.get('src')
            else:
                output_string += child.text_content()
        except AttributeError:
            output_string += " ".join(child)
    else:
        return re.sub("[\r\n\t]", "", output_string)


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='eval', aliases=['evaluate'])
    async def eval(self, ctx, *, expression: str = ""):
        if expression == "":
            msg = await ctx.send("Please Enter Your Expression.")

            def check(m):
                return ctx.channel == m.channel and ctx.author == m.author
            try:
                response = await self.bot.wait_for('message', check=check, timeout=10)
                expression = response.content
                await ctx.send(f'{expression} = {eval(expression)}')
            except asyncio.TimeoutError:
                await msg.edit(content='Timed Out. Please reissue command.')
        else:
            await ctx.send(f'{expression} = {await clean_float(eval(expression)):,}')

    @commands.command(name='load', aliases=['reload'])
    @commands.has_permissions(administrator=True)
    async def load(self, ctx):
        msg = await ctx.send('Reloading Command Files!')
        with os.scandir('./commands') as active_directory:
            for current_file in active_directory:
                if current_file.name.endswith('.py') and current_file.is_file():
                    try:
                        self.bot.reload_extension(f'commands.{current_file.name[:-3]}')
                    except (AttributeError, ImportError) as err:
                        await ctx.say("```py\n{}: {}\n```".format(type(err).__name__, str(err)))
                        pass
        await msg.edit(content='Reloaded Command Files!')
        msg = await ctx.send('Reloading Storage Files!')
        await msg.edit(content='Reloaded Storage Files!')

    @commands.command(name='clear', aliases=['cls', 'empty'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int = 50):
        await ctx.channel.purge(limit=amount)

    @commands.command(name='ban', aliases=['banned'])
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(demonstrate_reason=reason)
        await ctx.send(f'Banned {member.mention}')

    @commands.command(name='shutdown', help="Shut down the bot")
    @commands.has_permissions(administrator=True)
    async def shutdown(self, ctx):
        embed = discord.Embed(
            title=f"{self.bot.user.name} shutting down!",
            color=discord.Color.from_rgb(0, 0, 0),
            timestamp=datetime.now(timezone.utc)
        )
        embed.set_author(
            name=ctx.author.name,
            icon_url=ctx.author.avatar_url
        )
        embed.set_footer(
            text="Why am I still doing this",
            icon_url="https://en.wikipedia.org/wiki/Flag_of_Japan#/media/File:Flag_of_Japan.svg"
        )
        log_channel = self.bot.get_channel(self.bot.guild_list[ctx.guild.id].log_channel)
        await log_channel.send(embed=embed)
        await ctx.message.add_reaction('✅')
        await self.bot.close()

    @commands.command(name='prefix', help='Set your prefix with this')
    @commands.has_permissions(administrator=True)
    async def prefix(self, ctx, prefix):
        if prefix not in ["'", '"', "#", "<", ">"]:
            if isinstance(prefix, str):
                self.bot.guild_list[ctx.guild.id].prefix = [prefix]
            else:
                self.bot.guild_list[ctx.guild.id].prefix = prefix
            await ctx.send(f'The prefix has been changed to: {prefix}')
        else:
            await ctx.send('Invalid Prefix. Prefix has not changed.')

    @commands.command(name='log', aliases=['log_channel', 'update_log'], help='Set your log_channel with this')
    @commands.has_permissions(administrator=True)
    async def log(self, ctx, log_channel_id):
        try:
            self.bot.guild_list[ctx.guild.id].log_channel_id = log_channel_id
        except KeyError:
            self.bot.guild_list.update({ctx.guild.id: Guild(guild_id=ctx.guild.id, log_channel_id=log_channel_id)})
        finally:
            await ctx.send(f'The log_channel has been changed to this channel id: {log_channel_id}')

    @commands.command(name='eight_ball', aliases=['8ball', 'eightball', '8_ball', '8'])
    async def eight_ball(self, ctx, question):
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(self.bot.eight_ball_responses)}')

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
        await msg.edit(content=f"Completed hacking of {user}'s account.\n"
                               f"Please check log for Information. <a:peepohack:740653897772826724>")

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


def setup(bot):
    bot.add_cog(Utility(bot))
