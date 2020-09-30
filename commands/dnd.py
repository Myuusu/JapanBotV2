import asyncio

from discord import Embed
from discord.ext import commands

from classes import Character, Attributes
from commands.utility import read_website, trim, one_in
from storage.dnd_list import class_list, race_list, skill_list, alignment_list


class DND(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.races = "\n".join(race_list)
        self.skills = "\n".join(skill_list)
        self.class_types = "\n".join(class_list)
        self.alignments = "\n".join(alignment_list)

    @commands.command(name="create_character", aliases=['make_char', 'createcharacter'])
    async def create_character(
            self,
            ctx,
            char_name=None,
            class_type=None,
            level: int = 1,
            background=None,
            alignment=None,
            race=None,
            exp: int = 0,
            proficiencies=None,
            attributes=None
    ):
        if isinstance(class_type, Class):
            class_type = class_type
        elif class_type in class_list:
            class_type = class_list[class_type]
        else:
            class_type = None
        if proficiencies is not None:
            proficiencies = dict(proficiencies.split(','))
        if attributes is None or len(attributes.split(',')) != 6:
            attributes = Attributes()
        else:
            att = attributes.split(',')
            if len(att) == 6:
                attributes = Attributes(
                    int(att[0]), int(att[1]), int(att[2]), int(att[3]), int(att[4]), int(att[5])
                )
            else:
                attributes = Attributes()

        current = Character(
            user_id=ctx.author.id,
            char_name=char_name,
            class_type=class_type,
            level=level,
            background=background,
            alignment=alignment,
            race=race,
            exp=exp,
            proficiencies=proficiencies,
            attributes=attributes
        )
        self.bot.character_list.update({ctx.author.id: current})
        await ctx.send('Created a character object for your UserID!', delete_after=10)

    @commands.command(name="dnd", aliases=['query_dnd', 'querydnd', 'dnd_lookup', 'dndlookup'])
    async def dnd(self, ctx, url_suffix):
        results = await read_website(url=f'https://www.dnd5eapi.co/api/{url_suffix}', process_format="json")
        await ctx.send(await trim(results, 2000))

    @commands.command(name="roll", aliases=['roll_skill'])
    async def roll(self, ctx, *, skill):
        character = await(self.character_found(ctx))
        if character:
            if skill in character.skills:
                bonus = character.skills[skill].stat
                roll = await one_in(20)
                await ctx.send(f"**{roll + bonus}**\nRoll: {roll}\nBonus: {bonus}")
            else:
                for i in character.skills:
                    if skill in character.skills[i].aliases:
                        bonus = character.skills[i].stat
                        roll = await one_in(20)
                        await ctx.send(f"**{roll + bonus}**\nRoll: {roll}\nBonus: {bonus}")
                        return
                else:
                    await ctx.send("Are you sure that's the name of the skill?", delete_after=10)

    @commands.group()
    async def set(self, ctx):
        if await self.character_found(ctx) and ctx.invoked_subcommand is None:
            await ctx.send('uhhhhh what are you setting?... enter additional info', delete_after=10)

    @set.command(aliases=['str'])
    async def strength(self, ctx, level=None):
        attr = "strength"
        if level is None:
            result = await self.prompt(ctx=ctx, question=f"Enter {attr} level", output="int")
            if result is not False:
                await self.set_attribute(ctx, attr, result)
        else:
            await self.set_attribute(ctx, attr, int(level))

    @set.command(aliases=['dex'])
    async def dexterity(self, ctx, level=None):
        attr = "dexterity"
        if level is None:
            result = await self.prompt(ctx=ctx, question=f"Enter {attr} level", output="int")
            if result is not False:
                await self.set_attribute(ctx, attr, result)
        else:
            await self.set_attribute(ctx, attr, int(level))

    @set.command(aliases=['con'])
    async def constitution(self, ctx, level=None):
        attr = "constitution"
        if level is None:
            result = await self.prompt(ctx=ctx, question=f"Enter {attr} level", output="int")
            if result is not False:
                await self.set_attribute(ctx, attr, result)
        else:
            await self.set_attribute(ctx, attr, int(level))

    @set.command(aliases=['int'])
    async def intelligence(self, ctx, level=None):
        attr = "intelligence"
        if level is None:
            result = await self.prompt(ctx=ctx, question=f"Enter {attr} level", output="int")
            if result is not False:
                await self.set_attribute(ctx, attr, result)
        else:
            await self.set_attribute(ctx, attr, int(level))

    @set.command(aliases=['wis'])
    async def wisdom(self, ctx, level=None):
        attr = "wisdom"
        if level is None:
            result = await self.prompt(ctx=ctx, question=f"Enter {attr} level", output="int")
            if result is not False:
                await self.set_attribute(ctx, attr, result)
        else:
            await self.set_attribute(ctx, attr, int(level))

    @set.command(aliases=['cha'])
    async def charisma(self, ctx, level=None):
        attr = "charisma"
        if level is None:
            result = await self.prompt(ctx=ctx, question=f"Enter {attr} level", output="int")
            if result is not False:
                await self.set_attribute(ctx, attr, result)
        else:
            await self.set_attribute(ctx, attr, int(level))

    @set.command(aliases=['atts', 'ats'])
    async def attributes(self, ctx, *, attributes=None):
        if attributes is None:
            result = await self.prompt(ctx, question="Enter attributes separated by commas in this order:\nStr, Dex, "
                                                     "Con, Wis, Int, Cha")
            if result is not False:
                await self.update_valid_attributes(ctx, result.replace(" ", "").split(","))
        else:
            await self.update_valid_attributes(ctx, attributes.replace(" ", "").split(","))

    @set.command(aliases=['skills', 'profs'])
    async def proficiencies(self, ctx, *, skills=None):
        if skills is None:
            result = await self.prompt(ctx=ctx, question="Enter skills separated by commas", description=self.skills)
            if result is not False:
                await self.process_valid_skills(ctx, result.split(','))
        else:
            await self.process_valid_skills(ctx, skills.split(","))

    @set.command(aliases=['toggle_prof', 'toggle prof'])
    async def prof(self, ctx, skill=None):
        if skill is None:
            result = await self.prompt(ctx=ctx, question="Enter skill to toggle proficiency", description=self.skills)
            if result is not False:
                await self.process_valid_skill(ctx, result.split(','))
        else:
            await self.process_valid_skill(ctx, skill)

    @set.command()
    async def alignment(self, ctx, *, alignment=None):
        if alignment is None:
            result = await self.prompt(ctx=ctx, question="Enter an alignment", description=self.alignments)
            if result is not False:
                await self.process_valid_alignment(ctx, result)
        else:
            await self.process_valid_alignment(ctx, alignment)

    @set.command()
    async def race(self, ctx, *, race=None):
        if race is None:
            result = await self.prompt(ctx=ctx, question="Enter a race", description=self.races)
            if result is not False:
                await self.process_valid_race(ctx, result)
        else:
            await self.process_valid_race(ctx, race)

    @set.command(aliases=['class'])
    async def class_type(self, ctx, *, class_type=None):
        if class_type is None:
            result = await self.prompt(ctx=ctx, question="Enter a class", description=self.class_types)
            if result is not False:
                await self.process_valid_class(ctx, result)
        else:
            await self.process_valid_class(ctx, class_type)

    @commands.command(aliases=['print'])
    async def output(self, ctx):
        if await(self.character_found(ctx)):
            await self.bot.character_list[ctx.author.id].output(ctx)

    """ Helper function that prompts the user for additional input """

    async def prompt(self, ctx, question: str = None, description: str = None, output="str"):
        if question is None:
            if description is not None:
                await ctx.send(embed=Embed(title="Question", description=description), delete_after=10)
        else:
            await ctx.send(embed=Embed(title=question, description=description), delete_after=10)

        def check(m):
            return ctx.channel == m.channel and ctx.author == m.author

        try:
            response = await self.bot.wait_for('message', check=check, timeout=10)
            if output == "str":
                return response.content
            elif output == "int":
                return int(response.content)
        except asyncio.TimeoutError:
            await ctx.send('Timed Out. Please reissue command.', delete_after=10)
        return False

    """ Helper function that prevents commands from executing for any users without a character created """

    async def character_found(self, ctx):
        if ctx.author.id in self.bot.character_list:
            return self.bot.character_list[ctx.author.id]
        else:
            await ctx.message.delete()
            await ctx.send('Character Not Found. Please use the make_char command.', delete_after=10)
            return False

    """ Helper function that cleans up the set.attributes command group """

    async def set_attribute(self, ctx, attribute, level: int):
        await ctx.send(await self.bot.character_list[ctx.author.id].set_attribute(attribute, level), delete_after=10)

    """ Helper function to check user input and filter out bad strings that were inputted as 'alignment' """

    async def process_valid_alignment(self, ctx, alignment):
        if alignment in alignment_list:
            self.bot.character_list[ctx.author.id].alignment = alignment_list[alignment]
        else:
            for i in alignment_list:
                if alignment in alignment_list[i]["aliases"]:
                    self.bot.character_list[ctx.author.id].alignment = alignment_list[i]
                    await ctx.send(f'Alignment set to {alignment_list[i]["name"]}.', delete_after=10)
                    return
            else:
                await ctx.send('Alignment could not be updated successfully. Ensure proper spelling.', delete_after=10)

    """ Helper function to check user input and filter out bad strings that were inputted as 'skill' """

    async def process_valid_skill(self, ctx, skill):
        if skill in skill_list:
            await self.toggle_prof(ctx, skill)
        else:
            for i in skill_list:
                if skill in skill_list[i]["aliases"]:
                    await self.toggle_prof(ctx, skill_list[i]["name"])
                    return
            else:
                await ctx.send('Skill could not be updated successfully. Ensure proper spelling.', delete_after=10)

    """ Helper function to append / remove skill to / from proficiencies """

    async def toggle_prof(self, ctx, skill):
        current = self.bot.character_list[ctx.author.id]
        try:
            current.proficiencies.remove(skill)
        except (ValueError, KeyError):
            current.proficiencies.append(skill)
        finally:
            await current.reload_skills()
            await ctx.send('Successfully updated proficiencies and skills.', delete_after=10)

    """ Helper function to check user input and filter out bad strings that were inputted as 'skills' """

    async def process_valid_skills(self, ctx, skills):
        verified_skills = []
        incorrect_skills = []
        for i in skills:
            if i in skill_list:
                verified_skills.append(i)
            else:
                incorrect_skills.append(i)
        else:
            if incorrect_skills is not None:
                await ctx.send(f"Could not process the following 'skills':\n{','.join(incorrect_skills)}")
            if verified_skills is not None:
                self.bot.character_list[ctx.author.id].proficiencies = verified_skills
                await self.bot.character_list[ctx.author.id].reload_skills()
                await ctx.send('Successfully updated proficiencies and skills.', delete_after=10)

    """ Helper function to check an array and create an Attributes object with it. """

    async def update_valid_attributes(self, ctx, att):
        if len(att) == 6:
            self.bot.character_list[ctx.author.id].attributes = Attributes(
                int(att[0]), int(att[1]), int(att[2]), int(att[3]), int(att[4]), int(att[5])
            )
            await ctx.send('Successfully updated Attributes.', delete_after=10)
        else:
            await ctx.send('Failed, Did not update the character! Please check format', delete_after=10)

    """ Helper function to check that the race is available. """

    async def process_valid_race(self, ctx, race):
        if race in race_list:
            self.bot.character_list[ctx.author.id].race = race
            await ctx.send('Successfully Updated Race.', delete_after=10)
        else:
            await ctx.send(embed=self.race_embed, delete_after=10)

    """ Helper function to check that class is available. """

    async def process_valid_class(self, ctx, class_type):
        if class_type in class_list:
            self.bot.character_list[ctx.author.id].class_type = class_type
            await ctx.send(content='Updated class.', delete_after=10)
        else:
            await ctx.send(embed=self.class_type_embed, delete_after=10)


def setup(bot):
    bot.add_cog(DND(bot))
