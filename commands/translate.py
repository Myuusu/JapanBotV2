import asyncio
import re
import urllib
from urllib.parse import quote_plus

import discord
import lxml.html
from discord import Embed
from discord.ext import commands
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from commands.utility import find_in_site_text, read_website
from commands.utility import trim
from config import chrome_driver_path
from config import x_naver_client_id, x_naver_client_secret


class WebTable:
    def __init__(self, web_table):
        self.table = {
            "table": web_table,
            "rows": len(web_table.find_elements_by_xpath("tr")) - 1,
            "columns": len(web_table.find_elements_by_xpath("//tr[2]/td"))
        }

    def __getitem__(self, item):
        return self.table[item]

    def get_row_count(self):
        return len(self.table["table"].find_elements_by_tag_name("tr")) - 1

    def get_column_count(self):
        return len(self.table["table"].find_elements_by_xpath("//tr[2]/td"))

    def get_table_size(self):
        return {"rows": self.get_row_count(), "columns": self.get_column_count()}

    def row_data(self, row_number):
        if row_number == 0:
            raise Exception("Row number starts from 1")
        r_data = []
        for webElement in self.table["table"].find_elements_by_xpath(f'//tr[{str(row_number + 1)}]/td'):
            r_data.append(webElement.text)
        return r_data

    def column_data(self, column_number):
        r_data = []
        for webElement in self.table["table"].find_elements_by_xpath(f'//tr/td[{str(column_number)}]'):
            r_data.append(webElement.text)
        return r_data

    def get_all_data(self, max_rows=None):
        if max_rows:
            num_rows = len(self.table["table"].find_elements_by_xpath("//tr")) - 1
            if max_rows < num_rows:
                num_rows = max_rows
        else:
            num_rows = len(self.table["table"].find_elements_by_xpath("//tr")) - 1
        header = ["Form", "Plain", "Polite"]
        all_data = [" | ".join(header)]
        for i in range(2, num_rows):
            ro = ["**(" + self.table["table"].find_element_by_xpath(f'//tr[{str(i)}]/th').text + ")**"]
            for j in range(1, len(self.table["table"].find_elements_by_xpath(f'//tr[{str(i)}]/td')) - 1):
                try:
                    ro.append(
                        self.table["table"].find_element_by_xpath(
                            f'//tr[{str(i)}]/td[{str(j)}]'
                        ).text
                    )
                except NoSuchElementException:
                    pass
            all_data.append(" | ".join(ro))
        return all_data

    def presence_of_data(self, data):
        return len(self.table["table"].find_elements_by_xpath(f'//td[normalize-space(text())="{data}"]')) > 0

    def get_cell_data(self, row_number, column_number):
        if row_number == 0:
            raise Exception("Row number starts from 1")
        return self.table["table"].find_element_by_xpath(f'//tr[{str(row_number + 1)}]/td[{str(column_number)}]').text


class Translate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='j', aliases=['jisho'])
    async def j(self, ctx, *, params):
        if not isinstance(params, str):
            safe_params = re.sub("[ +_]", "%20", urllib.parse.quote_plus(" ".join(params)))
        else:
            safe_params = re.sub("[ +_]", "%20", urllib.parse.quote_plus(params))
        url = f'https://jisho.org/search/{safe_params}'
        base = '//*[@id="primary"]/div[1]/div[1]'
        site_text = lxml.html.fromstring(await read_website(url=url, process_format="text"))
        output = [
            f"**{await find_in_site_text(site_text, f'{base}/div[1]/div[1]/div/span[2]')}**",
            await find_in_site_text(site_text, f'{base}/div[1]/div[2]/span[2]'),
            await find_in_site_text(site_text, f'{base}/div[2]/div/div[1]')
        ]
        for i in range(6):
            current_span1 = await find_in_site_text(site_text, f'{base}/div[2]/div/div[{i}]/div/span[1]')
            current_span2 = await find_in_site_text(site_text, f'{base}/div[2]/div/div[{i}]/div/span[2]')
            if current_span1 and current_span2:
                output.append(f'**{current_span1}** {current_span2}')
        else:
            description = "\n".join(output)
            discord_embed = Embed(title=f'Definition For - {params}', description=description)
            await ctx.send(embed=discord_embed)

    @commands.command(name='draw', aliases=['drawing', 'pen', 'mp4', 'd'])
    async def draw(self, ctx, *, terms, video_format: str = "mp4"):
        output = [f'Searching For: {terms}']
        for term in terms:
            site_text = await read_website(
                url=f'https://app.kanjialive.com/api/kanji/{re.sub("[ +_]", "%20", urllib.parse.quote_plus(term))}',
                process_format="json"
            )
            try:
                if video_format == "webm":
                    output.append(site_text['webm_video_source'])
                else:
                    output.append(site_text['mp4_video_source'])
            except KeyError:
                output.append(f'{term}: Kanji Could Not Be Found For {term}, So No Page Was Loaded.')
        else:
            await ctx.send("\n".join(output))

    @commands.command(name="translate", aliases=['ja', 'en', 'convert'])
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def translate(self, ctx, *, query: str):
        if len(query) > 280:
            await ctx.send("Error: Character Count Exceeded. Please Use Fewer Characters!")
            return
        prefix_length = len(await self.bot.get_prefix(ctx.message))
        if ctx.message.content[prefix_length:prefix_length + 2].lower() == "ja":
            data = {
                "source": "ja",
                "target": "en",
                "text": query
            }
        else:
            data = {
                "source": "en",
                "target": "ja",
                "text": query
            }
        url = 'https://openapi.naver.com/v1/papago/n2mt'
        headers = {
            "X-Naver-Client-Id": x_naver_client_id,
            "X-Naver-Client-Secret": x_naver_client_secret,
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
        results = await read_website(url=url, method="POST", process_format="json", headers=headers, data=data)
        try:
            await ctx.send(f'/tts {results["message"]["result"]["translatedText"]}')
        except KeyError:
            await ctx.send("Translation Was Not Able To Be Found")

    @commands.command(name='c', aliases=['con', 'conjugate'])
    async def c(self, ctx, query: str = "string"):
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        with webdriver.Chrome(executable_path=chrome_driver_path, options=options) as driver:
            driver.get(f'https://tangorin.com/words?search={query}')
            page_link = driver.find_element_by_xpath('//*[@class="results-dl "]/*/a')
            page_link.click()
            await asyncio.sleep(5)
            table_link = driver.find_element_by_xpath('//*/section/div/dl/div/dt/a')
            table_link.click()
            des = []
            table_data = driver.find_element_by_xpath('//*/section/*/table')
            for row in WebTable(table_data).get_all_data(40):
                des.append(
                    row.strip("'[]").replace("\n", "//")
                )
            await ctx.send(
                embed=discord.Embed(
                    title=f"Conjugation of {query}",
                    description=await trim("\n".join(des)),
                    color=0x00ff00
                )
            )
        driver.quit()


def setup(bot):
    bot.add_cog(Translate(bot))
