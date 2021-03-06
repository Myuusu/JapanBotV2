import asyncio
import os
import re
from datetime import datetime
from random import randrange

import discord
from config import bot_token, t_b, t_c, t_c_a, t_q_h, t_a_h
from discord.ext import commands, tasks

from classes import Guild
from commands.utility import find_message_in_channel, find_string_in_channel_content
from storage.account_list import account_list
from storage.character_list import character_list
from storage.eight_ball_responses import eight_ball_responses
from storage.guild_list import guild_list
from storage.level_list import level_list
from storage.slot_machines import slot_machines
from storage.station_list import station_list
from storage.timer_list import timer_list
from storage.trivia_list import trivia_list


class Bot(commands.Bot):
    def __init__(self):
        super(Bot, self).__init__(case_insensitive=True, command_prefix=self.get_prefix)
        self.trivia_channel_answers = self.get_channel(t_c_a)
        self.eight_ball_responses = eight_ball_responses
        self.slot_machines = slot_machines
        self.account_list = account_list
        self.guild_list = guild_list
        self.level_list = level_list
        self.station_list = station_list
        self.trivia_list = trivia_list
        self.timer_list = timer_list
        self.character_list = character_list

        self.last_slot_machines = slot_machines
        self.last_account_list = account_list
        self.last_guild_list = guild_list
        self.last_level_list = level_list
        self.last_station_list = station_list
        self.last_trivia_list = trivia_list
        self.last_timer_list = timer_list
        self.last_character_list = character_list

        for filename in os.listdir('./commands'):
            if filename.endswith('.py'):
                self.load_extension(f'commands.{filename[:-3]}')

        self.errors = []

    @tasks.loop(seconds=15, count=None, reconnect=True)
    async def update(self):
        if self.guild_list != self.last_guild_list:
            await self.update_guild_list()

        if self.account_list != self.last_account_list:
            await self.update_account_list()

        if self.slot_machines != self.last_slot_machines:
            await self.update_slot_machines()

        if self.trivia_list != self.last_trivia_list:
            await self.update_trivia_list()

        if self.timer_list != self.last_timer_list:
            await self.update_timer_list()

    async def remove_timers(self, indices_to_remove):
        if indices_to_remove is not None:
            for i in indices_to_remove:
                self.timer_list[i].pop()

    async def update_timer_list(self):
        output = []
        items_to_remove = []
        now = datetime.now()
        for i in self.timer_list.keys():
            item = self.timer_list[i]
            if item.end_time < now:
                items_to_remove.append(i)
                user = self.get_user(item.user_id)
                if user is None:
                    print(
                        f'{item.name} timer expired at {item.end_time}, '
                        f'but user with id {item.user_id} could not be found.'
                    )
                else:
                    await user.send(f'{item.name} timer expired at {item.end_time}')
            else:
                output.append(item.get_json())
        else:
            await self.remove_timers(items_to_remove)
            output_string = ",\n    ".join(output)
            with open('storage/timer_list.py', mode='w+', encoding="ascii", errors="backslashreplace") as fp:
                fp.write(f'from classes import Timer\n\ntimer_list = {{\n    {output_string}\n}}\n')
            fp.close()
            self.last_timer_list = self.timer_list

    async def update_guild_list(self):
        output = []
        for i in self.guild_list.keys():
            output.append(self.guild_list[i].get_json())
        else:
            output_string = ",\n    ".join(output)
            with open('storage/guild_list.py', mode='w+', encoding="ascii", errors="backslashreplace") as fp:
                fp.write(f'from classes import Guild\n\nguild_list = {{\n    {output_string}\n}}\n')
            fp.close()
            self.last_guild_list = self.guild_list

    async def update_account_list(self):
        output = []
        for i in self.account_list.keys():
            output.append(self.account_list[i].get_json())
        else:
            output_string = ",\n    ".join(output)
            with open('storage/account_list.py', mode='w+', encoding="ascii", errors="backslashreplace") as fp:
                fp.write(f'from classes import Account\n\naccount_list = {{\n    {output_string}\n}}\n')
            fp.close()
            self.last_account_list = self.account_list

    async def update_slot_machines(self):
        output = []
        for i in self.slot_machines.keys():
            output.append(self.slot_machines[i].get_json())
        else:
            output_string = ",\n    ".join(output)
            with open('storage/slot_machines.py', mode='w+', encoding="ascii", errors="backslashreplace") as fp:
                fp.write(f'from classes import SlotMachine, Emoji\n\nslot_machines = {{\n    {output_string}\n}}\n')
            fp.close()
            self.last_slot_machines = self.slot_machines

    async def update_trivia_list(self):
        output = []
        for i in self.trivia_list:
            question = self.trivia_list[i]["question"]
            answer = self.trivia_list[i]["answer"]
            output.append(
                f'    "{question}": {{\n        "question": "{question}",\n        "answer": "{answer}"\n    }}'
            )
        else:
            output_string = ",\n".join(output)
            contents_to_write = f'trivia_list = {{\n{output_string}\n}}\n'
            with open('storage/trivia_list.py', mode='w+', encoding="ascii", errors="backslashreplace") as fp:
                fp.write(contents_to_write)
            fp.close()
            self.last_trivia_list = self.trivia_list

    async def get_prefix(self, message):
        try:
            self.guild_list[message.guild.id].message_count += 1
        except KeyError:
            self.guild_list.update({message.guild.id: Guild(guild_id=message.guild.id)})
        finally:
            return self.guild_list[message.guild.id].prefix

    async def purge_channel(self, channel):
        await channel.purge(limit=None)
        output = []
        for i in self.trivia_list.keys():
            if self.trivia_list[i].answer is None:
                output.append(self.trivia_list[i].question)
            else:
                if not await find_string_in_channel_content(i, channel):
                    await channel.send(
                        f'**{self.trivia_list[i].question}** ```{self.trivia_list[i].answer}```'
                    )
        else:
            if output:
                output_string = "\n".join(output)
                print(f'Needs Answers: \n{output_string}')

    async def on_ready(self):
        print("Ready")
        try:
            await self.update.start()
        except RuntimeError:
            print('Previous task still running.')
        # if self.trivia_channel_answers is not None:
        # await self.purge_channel(self.trivia_channel_answers)

    async def on_guild_join(self, guild):
        self.guild_list.update({guild.id: Guild(guild_id=guild.id, active=True)})

    async def on_guild_remove(self, guild):
        self.guild_list.update({guild.id: Guild(guild_id=guild.id, active=False)})

    async def on_message(self, message):
        if message.channel.id in t_c and message.author.id in t_b and message.content != '':
            if t_q_h in message.content:
                for string in t_a_h:
                    if string in message.content:
                        return await self.process_commands(message)
                else:
                    return await self.process_trivia_question(message=message)
            else:
                return await self.process_commands(message)
        else:
            return await self.process_commands(message)

    async def process_trivia_question(self, message):
        if self.trivia_channel_answers is None:
            self.trivia_channel_answers = self.get_channel(t_c_a)
        question = re.sub(r'^.*\.\.\.\*\* ', '', message.content)
        try:
            current = self.trivia_list[question]
            if current["answer"] in ["None", "", " ", None]:
                await message.channel.send("Question Located But No Solution Found; Please Update.")
            else:
                await asyncio.sleep(randrange(2))
                await message.channel.send(current["answer"])
                if not await find_message_in_channel(message=message, channel=self.trivia_channel_answers):
                    await self.trivia_channel_answers.send(f'**{question}**\n```{current["answer"]}```')
        except KeyError:
            await message.channel.send("Question Not Located. Added To List; Please Update.")
            trivia_question = {question: {"question": question, "answer": "None"}}
            print(trivia_question)
            self.trivia_list.update(trivia_question)

    async def on_command_error(self, ctx, exception):
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
        self.errors.append(exception)


bot = Bot()
bot.run(bot_token, reconnect=True)
