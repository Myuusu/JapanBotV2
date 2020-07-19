import asyncio
import discord
from discord.ext import commands
import aiohttp


class CurrencyExchanger(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='exc')
    async def exc(self, ctx, input_amount, base_currency="EUR", output_currency=None):
        if output_currency is None:
            output_currency = ['JPY', 'GBP']
        exchange_amount = input_amount
        output_currency_as_string = ",".join(output_currency)
        async with aiohttp.ClientSession() as session:
            params = {'base': base_currency, 'symbols': output_currency_as_string}
            async with session.get(
                    'https://api.exchangeratesapi.io/latest',
                    params=params) as resp:
                output = await resp.json()
                des = [exchange_amount + " " + base_currency + " is:"]
                for symbol in output_currency:
                    des.append(
                        str(round(float(exchange_amount) * float(output['rates'][symbol]), 2)) +
                        " " +
                        symbol)

                embedable = discord.Embed(
                    title="Currency Exchange Output",
                    description="\n".join(des),
                    color=0x00ff00)
                await ctx.send(embed=embedable)


def setup(bot):
    bot.add_cog(CurrencyExchanger(bot))
