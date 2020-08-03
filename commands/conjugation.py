import asyncio
import discord
from classes import WebTable
from commands.utility import trim
from config import chrome_driver_path
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Conjugation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['con'])
    async def c(self, ctx, query: str = "string"):
        options = webdriver.ChromeOptions()
#        options.add_argument("headless")
        with webdriver.Chrome(executable_path=chrome_driver_path, options=options) as driver:
#            wait = WebDriverWait(driver, 5)
            driver.get(f'https://tangorin.com/words?search={query}')
            page_link = driver.find_element_by_xpath(
                '//*[@class="results-dl "]/*/a'
            )
            page_link.click()
            await asyncio.sleep(5)
            table_link = driver.find_element_by_xpath(
                '//*/section/div/dl/div/dt/a'
            )
            table_link.click()
            des = []
            table_data = driver.find_element_by_xpath(
                '//*/section/*/table'
            )
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
    bot.add_cog(Conjugation(bot))
