import asyncio
import os
import re
from datetime import datetime
from random import randrange

import discord
import psutil
from discord.ext import commands, tasks

from classes import Guild, Trivia
from config import bot_token, t_b, t_c, t_c_a, t_q_h, t_a_h, lavalink_exe_path
from storage.account_list import account_list
from storage.eight_ball_responses import eight_ball_responses
from storage.guild_list import guild_list
from storage.level_list import level_list
from storage.slot_machines import slot_machines
from storage.station_list import station_list
from storage.timer_list import timer_list
from storage.trivia_list import trivia_list


async def find_duplicate_messages(channel):
    if channel is None:
        print('Channel Is Not Found In find_duplicate_messages Function')
        return None
    found = []
    duplicates = []

    def transform(message):
        return {message.content, message.id}

    async for content, message_id in channel.history(limit=None).map(transform):
        if content in found:
            print(f"Duplicate Found: {content}")
            duplicates.append(message_id)
        else:
            found.append(content)
    else:
        return duplicates


async def remove_duplicate_messages_in_channel(channel):
    if channel is None:
        print('Channel Is Not Found In remove_duplicate_messages_in_channel Function')
    duplicate_messages = await find_duplicate_messages(channel)
    if duplicate_messages is not None:
        for i in duplicate_messages:
            msg = await channel.fetch_message(id=i)
            if msg is not None:
                await msg.delete()


async def find_message_in_channel(message, channel):
    async for i in channel.history(limit=None):
        if message == i:
            return True
    else:
        return False


async def find_string_in_channel_content(content, channel):
    async for i in channel.history(limit=None):
        if content in i.content:
            return True
    else:
        return False


class Bot(commands.Bot):
    def __init__(self):
        super(Bot, self).__init__(case_insensitive=True, command_prefix=self.get_prefix)
        self.trivia_channel_answers = {}
        self.account_list = account_list
        self.guild_list = guild_list
        self.level_list = level_list
        self.eight_ball_responses = eight_ball_responses
        self.slot_machines = slot_machines
        self.station_list = station_list
        self.trivia_list = trivia_list
        self.timer_list = timer_list

        try:
            os.startfile(lavalink_exe_path)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

        for filename in os.listdir('./commands'):
            if filename.endswith('.py'):
                self.load_extension(f'commands.{filename[:-3]}')

    @tasks.loop(seconds=30, count=None, reconnect=True)
    async def update(self):
        await self.update_guild_list()
        await self.update_account_list()
        await self.update_slot_machines()
        await self.update_trivia_list()
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

    async def update_guild_list(self):
        output = []
        for i in self.guild_list.keys():
            output.append(self.guild_list[i].get_json())
        else:
            output_string = ",\n    ".join(output)
            with open('storage/guild_list.py', mode='w+', encoding="ascii", errors="backslashreplace") as fp:
                fp.write(f'from classes import Guild\n\nguild_list = {{\n    {output_string}\n}}\n')
            fp.close()

    async def update_account_list(self):
        output = []
        for i in self.account_list.keys():
            output.append(self.account_list[i].get_json())
        else:
            output_string = ",\n    ".join(output)
            with open('storage/account_list.py', mode='w+', encoding="ascii", errors="backslashreplace") as fp:
                fp.write(f'from classes import Account\n\naccount_list = {{\n    {output_string}\n}}\n')
            fp.close()

    async def update_slot_machines(self):
        output = []
        for i in self.slot_machines.keys():
            output.append(self.slot_machines[i].get_json())
        else:
            output_string = ",\n    ".join(output)
            with open('storage/slot_machines.py', mode='w+', encoding="ascii", errors="backslashreplace") as fp:
                fp.write(f'from classes import SlotMachine, Emoji\n\nslot_machines = {{\n    {output_string}\n}}\n')
            fp.close()

    async def update_trivia_list(self):
        output = []
        for i in self.trivia_list.keys():
            output.append(self.trivia_list[i].get_json())
        else:
            output_string = ",\n    ".join(output)
            with open('storage/trivia_list.py', mode='w+', encoding="ascii", errors="backslashreplace") as fp:
                fp.write(f'from classes import Trivia\n\ntrivia_list = {{\n    {output_string}\n}}\n')
            fp.close()

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
        self.update.start()
        self.trivia_channel_answers = self.get_channel(t_c_a)
        if self.trivia_channel_answers is not None:
            await self.purge_channel(self.trivia_channel_answers)
            print("Finished Purging Channel.", end="\r")

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
                    return await self.process_trivia_question(message=message, channel=self.trivia_channel_answers)
            else:
                return await self.process_commands(message)
        else:
            return await self.process_commands(message)

    async def process_trivia_question(self, message, channel=None):
        if channel is None:
            channel = message.channel
        question = re.sub(r'^.*\.\.\.\*\* ', '', message.content)
        try:
            current = self.trivia_list[question].answer
            if current == '':
                await message.channel.send("Question Located But No Solution Found; Please Update.")
            else:
                await asyncio.sleep(randrange(3))
                await message.channel.send(current)
            if not await find_message_in_channel(message=message, channel=channel):
                await channel.send(f'**{question}**\n```{current}```')
        except KeyError:
            self.trivia_list.update({question: Trivia(question=question)})
            await message.channel.send("Question Not Located. Inserted, But Needs Solution.")

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


bot = Bot()
bot.run(bot_token, reconnect=True)

"""
To do list:

Gambling:
Weighting modifications
Jackpot announcements on Animal slot for lion
Server admin right to toggle "Jackpot Winner" role

Conjugation:
Fix elements, unable to locate currently
Fix Issue with overload of conjugations

Station:
Add a type and subtype for each station so that users can filter through genres

Jisho:
Fix encoding issue when use a space for ex. to go
Possibly look into changing from jisho to the website conjugation uses


Papago sentence translator:
Add the API we talked bout of https://papago.naver.com/ to translate entire sentences
Add the audio output of the translated sentences into the VC function from music.py

Stroke order:
Create a new command called !so for pulling pictures of the stroke orders for kanji
        https://jisho.org/search/%23kanji%20(input) <- make sure you type the japanese word in kanji
        https://gyazo.com/fe9f8c8b4ea6661107c04203b5bc0bf1 <-- reference picture
If possible, have the automated drawing left side of the picture also be output as a gif or something
        https://gyazo.com/8f61500ae94e96175bc7433b5e7dd619 <-- reference picture
"""
