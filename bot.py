import discord
import os
from discord.ext import commands
from config import bot_token, bot_prefix
from storage.account_list import account_list
from storage.eight_ball_responses import responses
from storage.level_list import level_list
from storage.slot_machines import slot_machines
from classes.machine import Machine
from classes.account import Account
from classes.level import Level
from classes.station import Station
from storage.station_list import station_list


class Bot(commands.Bot):

    def __init__(self):
        super(Bot, self).__init__(
            command_prefix=bot_prefix,
            case_insensitive=True
        )

        self.account_list = []
        for account in account_list:
            self.account_list.append(
                Account(account["user_id"], account["balance"])
            )

        self.slot_machines = []
        for machine in slot_machines:
            self.slot_machines.append(
                Machine(machine["name"], machine["emojis"], machine["cost"], machine["machine_type"])
            )

        self.level_list = []
        for level in level_list:
            self.level_list.append(
                Level(level["level"], level["exp"])
            )

        self.eight_ball_responses = responses
        self.slot_machines = slot_machines
        self.station_list = []
        for station in station_list:
            self.station_list.append(Station(station["station_id"], station["name"], station["url"]))

        for filename in os.listdir('./commands'):
            if filename.endswith('.py'):
                self.load_extension(f'commands.{filename[:-3]}')

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
