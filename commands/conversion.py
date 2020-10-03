import discord
from discord.ext import commands

from commands.utility import clean_float, read_website


class Conversion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='exc', aliases=['jpy', 'gbp', 'usd', 'eur'])
    async def exc(self, ctx, input_amount, base_currency=''):
        output_currency = ["EUR", "JPY", "GBP", "USD"]
        if base_currency == "":
            prefix_length = len(await self.bot.get_prefix(ctx.message))
            base_currency = ctx.message.content[prefix_length - 1:prefix_length + 2].upper()
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

    @commands.command(name="kg")
    async def kg(self, ctx, output):
        output = await clean_float(output)
        converted_weight_lbs = round(output / 0.45, 2)
        await ctx.send(f"{output} kg is {converted_weight_lbs} pounds")

    @commands.command(name="lbs")
    async def lbs(self, ctx, output):
        output = await clean_float(output)
        converted_weight_kg = round(output * 0.45, 2)
        await ctx.send(f"{output} lbs is {converted_weight_kg} kg")

    @commands.command(name="cm")
    async def cm(self, ctx, output):
        output = await clean_float(output)
        converted_length_inch = round(output / 2.54, 2)
        await ctx.send(f"{output} cm is {converted_length_inch} inches")

    @commands.command(name="inch", aliases=["inches"])
    async def inch(self, ctx, output):
        output = await clean_float(output)
        converted_length_cm = round(output * 2.54, 2)
        await ctx.send(f"{output} inches is {converted_length_cm} cm")

    @commands.command(name="km")
    async def km(self, ctx, output):
        output = await clean_float(output)
        converted_distance = round(output * 0.621371, 2)
        await ctx.send(f"{output} km is {converted_distance} miles")

    @commands.command(name="miles")
    async def miles(self, ctx, output):
        output = await clean_float(output)
        converted_distance = round(output / 0.621371, 2)
        await ctx.send(f"{output} km is {converted_distance} km")

    @commands.command(name="celsius", aliases=['cel', 'cels'])
    async def celsius(self, ctx, output):
        output = await clean_float(output)
        temp = round(output / 5 * 9 + 32, 2)
        await ctx.send(f"{output} °C is {temp} °F")

    @commands.command(name="fahrenheit", aliases=['fah', 'fahr'])
    async def fahrenheit(self, ctx, output):
        output = await clean_float(output)
        temp = round((output - 32) * 5 / 9, 2)
        await ctx.send(f"{output} °F is {temp} °C")


def setup(bot):
    bot.add_cog(Conversion(bot))
