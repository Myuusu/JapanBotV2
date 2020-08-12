import discord
import os
from discord.ext import commands
from config import bot_token
from storage.account_list import account_list
from storage.eight_ball_responses import eight_ball_responses
from storage.level_list import level_list
from storage.slot_machines import slot_machines
from storage.station_list import station_list
from storage.guild_list import guild_list
from classes import Guild


class Bot(commands.Bot):
    def __init__(self):
        super(Bot, self).__init__(case_insensitive=True, command_prefix=self.get_prefix)

        self.account_list = account_list
        self.guild_list = guild_list
        self.level_list = level_list
        self.eight_ball_responses = eight_ball_responses
        self.slot_machines = slot_machines
        self.station_list = station_list

        for filename in os.listdir('./commands'):
            if filename.endswith('.py'):
                self.load_extension(f'commands.{filename[:-3]}')

    async def update_guild_list(self):
        output = []
        for guild_id in self.guild_list.keys():
            output.append(self.guild_list[guild_id].get_json())
        else:
            output_string = ",\n    ".join(output)
            with open('storage/guild_list.py', mode='w+', encoding="ascii", errors="backslashreplace") as fp:
                fp.write(f'from classes import Guild\n\nguild_list = {{\n    {output_string}\n}}')

    async def update_account_list(self):
        output = []
        for account_id in self.account_list.keys():
            output.append(self.account_list[account_id].get_json())
        else:
            output_string = ",\n    ".join(output)
            with open('storage/account_list.py', mode='w+', encoding="ascii", errors="backslashreplace") as fp:
                fp.write(f'from classes import Account\n\naccount_list = {{\n    {output_string}\n}}')

    async def update_slot_machines(self):
        output = []
        for slot_machine_name in self.slot_machines.keys():
            output.append(self.slot_machines[slot_machine_name].get_json())
        else:
            output_string = ",\n    ".join(output)
            with open('storage/slot_machines.py', mode='w+', encoding="ascii", errors="backslashreplace") as fp:
                fp.write(f'from classes import SlotMachine, Emoji\n\nslot_machines = {{\n    {output_string}\n}}')

    async def on_ready(self):
        await self.change_presence(
            status=discord.Status.dnd,
            activity=discord.Activity(type=discord.ActivityType.listening, name='[!s]')
        )
#        embed = discord.Embed(
#            title=f"{self.user.name} Online!",
#            color=discord.Color.from_rgb(0, 0, 0),
#            timestamp=datetime.datetime.now(datetime.timezone.utc)
#        )
#        embed.set_footer(
#            text="Why am I still doing this",
#            icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Flag_of_Japan.svg/120px-Flag_of_Japan.svg.png"
#        )
#        log_channel_id = 730995381177024532
#        await self.get_channel(log_channel_id).send(embed=embed, delete_after=10)
        print(f'Logged in as {self.user.name} | {self.user.id}')

    async def on_guild_join(self, guild):
        self.guild_list.update(
            {
                guild["guild_id"]:
                    Guild(
                        guild["guild_id"],
                        "!",
                        guild["message_count"],
                        True,
                        guild["log_channel_id"]
                    )
            }
        )
        print(f'Reconnected To: {str(guild.id)}')
        await self.update_guild_list()

    async def on_guild_remove(self, guild):
        self.guild_list.update(
            {
                guild["guild_id"]:
                    Guild(
                        guild["guild_id"],
                        guild["prefix"],
                        guild["message_count"],
                        False,
                        guild["log_channel_id"]
                    )
            }
        )
        print(f'Disconnected From: {str(guild.id)}')
        await self.update_guild_list()

    async def on_command_error(self, ctx, exception):
        print(f'Context: {ctx} | Exception: {exception}')

    async def get_prefix(self, message):
        try:
            if self.guild_list[message.guild.id]:
                self.guild_list[message.guild.id].message_count += 1
                await self.update_guild_list()
                return self.guild_list[message.guild.id].prefix
        except KeyError:
            self.guild_list.update(
                {
                    message.guild.id: Guild(
                        guild_id=message.guild.id,
                        prefix="!",
                        message_count=0,
                        active=True,
                        log_channel_id=None
                    )
                }
            )
            await self.update_guild_list()
            return self.guild_list[message.guild.id].prefix


bot = Bot()
bot.run(bot_token, reconnect=True)


"""
To do list:

Gambling:
Bet / Winning Modifier
Add a message everytime you win or lose
Weighting modifications
Jackpot announcements on Animal slot for lion
Server admin right to toggle "Jackpot Winner" role
Configure daily point dispenser

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
