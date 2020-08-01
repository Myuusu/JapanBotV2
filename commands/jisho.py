from discord.ext import commands
from commands.utility import url_encode, find_in_site
import discord


class Jisho(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['jisho'])
    async def j(self, ctx, *, params: str = "string"):
        url = f'https://jisho.org/search/{await url_encode(query=params)}'
        base = '//*[@id="primary"]/div[1]/div[1]'
        output = [
                " ".join(
                    [
                        f"**{await find_in_site(url, f'{base}/div[1]/div[1]/div/span[2]')}**",
                        await find_in_site(url, f'{base}/div[1]/div[1]/div/span[1]'),
                        await find_in_site(url, f'{base}/div[1]/div[1]/div/span[2]/span')
                    ]
                ).replace('\n', ''),
                await find_in_site(url, f'{base}/div[1]/div[2]/span[2]'),
                await find_in_site(url, f'{base}/div[2]/div/div[1]'),
                " ".join(
                    [
                        await find_in_site(url, f'{base}/div[2]/div/div[2]/div/span[1]'),
                        await find_in_site(url, f'{base}/div[2]/div/div[2]/div/span[2]')
                    ]
                ).replace('\n', ''),
                " ".join(
                    [
                        await find_in_site(url, f'{base}/div[2]/div/div[3]/div/span[1]'),
                        await find_in_site(url, f'{base}/div[2]/div/div[3]/div/span[2]')
                    ]
                ).replace('\n', ''),
                " ".join(
                    [
                        await find_in_site(url, f'{base}/div[2]/div/div[4]/div/span[1]'),
                        await find_in_site(url, f'{base}/div[2]/div/div[4]/div/span[2]')
                    ]
                ).replace('\n', ''),
                " ".join(
                    [
                        await find_in_site(url, f'{base}/div[2]/div/div[5]/div/span[1]'),
                        await find_in_site(url, f'{base}/div[2]/div/div[5]/div/span[2]')
                    ]
                ).replace('\n', ''),
                " ".join(
                    [
                        await find_in_site(url, f'{base}/div[2]/div/div[6]/div/span[1]'),
                        await find_in_site(url, f'{base}/div[2]/div/div[6]/div/span[2]')
                    ]
                ).replace('\n', '')
            ]
        embed_object = discord.Embed(
            title=f'Definition For - {params}',
            description="\n".join(filter(None, output))
        )
        await ctx.send(embed=embed_object)


def setup(bot):
    bot.add_cog(Jisho(bot))
