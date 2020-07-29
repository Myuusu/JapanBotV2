import aiohttp
import discord
from discord.ext import commands
import lxml.html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class Conjugation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['con'])
    async def c(self, ctx, query: str = "string"):
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        self.driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe", options=options)

        self.driver.get(f"https://tangorin.com/definition/{query}")
        link = self.driver.find_element_by_link_text("Inflection")
        link.click()
        time.sleep(5)

        try:
            base = '//*[@id="App"]/main/div[1]/div[1]/div[1]/div/section/div/dl/div'
            main = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f'{base}'))
            )
            des = [main.text]
            embedable = discord.Embed(
                title=f"Conjugation of {query}",
                description="\n".join(des),
                color=0x00ff00)
            await ctx.send(embed=embedable)

        except:
            self.driver.quit()

        self.driver.quit()


def setup(bot):
    bot.add_cog(Conjugation(bot))
