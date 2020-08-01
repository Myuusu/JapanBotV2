import discord
import os
from discord.ext import commands
from config import bot_token, bot_prefix
from storage.account_list import account_list
from storage.eight_ball_responses import responses
from storage.level_list import level_list
from storage.slot_machines import slot_machines
from storage.station_list import station_list
from classes import *


class Bot(commands.Bot):

    def __init__(self):
        super(Bot, self).__init__(
            command_prefix=bot_prefix,
            case_insensitive=True
        )
        self.account_list = account_list
        self.eight_ball_responses = responses
        self.level_list = level_list
        self.slot_machines = slot_machines
        self.station_list = station_list

        for filename in os.listdir('./commands'):
            if filename.endswith('.py'):
                self.load_extension(f'commands.{filename[:-3]}')

    async def lookup_user_balance(self, user: discord.User):
        for current_user in self.account_list:
            if user.id == current_user["user_id"]:
                return current_user["balance"]
        return None

    async def lookup_machine_cost(self, machine_name: str):
        for machine in self.slot_machines:
            if machine_name == machine["name"]:
                return machine["cost"]
        return None

    async def on_ready(self):
        await self.change_presence(
            status=discord.Status.online,
            activity=discord.Game(
                'streams of your favorite stations! [!s]'
            )
        )
        print(f'Logged in as {self.user.name} | {self.user.id}')

    async def on_command_error(self, ctx, exception):
        print(f'Context: {ctx} | Exception: {exception}')


bot = Bot()
bot.run(bot_token)
