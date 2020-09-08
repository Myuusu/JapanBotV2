import asyncio
import discord
import os
import re
import traceback
from classes import Guild, Account, LolAccount, Trivia
from commands.utility import trim
from config import bot_token, t_b, t_c, t_c_a, t_q_h, t_a_h
from discord.ext import commands, tasks
from random import randrange
from storage.account_list import account_list
from storage.eight_ball_responses import eight_ball_responses
from storage.guild_list import guild_list
from storage.level_list import level_list
from storage.slot_machines import slot_machines
from storage.station_list import station_list
from storage.trivia_list import trivia_list


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

        for filename in os.listdir('./commands'):
            if filename.endswith('.py'):
                self.load_extension(f'commands.{filename[:-3]}')

    @tasks.loop(seconds=60)
    async def update(self):
        await self.wait_until_ready()
        await self.update_guild_list()
        await self.update_account_list()
        await self.update_slot_machines()
        await self.update_trivia_list()

    async def update_guild_list(self):
        output = []
        for iter in self.guild_list.keys():
            output.append(self.guild_list[iter].get_json())
        else:
            output_string = ",\n    ".join(output)
            with open('storage/guild_list.py', mode='w+', encoding="ascii", errors="backslashreplace") as fp:
                fp.write(f'from classes import Guild\n\nguild_list = {{\n    {output_string}\n}}\n')

    async def update_account_list(self):
        output = []
        for iter in self.account_list.keys():
            output.append(self.account_list[iter].get_json())
        else:
            output_string = ",\n    ".join(output)
            with open('storage/account_list.py', mode='w+', encoding="ascii", errors="backslashreplace") as fp:
                fp.write(f'from classes import Account\n\naccount_list = {{\n    {output_string}\n}}\n')

    async def update_slot_machines(self):
        output = []
        for iter in self.slot_machines.keys():
            output.append(self.slot_machines[iter].get_json())
        else:
            output_string = ",\n    ".join(output)
            with open('storage/slot_machines.py', mode='w+', encoding="ascii", errors="backslashreplace") as fp:
                fp.write(f'from classes import SlotMachine, Emoji\n\nslot_machines = {{\n    {output_string}\n}}\n')

    async def update_trivia_list(self):
        output = []
        for iter in self.trivia_list.keys():
            output.append(self.trivia_list[iter].get_json())
        else:
            output_string = ",\n    ".join(output)
            with open('storage/trivia_list.py', mode='w+', encoding="ascii", errors="backslashreplace") as fp:
                fp.write(f'from classes import Trivia\n\ntrivia_list = {{\n    {output_string}\n}}\n')

    async def get_prefix(self, message):
        try:
            self.guild_list[message.guild.id].message_count += 1
        except KeyError:
            self.guild_list.update({guild_id: Guild(guild_id=guild_id)})
        finally:
            return self.guild_list[message.guild.id].prefix

    async def on_ready(self):
        self.update.start()
        self.trivia_channel_answers = self.get_channel(t_c_a)
        if self.trivia_channel_answers:
            output = []
            for iter in self.trivia_list.keys():
                if self.trivia_list[iter].answer is None:
                    output.append(self.trivia_list[iter].question)
            else:
                if output:
                    output_string = "\n".join(output)
                    print(f'Needs Answers: \n{output_string}')

    async def on_guild_join(self, guild):
        try:
            self.guild_list[guild.id].active = True
        except KeyError:
            self.guild_list.update({guild.id: Guild(guild_id=guild.id)})

    async def on_guild_remove(self, guild):
        try:
            self.guild_list[guild.id].active = False
        except KeyError:
            self.guild_list.update({guild.id: Guild(guild_id=guild.id, active=False)})

    async def on_message(self, message):
        if self.trivia_channel_answers is None:
            await self.process_commands(message)
        else:
            if message.author.id in t_b and message.channel.id in t_c and message.content != '':
                question_format_found = True
                for string in t_a_h:
                    if string in message.content:
                        question_format_found = False
                else:
                    if question_format_found:
                        await self.process_trivia_question(message=message)
                    else:
                        await self.process_commands(message)
            else:
                await self.process_commands(message)

    async def process_trivia_question(self, message):
        question = re.sub(r'^.*\.\.\.\*\* ', '', message.content)
        try:
            current = self.trivia_list[question].answer
            if current == '':
                await message.channel.send("Question Located But No Solution Found; Please Update.")
            if t_q_h in message.content:
                await asyncio.sleep(randrange(3))
                await message.channel.send(current)
            if await self.not_found_in_channel(question):
                await self.trivia_channel_answers.send(f'**{question}**\n```{current}```')
        except KeyError:
            self.trivia_list.update({question: Trivia(question=question)})
            await message.channel.send("Question Not Located. Inserted, But Needs Solution.")

    async def not_found_in_channel(self, test_message):
        async for message in self.trivia_channel_answers.history():
            if test_message in message.content:
                return False
        else:
            return True

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


bot = Bot()
bot.run(bot_token, reconnect=True)

"""
To do list:

Gambling:
Bet / Winning Modifier
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

Currency Exchanger:
Fix Key Error 'rates'

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
