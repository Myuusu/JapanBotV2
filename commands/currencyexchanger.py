import asyncio
import discord
from discord.ext import commands
import aiohttp


class CurrencyExchanger(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='exc')
    async def exc(self, ctx, input_amount, base_currency='EUR'):
        base_currency = base_currency.upper()
        if base_currency == 'EUR':
            output_currency = ['JPY', 'GBP', 'USD']
        elif base_currency == 'JPY':
            output_currency = ['EUR', 'GBP', 'USD']
        elif base_currency == 'GBP':
            output_currency = ['EUR', 'JPY', 'USD']
        elif base_currency == 'USD':
            output_currency = ['EUR', 'JPY', 'GBP']
        else:
            output_currency = ['EUR', 'JPY', 'GBP', 'USD']
        output_currency_as_string = ",".join(output_currency)
        async with aiohttp.ClientSession() as session:
            params = {
                'base': base_currency,
                'symbols': output_currency_as_string
            }
            async with session.get(
                    'https://api.exchangeratesapi.io/latest',
                    params=params
            ) as resp:
                output = await resp.json()
                des = [input_amount + " " + base_currency + " is:"]
                for rate in output["rates"]:
                    output_no_cleanup = float(input_amount) * float(output["rates"][rate])
                    if rate == 'JPY':
                        description_line = str(round(output_no_cleanup))
                    else:
                        description_line = "{:.2f}".format(round(output_no_cleanup, 2))
                    des.append(description_line + " " + rate)
                custom_embed = discord.Embed(
                    title="Currency Exchange Output",
                    description="\n".join(des),
                    url="https://exchangeratesapi.io/",
                    color=0x00ff00
                ).set_footer(
                    text="Click title for more rates and information!"
                )
                await ctx.send(embed=custom_embed)


def setup(bot):
    bot.add_cog(CurrencyExchanger(bot))
