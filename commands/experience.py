import math
from discord.ext import commands


class Experience(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='convert_lvl_to_xp',
        aliases=[
            'conlvltoxp', 'conleveltoxp', 'conlvltoexp', 'conleveltoexp',
            'con_lvl_to_xp', 'con_level_to_xp', 'con_lvl_to_exp', 'con_level_to_exp'
        ]
    )
    async def convert_lvl_to_xp(self, ctx, lvl, external=True):
        lvl = int(lvl.replace(',', ""))
        points = 0
        for i in range(lvl):
            points += math.floor(i + 300 * math.pow(2, i / 7))
        if external:
            await ctx.send(
                f'Level {lvl} is reached at: {math.floor(points / 4):,d} xp.'
            )
        else:
            return math.floor(points / 4)

    @commands.command(
        name='convert_xp_to_lvl',
        aliases=[
            'conxptolvl', 'conxptolevel', 'conexptolvl', 'conexptolevel',
            'con_xp_to_lvl', 'con_xp_to_level', 'con_exp_to_lvl', 'con_exp_to_level'
        ]
    )
    async def convert_xp_to_lvl(self, ctx, xp, external=True):
        xp = int(xp.replace(',', ""))
        points = 0
        for lvl in range(99):
            points += math.floor(lvl + 300 * math.pow(2, lvl / 7))
            if math.floor(points / 4) >= xp + 1:
                if external:
                    await ctx.send(
                        f'{xp} xp means that you are level: {lvl}.'
                    )
                else:
                    return lvl
        if external:
            await ctx.send(99)
        else:
            return 99

    @commands.command(
        name='xp_to_99',
        aliases=[
            'xpto99', 'expto99', 'exp_to_99'
        ]
    )
    async def xp_to_99(self, ctx, xp, external=True):
        xp = int(xp.replace(',', ""))
        if external:
            await ctx.send(
                f'{13034431 - xp:,d} xp remaining till Level 99.'
            )
        else:
            return 13034431 - xp

    @commands.command(
        name='xp_to_max',
        aliases=[
            'xptomax', 'exptomax', 'exp_to_max'
        ]
    )
    async def xp_to_max(self, ctx, xp, external=True):
        xp = int(xp.replace(',', ""))
        if external:
            await ctx.send(
                f'{200000000 - xp:,d} xp remaining till Max (200M xp).'
            )
        else:
            return 200000000 - xp

    @commands.command(
        name='xp_to_lvl',
        aliases=[
            'xptolvl', 'xptogoal', 'exptolvl', 'exptolevel', 'xptolevel'
            'exptogoal', 'xp_to_goal', 'exp_to_lvl', 'exp_to_goal'
        ]
    )
    async def xp_to_lvl(self, ctx, xp, lvl, external=True):
        xp = int(xp.replace(',', ""))
        goal_exp = await self.convert_lvl_to_xp(ctx=ctx, lvl=lvl, external=False)
        if external:
            await ctx.send(
                f'{goal_exp - xp:,d} xp remaining till level {lvl}.\nYou are {xp/goal_exp*100:.2f}% to the goal!'
            )
        else:
            return goal_exp - xp


def setup(bot):
    bot.add_cog(Experience(bot))
