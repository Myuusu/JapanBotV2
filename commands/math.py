import math
from discord.ext import commands
from commands.utility import clean_float, trim


class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['round_up'])
    async def ceil(self, ctx, term: str):
        if term:
            await ctx.send(await trim(f'ceil({term}) = {math.ceil(clean_float(term)):,}'))
        else:
            await ctx.send('Please specify one term to round up!')

    @commands.command(aliases=['round_down'])
    async def floor(self, ctx, term: str):
        if term:
            await ctx.send(await trim(f'floor({term}) = {math.floor(clean_float(term)):,}'))
        else:
            await ctx.send('Please specify one term to round down!')

    @commands.command(aliases=['fact'])
    async def factorial(self, ctx, term: str):
        if term:
            await ctx.send(await trim(f'{term}! = {math.factorial(clean_float(term)):,}'))
        else:
            await ctx.send('Please specify one term to produce a factorial!')

    @commands.command(aliases=['multiplication', 'multiply', 'times', 'prod'])
    async def product(self, ctx, term1: str, term2: str):
        if term1 and term2:
            await ctx.send(await trim(f'{term1} * {term2} = {clean_float(term1)*clean_float(term2):,}'))
        else:
            await ctx.send('Please specify two terms to produce a product!')

    @commands.command(aliases=['divide', 'division', 'quot'])
    async def quotient(self, ctx, term1: str, term2: str):
        if term1 and term2:
            await ctx.send(await trim(f'{term1} / {term2} = {clean_float(term1)/clean_float(term2):,}'))
        else:
            await ctx.send('Please specify two terms to produce a quotient!')

    @commands.command(aliases=['root', 'square_root'])
    async def sqrt(self, ctx, term: str):
        if term:
            await ctx.send(await trim(f'sqrt({term}) = {math.sqrt(clean_float(term)):,}'))
        else:
            await ctx.send(
                'Please specify one term to produce a square root!'
            )

    @commands.command(aliases=['power', 'raise', 'square'])
    async def pow(self, ctx, term1: str, term2: str = 2):
        if term1 and term2:
            await ctx.send(await trim(f'{term1}^{term2} = {math.pow(clean_float(term1),clean_float(term2)):,}'))
        else:
            await ctx.send('Please specify two term to produce a square root!')

    @commands.command(aliases=['add', 'plus', '+'])
    async def addition(self, ctx, term1: str, term2: str):
        if term1 and term2:
            await ctx.send(await trim(f'{term1} + {term2} = {clean_float(term1)+clean_float(term2):,}'))
        else:
            await ctx.send('Please specify two terms to produce a quotient!')

    @commands.command(aliases=['subtract', 'minus', '-'])
    async def subtraction(self, ctx, term1: str, term2: str):
        if term1 and term2:
            await ctx.send(await trim(f'{term1} - {term2} = {clean_float(term1)-clean_float(term2):,.0f}'))
        else:
            await ctx.send('Please specify two terms to produce a quotient!')

            
def setup(bot):
    bot.add_cog(Math(bot))
