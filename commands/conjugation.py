from discord.ext import commands
import discord
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from config import chrome_driver_path
from classes.webtable import WebTable


class Conjugation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def trim(self, output: str):
        if len(output) > 2048:
            return output[:2048-len(output)-3]+'...'
        return output

    @commands.command(aliases=['con'])
    async def c(self, ctx, query: str = "string"):
        with webdriver.Chrome(executable_path=chrome_driver_path) as driver:
            wait = WebDriverWait(driver, 10)
            driver.get(f'https://tangorin.com/words?search={query}')
            link = wait.until(
                expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Inflection"))
            )
            if link:
                '''Will Open The Results Page'''
                link.click()
                final_link = wait.until(
                    expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Inflection"))
                )
                if final_link:
                    '''Will Open The Results Table'''
                    final_link.click()
                    base = '//*/table'
                    des = []
                    table_data = WebTable(
                        wait.until(
                            expected_conditions.presence_of_element_located((By.XPATH, base)))
                    ).get_all_data()
                    for row in table_data:
                        des.append(row.strip("'[]").replace("\n", "//"))
                    await ctx.send(
                        embed=discord.Embed(
                            title=f"Conjugation of {query}",
                            description=await self.trim("\n".join(des)),
                            color=0x00ff00
                        )
                    )
                else:
                    await ctx.send("Secondary page could not be found!")
            else:
                await ctx.send("Conjugation could not be found.")
        driver.quit()


def setup(bot):
    bot.add_cog(Conjugation(bot))
