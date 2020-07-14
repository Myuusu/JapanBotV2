import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio


class Stations(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['s', 'st'])
    async def stations(self, ctx):
        await ctx.send('Please use the following commands depending on the station you want to listen to:\n'
                       '``!r:   Anime Radio``\n'
                       '``!r1:  Jazz Sakura - asia DREAM radio``\n'
                       '``!r2:  Japan Hits - Asia DREAM Radio``\n'
                       '``!r3:  J-Pop Powerplay``\n'
                       '``!r4:  J-Club Powerplay Hip-Hop``\n'
                       '``!r5:  J-Pop Sakura 懐かしい``\n'
                       '``!r6:  J-Pop Powerplay Kawaii``\n'
                       '``!r7:  J-Rock Powerplay``\n'
                       '``!r8:  Vocaloid Radio``\n'
                       '``!r9 : Japanimradio``\n'
                       '``!r10: FM 845``\n'
                       '``!r11: Bitter Sweet Music JP``\n'
                       '``!r12: Banana FM``\n'
                       '``!r13: Musashino FM``\n'
                       '``!r14: Radio Kanazawa``'
                       )


def setup(bot):
    bot.add_cog(Stations(bot))
