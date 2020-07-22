import aiohttp
from discord.ext import commands
import lxml.html


class Jisho(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def find(self, site_text):
        output = ""
        for text in site_text:
            output += text.text_content().replace('\n', '').replace('\t', '')
        return output.strip()

    async def read_website(self, query: str):
        session = aiohttp.ClientSession()
        headers = {
            'User-Agent': "User-Agent: Mozilla/5.0 "
                          "(Windows NT 10.0; Win64; x64; rv:74.0) "
                          "Gecko/20100101 Firefox/74.0"
        }
        async with session.get(
                f'https://jisho.org/search/{query}',
                headers=headers
        ) as resp:
            text = await resp.text()
            await session.close()
            return text

    @commands.command(aliases=['jisho'])
    async def j(self, ctx, query: str = "string"):
        base = '//*[@id="primary"]/div[1]/div[1]'
        element_tree = lxml.html.fromstring(str(await self.read_website(query)))
        output = "\n".join(
            [
                f"**{await self.find(element_tree.xpath(base + '/div[1]/div[1]/div/span[2]'))}**" + f"    {await self.find(element_tree.xpath(base + '/div[1]/div[1]/div/span[1]'))}" + f"{await self.find(element_tree.xpath(base + '/div[1]/div[1]/div/span[2]/span'))}",
                await self.find(element_tree.xpath(f'{base}/div[1]/div[2]/span[2]')),
                f"*{await self.find(element_tree.xpath(base + '/div[2]/div/div[1]'))}*",
                await self.find(element_tree.xpath(f'{base}/div[2]/div/div[2]/div/span[1]')) + f" {await self.find(element_tree.xpath(base + '/div[2]/div/div[2]/div/span[2]'))}",
                await self.find(element_tree.xpath(f'{base}/div[2]/div/div[3]/div/span[1]')) + f" {await self.find(element_tree.xpath(base + '/div[2]/div/div[3]/div/span[2]'))}",
                await self.find(element_tree.xpath(f'{base}/div[2]/div/div[4]/div/span[1]')) + f" {await self.find(element_tree.xpath(base + '/div[2]/div/div[4]/div/span[2]'))}",
                await self.find(element_tree.xpath(f'{base}/div[2]/div/div[5]/div/span[1]')) + f" {await self.find(element_tree.xpath(base + '/div[2]/div/div[5]/div/span[2]'))}",
                await self.find(element_tree.xpath(f'{base}/div[2]/div/div[6]/div/span[1]')) + f" {await self.find(element_tree.xpath(base + '/div[2]/div/div[6]/div/span[2]'))}",
            ]
        )
        await ctx.send(output)


def setup(bot):
    bot.add_cog(Jisho(bot))