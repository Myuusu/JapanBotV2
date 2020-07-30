import aiohttp
from discord.ext import commands
import lxml.html


class Jisho(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['jisho'])
    async def j(self, ctx, query: str = "string"):

        async def read_website(term: str):
            session = aiohttp.ClientSession()
            async with session.get(f'https://jisho.org/search/{term}') as resp:
                text = await resp.text()
                await session.close()
                return text

        async def find(location: str = '/', term: str = "string"):
            site_text = lxml.html.fromstring(
                await read_website(term)
            ).xpath(
                location
            )
            output = ""
            for text in site_text:
                output += text.text_content().replace('\n', '').replace('\t', '')
            return output.strip()

        base = '//*[@id="primary"]/div[1]/div[1]'
        output = "\n".join(
            [
                f"**{await find(base + '/div[1]/div[1]/div/span[2]', query)}** "
                f"{await find(base + '/div[1]/div[1]/div/span[1]', query)} "
                f"{await find(base + '/div[1]/div[1]/div/span[2]/span', query)}",

                f"{await find(base + '/div[1]/div[2]/span[2]', query)}",

                f"*{await find(base + '/div[2]/div/div[1]', query)}*",

                f"{await find(base + '/div[2]/div/div[2]/div/span[1]', query)}"
                f"{await find(base + '/div[2]/div/div[2]/div/span[2]', query)}",

                f" {await find(base + '/div[2]/div/div[3]/div/span[1]', query)}"
                f" {await find(base + '/div[2]/div/div[3]/div/span[2]', query)}",

                f" {await find(base + '/div[2]/div/div[4]/div/span[1]', query)}"
                f" {await find(base + '/div[2]/div/div[4]/div/span[2]', query)}",

                f" {await find(base + '/div[2]/div/div[5]/div/span[1]', query)}"
                f" {await find(base + '/div[2]/div/div[5]/div/span[2]', query)}",

                f" {await find(base + '/div[2]/div/div[6]/div/span[1]', query)}"
                f" {await find(base + '/div[2]/div/div[6]/div/span[2]', query)}"
            ]
        )
        await ctx.send(output)


def setup(bot):
    bot.add_cog(Jisho(bot))
