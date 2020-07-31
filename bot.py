import discord
import os
from discord.ext import commands
from config import bot_token, bot_prefix
from storage import account_list, eight_ball_responses, level_list, slot_machines, station_list


class Bot(commands.Bot):

    def __init__(self):
        super(Bot, self).__init__(
            command_prefix=bot_prefix,
            case_insensitive=True
        )
        self.slot_machines = slot_machines
        self.level_list = level_list
        self.account_list = account_list
        self.eight_ball_responses = eight_ball_responses
        self.station_list = station_list

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
