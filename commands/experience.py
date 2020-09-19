from math import ceil

from discord.ext import commands

from commands.utility import clean_float


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
        lvl = ceil(await clean_float(lvl))
        try:
            if external:
                return await ctx.send(f'Level {lvl} is reached at: {self.bot.level_list[lvl].exp} xp.')
            else:
                return self.bot.level_list[lvl].exp
        except KeyError:
            return await ctx.send('Level Not Recognized! Please reissue command.')

    @commands.command(
        name='convert_xp_to_lvl',
        aliases=[
            'conxptolvl', 'conxptolevel', 'conexptolvl', 'conexptolevel',
            'con_xp_to_lvl', 'con_xp_to_level', 'con_exp_to_lvl', 'con_exp_to_level'
        ]
    )
    async def convert_xp_to_lvl(self, ctx, xp, external=True):
        xp = ceil(await clean_float(xp))
        for i in self.bot.level_list.keys():
            if i == 99:
                if external:
                    await ctx.send(99)
                    break
                else:
                    return 99
            elif self.bot.level_list[i].exp <= xp < self.bot.level_list[i+1].exp:
                if external:
                    await ctx.send(self.bot.level_list[i].level)
                    break
                else:
                    return self.bot.level_list[i].level

    @commands.command(name='xp_to_99', aliases=['xpto99', 'expto99', 'exp_to_99'])
    async def xp_to_99(self, ctx, xp, external=True):
        xp = ceil(await clean_float(xp))
        if external:
            await ctx.send(f'{13034431 - xp:,} xp remaining till Level 99.')
        else:
            return 13034431 - xp

    @commands.command(name='xp_to_max', aliases=['xptomax', 'exptomax', 'exp_to_max'])
    async def xp_to_max(self, ctx, xp, external=True):
        xp = ceil(await clean_float(xp))
        if external:
            await ctx.send(f'{200000000 - xp:,} xp remaining till Max (200M xp).')
        else:
            return 200000000 - xp

    @commands.command(
        name='xp_to_lvl',
        aliases=[
            'xptolvl', 'xptogoal', 'exptolvl', 'exptolevel', 'xp_to_level'
            'xptolevel', 'exptogoal', 'xp_to_goal', 'exp_to_lvl', 'exp_to_goal'
        ]
    )
    async def xp_to_lvl(self, ctx, xp, lvl, external=True):
        xp = ceil(await clean_float(xp))
        goal_exp = await self.convert_lvl_to_xp(ctx=ctx, lvl=lvl, external=False)
        if external:
            await ctx.send(
                f'{goal_exp - xp:,d} xp remaining till level {lvl}.'
                f'\nYou are {xp/goal_exp*100:.2f}% to the goal!'
            )
        else:
            return goal_exp - xp


def setup(bot):
    bot.add_cog(Experience(bot))
