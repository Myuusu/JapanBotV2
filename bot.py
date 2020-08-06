import discord
import os
from classes import SlotMachine, Account, Level, Station, Emoji
from config import bot_token, bot_prefix
from discord.ext import commands
from storage.account_list import account_list
from storage.eight_ball_responses import responses
from storage.level_list import level_list
from storage.level_list import level_list
from storage.slot_machines import slot_machines
from storage.station_list import station_list
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
            emoji_array = []
            for emoji in machine["emojis"]:
                emoji_array.append(
                    Emoji(emoji["emoji"], emoji["rank"], emoji["weights"])
                )
            self.slot_machines.append(
                SlotMachine(machine["name"], machine["cost"], machine["rows"], machine["reels"], emoji_array)
            )

        self.level_list = []
        for level in level_list:
            self.level_list.append(
                Level(level["level"], level["exp"])
            )

        self.eight_ball_responses = responses
        self.station_list = []
        for station in station_list:
            self.station_list.append(
                Station(station["station_id"], station["name"], station["url"])
            )

        for filename in os.listdir('./commands'):
            if filename.endswith('.py'):
                self.load_extension(f'commands.{filename[:-3]}')

    async def on_ready(self):
        await self.change_presence(
            status=discord.Status.online,
            activity=discord.Game('streams of your favorite stations! [!s]')
        )
        print(f'Logged in as {self.user.name} | {self.user.id}')


async def on_command_error(ctx, exception):
    print(f'Context: {ctx} | Exception: {exception}')


bot = Bot()
bot.run(bot_token)

"""
To do list:
Gambling:
Bet / Winning Modifier
Weighting modifications
Jackpot announcements on Animal slot for lion
Server admin right to toggle "Jackpot Winner" role
Configure daily point dispenser
Add custom emotes to a server for the slots

Conjugation:
Fix elements, unable to locate currently
Fix Issue with overload of conjugations

Station:
Add a type and subtype for each station so that users can filter through genres

Jisho:
Fix encoding issue when use a space for ex. to go
Possibly look into changing from jisho to the website conjugation uses

Currencyexchanger:
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
