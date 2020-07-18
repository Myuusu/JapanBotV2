import discord
from discord.ext import commands
from config import bot_token
import os


class Bot(commands.Bot):

    def __init__(self):
        super(Bot, self).__init__(command_prefix="!")

        for filename in os.listdir('./commands'):
            if filename.endswith('.py'):
                self.load_extension(f'commands.{filename[:-3]}')

    async def on_ready(self):
        await self.change_presence(status=discord.Status.dnd, activity=discord.Game('coding'))
        print(f'Logged in as {self.user.name} | {self.user.id}')


bot = Bot()
bot.run(bot_token)
