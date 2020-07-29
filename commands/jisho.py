import aiohttp
import lxml.html
from discord.ext import commands


class Jisho(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='j', aliases=['jisho'])
    async def j(self, ctx, query: str = "string"):
        async def find(site_text):
            for text in site_text:
                return str(text.text_content())

        async def read_website(term):
            session = aiohttp.ClientSession()
            async with session.get(f'https://jisho.org/search/{term}') as resp:
                await session.close()
                return await resp.text()

        base = '//*[@id="primary"]/div[1]/div[1]'
        element_tree = lxml.html.fromstring(await read_website(query))
#            output = [
#                   await find(element_tree.xpath(f'{base}/div[1]/div[1]/div/span[2]')),
#                   await find(element_tree.xpath(f'{base}/div[1]/div[1]/div/span[1]')),
#                   await find(element_tree.xpath(f'{base}/div[1]/div[2]/span[2]')),
#                   await find(element_tree.xpath(f'{base}/div[2]/div/div[1]')),
#                   await find(element_tree.xpath(f'{base}/div[2]/div/div[2]/div')),
#                   await find(element_tree.xpath(f'{base}/div[2]/div/div[3]/div')),
#                   await find(element_tree.xpath(f'{base}/div[2]/div/div[4]/div'))
#               ]
#        await ctx.send("\n".join(output))
        print(element_tree)

    @commands.command(name='lookup', aliases=['dictionary', 'term'])
    async def lookup(self, ctx, term: str):
        if not term:
            return await ctx.send('Please also specify a term to lookup.', delete_after=20)
        else:
            session = aiohttp.ClientSession()
            try:
                params = {'keyword': term}
                async with session.get('http://jisho.org/api/v1/search/words', params=params) as resp:
                    content = await resp.json()

                if not content["data"][0]:
                    await ctx.send("No results for that term!")
                    return False

                i = 0
                reply = [f'Search Results For: {term}']
                while i < 5:
                    """ Japanese Words And Readings """
                    japanese_words = []
                    for japanese_word in content["data"][i]["japanese"][0]["word"]:
                        japanese_words.append(japanese_word)
                    japanese_readings = []
                    for japanese_reading in content["data"][i]["japanese"][0]["reading"]:
                        japanese_readings.append(japanese_reading)
                    if japanese_words and japanese_readings:
                        reply.append(f'{"".join(japanese_words)} {"".join(japanese_readings)}')
                    if japanese_readings:
                        reply.append(f'{"".join(japanese_readings)}')
                    """ JLPT """
                    ratings = []
                    for rating in content["data"][i]['jlpt']:
                        ratings.append(rating)
                    if ratings:
                        reply.append(" ".join(ratings))
                    """ Senses Section """
                    if content["data"][i]["senses"][0]:
                        """ Parts of Speech """
                        parts_of_speech_arr = []
                        for parts_of_speech in content["data"][i]["senses"][0]["parts_of_speech"]:
                            parts_of_speech_arr.append(parts_of_speech)
                        if parts_of_speech_arr:
                            reply.append("; ".join(parts_of_speech_arr))
                        """ English Definitions """
                        english_definitions = []
                        for english_definition in content["data"][i]["senses"][0]["english_definitions"]:
                            english_definitions.append(english_definition)
                        if english_definitions:
                            reply.append(f'English Definitions: {"; ".join(english_definitions)}')
                        """ Link """
                        links = []
                        for link in content["data"][i]["senses"][0]["links"]:
                            links.append(link)
                        if links:
                            reply.append(f'Links: {" ".join(links)}')
                    i += 1
                    await ctx.send("\n".join(reply))
            except KeyError:
                pass
            finally:
                await session.close()


def setup(bot):
    bot.add_cog(Jisho(bot))
=======
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
