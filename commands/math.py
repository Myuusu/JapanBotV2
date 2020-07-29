import math
from discord.ext import commands


class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        aliases=[
            'round_up', 'ceiling'
        ]
    )
    async def ceil(self, ctx, *, term):
        if term:
            await ctx.send(
                f'ceil({term}) = {math.ceil(term)}'
            )
        else:
            await ctx.send(
                'Please specify one term to round up!'
            )

    @commands.command(
        aliases=[
            'round_down'
        ]
    )
    async def floor(self, ctx, *, term):
        if term:
            await ctx.send(
                f'floor({term}) = {math.floor(term)}'
            )
        else:
            await ctx.send(
                'Please specify one term to round down!'
            )

    @commands.command(
        aliases=[
            'fact'
        ]
    )
    async def factorial(self, ctx, *, term):
        if term:
            await ctx.send(
                f'{term}! = {math.factorial(term)}'
            )
        else:
            await ctx.send(
                'Please specify one term to produce a factorial!'
            )

    @commands.command(
        aliases=[
            'multiplication', 'multiply', 'times', 'prod'
        ]
    )
    async def product(self, ctx, term1: int, term2: int):
        if term1 and term2:
            await ctx.send(
                f'{term1} * {term2} = {term1*term2:,.2f}'
            )
        else:
            await ctx.send(
                'Please specify two terms to produce a product!'
            )

    @commands.command(
        aliases=[
            'divide', 'division', 'quot'
        ]
    )
    async def quotient(self, ctx, term1: float, term2: float):
        if term1 and term2:
            await ctx.send(
                f'{term1} / {term2} = {term1/term2:,.2f}'
            )
        else:
            await ctx.send(
                'Please specify two terms to produce a quotient!'
            )

    @commands.command(
        aliases=[
            'root', 'square_root'
        ]
    )
    async def sqrt(self, ctx, term: float):
        if term:
            await ctx.send(
                f'sqrt({term}) = {math.sqrt(term):,.2f}'
            )
        else:
            await ctx.send(
                'Please specify one term to produce a square root!'
            )

    @commands.command(
        aliases=[
            'power', 'raise', 'square'
        ]
    )
    async def pow(self, ctx, term1: float, term2: float = 2):
        if term1 and term2:
            await ctx.send(
                f'{term1}^{term2} = {math.pow(term1,term2):,.0f}'
            )
        else:
            await ctx.send(
                'Please specify two term to produce a square root!'
            )

    @commands.command(
        aliases=[
            'add', 'plus', '+'
        ]
    )
    async def addition(self, ctx, term1: float, term2: float):
        if term1 and term2:
            await ctx.send(
                f'{term1} + {term2} = {term1 + term2:,.0f}'
            )
        else:
            await ctx.send(
                'Please specify two terms to produce a quotient!'
            )

    @commands.command(
        aliases=[
            'subtract', 'minus', '-'
        ]
    )
    async def subtraction(self, ctx, term1: float, term2: float):
        if term1 and term2:
            await ctx.send(
                f'{term1} - {term2} = {term1 - term2:,.0f}'
            )
        else:
            await ctx.send(
                'Please specify two terms to produce a quotient!'
            )


def setup(bot):
    bot.add_cog(Math(bot))
