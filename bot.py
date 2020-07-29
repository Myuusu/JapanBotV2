import discord
import os
from discord.ext import commands
from config import bot_token


class Bot(commands.Bot):
    def __init__(self):
        super(Bot, self).__init__(
            command_prefix=["!", "'", "73"],
            case_insensitive=True
        )

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
