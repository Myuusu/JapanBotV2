import aiohttp
import asyncio
import discord
import datetime
import lxml.html
import os
import json
import random
import secrets
import urllib
from discord.ext import commands
from urllib.parse import quote_plus


async def trim(output: str = "", length: int = 2048):
    if len(output) > length:
        return output[:length - len(output) - 3] + '...'
    return output


def url_encode(query: str):
    return urllib.parse.quote_plus(query)


async def fetch(formatted_url: str, session):
    async with session.get(formatted_url) as resp:
        assert resp.status == 200
        return await resp.text()


async def read_website(formatted_url: str):
    async with aiohttp.ClientSession() as session:
        text = await fetch(formatted_url=formatted_url, session=session)
    await session.close()
    return text


async def find_in_site(search_url: str, xpath_location: str = '/'):
    site_text = lxml.html.fromstring(
        await read_website(search_url)
    ).xpath(xpath_location)
    output_string = ""
    for text in site_text:
        output_string += text.text_content().replace('\n', '').replace('\t', '')
    return output_string.strip()


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.eight_ball_responses = bot.eight_ball_responses

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

    @commands.command(name='shutdown', help="Shut down the bot")
    @commands.has_permissions(administrator=True)
    async def shutdown(self, ctx):
        embed = discord.Embed(
            title=f"{self.bot.user.name} shutting down!",
            color=discord.Color.from_rgb(0, 0, 0),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        embed.set_author(
            name=ctx.author.name,
            icon_url=ctx.author.avatar_url
        )
        embed.set_footer(
            text="Why am I still doing this",
            icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Flag_of_Japan.svg/120px-Flag_of_Japan.svg.png"
        )
        log_channel_id = 741755498193223710
        log_channel = self.bot.get_channel(log_channel_id)
        await log_channel.send(embed=embed)
        await ctx.message.add_reaction('✅')
        await self.bot.close()

    @commands.command(name='prefix')
    @commands.has_permissions(administrator=True)
    async def prefix(self, ctx, prefix):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

        await ctx.send(f'Prefix changed to {prefix}')

    @commands.command(name='eight_ball', aliases=['8ball', 'eightball', '8_ball', '8'])
    async def eight_ball(self, ctx, *, question):
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(self.bot.eight_ball_responses)}')

    @commands.command(name='ping', aliases=['ding'])
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

    @commands.command(name='test_emojis', aliases=['test_emoji'])
    async def test_emojis(self, ctx):
        await ctx.send(
            f'<:Tangleroot:740607927257399347> '
            f'<:RiftGuardian:740607758780596334> '
            f'<:GiantSquirrel:740607823280603166> '
            f'<:BlackRocky:740607984916496475> '
            f'<:Beaver:740607855685533787>'
        )

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

    @commands.command(name="kg")
    async def kg(self, ctx, output: int = ""):
        converted_weight_lbs = round(output / 0.45, 2)
        await ctx.send(f"{output} kg is {converted_weight_lbs} pounds")

    @commands.command(name="lbs")
    async def lbs(self, ctx, output: int = ""):
        converted_weight_kg = round(output * 0.45, 2)
        await ctx.send(f"{output} lbs is {converted_weight_kg} kg")

    @commands.command(name="cm")
    async def cm(self, ctx, output: int = ""):
        converted_length_inch = round(output / 2.54, 2)
        await ctx.send(f"{output} cm is {converted_length_inch} inches")

    @commands.command(name="inch", aliases=["inches"])
    async def inch(self, ctx, output: int = ""):
        converted_length_cm = round(output * 2.54, 2)
        await ctx.send(f"{output} inches is {converted_length_cm} cm")

    @commands.command(name="km")
    async def km(self, ctx, output: int = ""):
        converted_distance = round(output * 0.621371, 2)
        await ctx.send(f"{output} km is {converted_distance} miles")

    @commands.command(name="miles")
    async def miles(self, ctx, output: int = ""):
        converted_distance = round(output / 0.621371, 2)
        await ctx.send(f"{output} km is {converted_distance} km")

    @commands.command(name="celsius", aliases=['cel', 'cels'])
    async def celsius(self, ctx, output: float = ""):
        temp = round(output / 5 * 9 + 32, 2)
        await ctx.send(f"{output} °C is {temp} °F")

    @commands.command(name="fahrenheit", aliases=['fah', 'fahr'])
    async def fahrenheit(self, ctx, output: float = ""):
        temp = round((output - 32) * 5 / 9, 2)
        await ctx.send(f"{output} °F is {temp} °C")


def setup(bot):
    bot.add_cog(Utility(bot))
