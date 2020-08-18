import aiohttp
import discord
from discord.ext import commands


class CurrencyExchanger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='exc', aliases=['$'])
    async def exc(self, ctx, input_amount: float, base_currency: str = 'EUR'):
        base_currency = base_currency.upper()
        if base_currency == 'JPY':
            output_currency = ['JPY', 'GBP', 'USD']
        elif base_currency == 'JPY':
            output_currency = ['EUR', 'GBP', 'USD']
        elif base_currency == 'GBP':
            output_currency = ['EUR', 'JPY', 'USD']
        elif base_currency == 'USD':
            output_currency = ['EUR', 'JPY', 'GBP']
        else:
            output_currency = ['EUR', 'JPY', 'GBP', 'USD']
        async with aiohttp.ClientSession() as session:
            params = {'base': base_currency, 'symbols': ",".join(output_currency)}
            async with session.get(
                    'https://api.exchangeratesapi.io/latest',
                    params=params
            ) as resp:
                output = await resp.json()
        await session.close()
        des = [f'{input_amount} {base_currency} is:']
        for rate in output["rates"]:
            output_no_cleanup = float(input_amount) * float(output["rates"][rate])
            if rate == 'JPY':
                des.append(f'{round(output_no_cleanup)} {rate}')
            else:
                des.append(f'{round(output_no_cleanup, 2):,.2f} {rate}')
        custom_embed = discord.Embed(
            title="Currency Exchange Output",
            description="\n".join(des),
            url="https://exchangeratesapi.io/",
        ).set_footer(text="Click title for more rates and information!")
        await ctx.send(embed=custom_embed)


def setup(bot):
    bot.add_cog(CurrencyExchanger(bot))
