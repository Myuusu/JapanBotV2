import discord
from discord.ext import commands

from commands.utility import read_website, clean_float


class CurrencyExchanger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='exc', aliases=['jpy', 'gbp', 'usd', 'eur'])
    async def exc(self, ctx, input_amount, base_currency=''):
        output_currency = ["EUR", "JPY", "GBP", "USD"]
        if base_currency == "":
            prefix_length = len(await self.bot.get_prefix(ctx.message))
            base_currency = ctx.message.content[prefix_length-1:prefix_length+2].upper()
            input_amount = await clean_float(input_amount)
        elif input_amount.upper() in output_currency:
            temp = await clean_float(base_currency)
            base_currency = input_amount.upper()
            input_amount = temp

        output_currency.remove(base_currency)

        url = "https://api.exchangeratesapi.io/latest"
        params = {"base": base_currency, "symbols": ",".join(output_currency)}
        output = await read_website(url=url, params=params, process_format="json")

        if base_currency == "JPY":
            des = [f'{input_amount:,} {base_currency} is:']
        else:
            des = [f'{input_amount:,.2f} {base_currency} is:']
        for rate in output["rates"]:
            output_no_cleanup = input_amount * output["rates"][rate]
            if rate == 'JPY':
                des.append(f'{round(output_no_cleanup):,} {rate}')
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
