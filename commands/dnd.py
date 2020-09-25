# !create_character Vol Fighter 5 "Chaotic Neutral" 900 acrobatics,survival 10,11,12,13,14,15
from commands.utility import read_website, trim, one_in
from discord.ext import commands
from classes import Character, Attributes, Skill


class DND(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="create_character", aliases=['createcharacter'])
    async def create_character(
            self,
            ctx,
            char_name=None,
            class_type=None,
            level: int = 1,
            alignment=None,
            exp: int = 0,
            proficiencies=None,
            attributes=None
    ):
        if proficiencies is not None:
            proficiencies = proficiencies.split(',')
        if attributes is None:
            attributes = Attributes()
        else:
            at = attributes.split(',')
            attributes = Attributes(int(at[0]), int(at[1]), int(at[2]), int(at[3]), int(at[4]), int(at[5]))

        current = Character(
            user_id=ctx.author.id,
            char_name=char_name,
            class_type=class_type,
            level=level,
            alignment=alignment,
            exp=exp,
            proficiencies=proficiencies,
            attributes=attributes
        )
        self.bot.character_list.update({ctx.author.id: current})
        await ctx.send('Created a character object for your UserID!')

    @commands.command(name="dnd", aliases=['query_dnd', 'querydnd', 'dnd_lookup', 'dndlookup'])
    async def dnd(self, ctx, url_suffix):
        results = await read_website(url=f'https://www.dnd5eapi.co/api/{url_suffix}', process_format="json")
        await ctx.send(await trim(results, 2000))

    @commands.command(name="roll", aliases=['roll_skill'])
    async def roll(self, ctx, skill):
        try:
            current = self.bot.character_list[ctx.author.id]
            try:
                current_skill = current.skills[skill]
                try:
                    bonus = current_skill.stat
                    roll = await one_in(20)
                    await ctx.send(f"**{roll + bonus}**\nRoll: {roll}\nBonus: {bonus}")
                except KeyError:
                    await ctx.send("Skill not set correcly. Your stat could not be loaded!")
            except KeyError:
                await ctx.send("Are you sure that's the name of the skill?")
        except KeyError:
            await ctx.send("You don't have a character created or saved currently!")

    @commands.group()
    async def set(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('uhhhhh what are you setting?...')
        try:
            ins = self.bot.character_list[ctx.author.id]
            output = f"Name: {ins.char_name} | Class: Level {ins.level} {ins.class_type}"
            await ctx.send(output, delete_after=5)
        except KeyError:
            self.bot.character_list.update({ctx.author.id: Character(ctx.author.id)})

    @set.command()
    async def attributes(self, ctx, *, attributes=None):
        if attributes is None:
            msg = await ctx.send(
                'Please enter a number for each attribute, and separate each with a comma!\n'
                'Enter stats in this order: \n'
                'Str, Dex, Con, Wis, Int, Cha'
            )

            def check(m):
                return ctx.channel == m.channel and ctx.author == m.author

            try:
                response = await self.bot.wait_for('message', check=check, timeout=10)
                await self.setup_attributes(ctx, response.content.replace(" ", "").split(","))
            except asyncio.TimeoutError:
                await msg.edit(content='Timed Out. Please reissue command.')
        else:
            await ctx.send('Attempting To Update Attributes!', delete_after=30)
            await self.setup_attributes(ctx, attributes.replace(" ", "").split(","))

    @set.command(aliases=['str'])
    async def strength(self, ctx, level: int):
        await ctx.send(
            await self.bot.character_list[ctx.author.id].set_attribute("strength", level), delete_after=10
        )

    @set.command(aliases=['dex'])
    async def dexterity(self, ctx, level: int):
        await ctx.send(
            await self.bot.character_list[ctx.author.id].set_attribute("dexterity", level), delete_after=10
        )

    @set.command(aliases=['con'])
    async def constitution(self, ctx, level: int):
        await ctx.send(
            await self.bot.character_list[ctx.author.id].set_attribute("constitution", level), delete_after=10
        )

    @set.command(aliases=['int'])
    async def intelligence(self, ctx, level: int):
        await ctx.send(
            await self.bot.character_list[ctx.author.id].set_attribute("intelligence", level), delete_after=10
        )

    @set.command(aliases=['wis'])
    async def wisdom(self, ctx, level: int):
        await ctx.send(
            await self.bot.character_list[ctx.author.id].set_attribute("wisdom", level), delete_after=10
        )

    @set.command(aliases=['cha'])
    async def charisma(self, ctx, level: int):
        await ctx.send(
            await self.bot.character_list[ctx.author.id].set_attribute("charisma", level), delete_after=10
        )

    async def setup_attributes(self, ctx, st):
        output = []
        stats = ['Str', 'Dex', 'Con', 'Wis', 'Int', 'Cha']
        for i in range(len(st)):
            output.append(f"{stats[i]}: {st[i]}")
            st[i] = int(st[i])
        else:
            output = "\n".join(output)
            if len(st) == 6:
                self.bot.character_list[ctx.author.id].attributes = Attributes(st[0], st[1], st[2], st[3], st[4], st[5])
                await ctx.send(f'Attribute object has been created for {ctx.author.id}:\n```{output}```')
            else:
                await ctx.send(f'Failed, Did not update the character! Please check format')


def setup(bot):
    bot.add_cog(DND(bot))
