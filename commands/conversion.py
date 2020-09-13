import discord
from commands.utility import clean_float
from discord.ext import commands


class Conversion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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
