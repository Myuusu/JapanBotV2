import asyncio
from commands.utility import url_encode, find_in_site_text, read_website
from discord import Embed
from discord.ext import commands
from config import chrome_driver_path
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import cssselect
import lxml.html


class Translate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['jisho'])
    async def j(self, ctx, *, params: str = "string"):
        safe_params = url_encode(query=params)
        url = f'https://jisho.org/search/{safe_params}'
        base = '//*[@id="primary"]/div[1]/div[1]'
        site_text = lxml.html.fromstring(await read_website(url=url))
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
            await ctx.send(embed=Embed(title=f'Definition For - {params}', description="\n".join(output)))

    @commands.command(name='draw', aliases=['drawing', 'pen', 'mp4', 'd'])
    async def draw(self, ctx, terms, format: str = "mp4"):
        output = [f'Searching For: {terms}']
        for term in terms:
            site_text = await read_website(
                url=f'https://app.kanjialive.com/api/kanji/{url_encode(query=term)}',
                format="json"
            )
            if format == "webm":
                if site_text['webm_video_source']:
                    output.append(site_text['webm_video_source'])
                else:
                    output.append(f'Webm Kanji Could Not Be Found For {term}, So No Page Was Loaded.')
            else:
                if site_text['mp4_video_source']:
                    output.append(site_text['mp4_video_source'])
                else:
                    output.append(f'mp4 Kanji Could Not Be Found For {term}, So No Page Was Loaded.')
        else:
            await ctx.send("\n".join(output))


def setup(bot):
    bot.add_cog(Translate(bot))
