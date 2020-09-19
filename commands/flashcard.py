import asyncio
from datetime import datetime, timedelta

import discord
from discord.ext import commands

from classes import Trivia, Timer


async def create_timer(end_time, author_id, timer_name):
    return Timer(end_time, author_id, timer_name)


class Flashcard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='update_trivia',
        aliases=[
            'update_trivia_answer',
            'trivia_update',
            'update_flashcard',
            'flashcard_update',
            'updatetriviaanswer',
            'triviaupdate',
            'updateflashcard',
            'flashcardupdate'
        ]
    )
    async def update_trivia(self, ctx, *, question):
        msg = await ctx.send("Please enter the answer to the question.")

        def check(m):
            return ctx.channel == m.channel and ctx.author == m.author
        try:
            response = await self.bot.wait_for('message', check=check, timeout=10)
            self.bot.trivia_list.update({question: Trivia(question=question, answer=response.content)})
            await msg.edit(content=f'Updated Successfully.```Question: {question}\nAnswer: {response.content}```')
            not_in_channel = True
            async for message in self.bot.trivia_channel_answers.history():
                if question in message.content:
                    await message.edit(content=f'**{question}**\n```{response.content}```')
                    not_in_channel = False
            else:
                if not_in_channel:
                    await self.bot.trivia_channel_answers.send(f'**{question}**\n```{response.content}```')

        except asyncio.TimeoutError:
            await msg.edit(content='Timed Out. Please reissue command.')

    @commands.command(
        name='set_timer',
        aliases=[
            'start_timer',
            'timer_start',
            'timer',
            'starttimer',
            'timerstart',
            'settimer',
            'timer_set',
            'timerset'
        ]
    )
    async def set_timer(self, ctx, time="00:00:05", name="Reminder"):
        [hours, minutes, seconds] = time.split(":")
        now = datetime.now()
        x = now + timedelta(seconds=int(hours) * 3600 + int(minutes) * 60 + int(seconds))
        new_timer = await create_timer(x, ctx.author.id, name)
        self.bot.timer_list.update({f'"{ctx.author.id}|{name}"': new_timer})
        await ctx.send(f'{name} timer has been set at {now.time()}. It will expire at {x.time()}')

    @commands.command(
        name='timers',
        aliases=[
            'lookup_timer',
            'timer_lookup',
            'timer_status',
            'status_timer'
        ]
    )
    async def timer(self, ctx):
        output = []
        for i in self.bot.timer_list.keys():
            current = self.bot.timer_list[i]
            if current.user_id == ctx.author.id:
                output.append(f'{current.name} timer will end at {current.end_time}')
        else:
            if output:
                output_string = "\n".join(output)
                await ctx.send(f'Your current timers:\n{output_string}')
            else:
                await ctx.send('You have no active timers!')

    @staticmethod
    async def on_command_error(ctx, exception):
        if isinstance(exception, commands.CommandNotFound):
            await ctx.send('Invalid command used! Please try again.')
        elif isinstance(exception, commands.CommandOnCooldown):
            await ctx.send(exception)
        elif isinstance(exception, commands.MissingRequiredArgument):
            await ctx.send(f"```{exception}```")
        elif isinstance(exception, TimeoutError):
            await ctx.send("This operation ran out of time! Please try again")
        elif isinstance(exception, discord.Forbidden):
            await ctx.send("Error: This command requires the bot to have permission to send links.")
        else:
            print(f'Context: {ctx}\nException: {exception}')


def setup(bot):
    bot.add_cog(Flashcard(bot))
