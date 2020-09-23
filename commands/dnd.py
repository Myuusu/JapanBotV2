from commands.utility import read_website, trim
from discord.ext import commands
from classes import Character, Attributes, Skill


class DND(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="create_character",
        aliases=['createcharacter']
    )
    async def create_character(
            self,
            ctx,
            name: str = None,
            class_type: str = None,
            level: int = 1,
            alignment: str = None,
            exp: int = 0,
            attributes: Attributes = Attributes(),
            proficiencies: [] = None
    ):
        current = Character(
            user_id=ctx.author.id,
            name=name,
            class_type=class_type,
            level=level,
            alignment=alignment,
            exp=exp,
            attributes=attributes,
            proficiencies=proficiencies)
        self.bot.character_list.update({ctx.author.id: current})
        await ctx.send('Created a character object for your UserID!')

    @commands.command(
        name="query_dnd_api",
        aliases=['querydndapi', 'query_dnd', 'querydnd', 'dnd_lookup', 'dndlookup']
    )
    async def query_dnd_api(self, ctx, url_suffix):
        results = await read_website(url=f'https://www.dnd5eapi.co/api/{url_suffix}', process_format="json")
        await ctx.send(await trim(results, 2000))


def setup(bot):
    bot.add_cog(DND(bot))
