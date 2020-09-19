import lxml.html
from discord import Embed
from discord.ext import commands

from commands.utility import url_encode, find_in_site_text, read_website
from config import x_naver_client_id, x_naver_client_secret


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
            try:
                if format == "webm":
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
        results = await read_website(url=url, method="POST", format="json", headers=headers, data=data)
        try:
            await ctx.send(f'/tts {results["message"]["result"]["translatedText"]}')
        except KeyError:
            await ctx.send("Translation Was Not Able To Be Found")


def setup(bot):
    bot.add_cog(Translate(bot))
