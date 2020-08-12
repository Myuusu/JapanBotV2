import random
import json
import asyncio
from selenium.common.exceptions import NoSuchElementException
from storage.winnings_table import \
    three_by_three_lines, three_by_one_lines, three_reel_winnings, \
    five_by_one_lines, five_by_three_lines, five_reel_winnings
from commands.utility import resolve_line


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self):
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.contents = [Card(rank, suit) for rank in ranks for suit in suits]


class Emoji:
    def __init__(self, emoji, rank, weights):
        self.emoji = emoji
        self.rank = rank
        self.weights = weights

    def get_json(self):
        weights = json.dumps(self.weights)
        return f"            Emoji(emoji=u'{self.emoji}', rank={self.rank}, weights={weights})"


class Machine:
    def __init__(self, name, cost, machine_type):
        self.name = name
        self.cost = cost
        self.machine_type = machine_type


class SlotMachine:
    def __init__(self, name: str, cost: int, rows: int, reels: int, emojis: [Emoji],
                 machine_type: str = "slot", play_count=0, winnings=0, profit=0
                 ):
        self.name = name
        self.cost = cost
        self.machine_type = machine_type
        self.rows = rows
        self.reels = reels
        self.emojis = emojis
        self.play_count = play_count
        self.winnings = winnings
        self.profit = profit

    def print(self):
        return f'Cost: {self.cost} | Emojis: {" ".join([self.emojis.emoji])} | Name: {self.name}'

    def calculate_winnings(self, ranks_matrix: [[]], multiplier=1):
        winnings = 0
        if self.reels == 3:
            if self.rows == 1:
                for line in three_by_one_lines:
                    winnings = winnings + int(resolve_line(ranks_matrix, line, three_reel_winnings))
            if self.rows == 3:
                for line in three_by_three_lines:
                    winnings = winnings + int(resolve_line(ranks_matrix, line, three_reel_winnings))
        if self.reels == 5:
            if self.rows == 1:
                for line in five_by_one_lines:
                    winnings = winnings + int(resolve_line(ranks_matrix, line, five_reel_winnings))
            if self.rows == 3:
                for line in five_by_three_lines:
                    winnings = winnings + int(resolve_line(ranks_matrix, line, five_reel_winnings))
        self.winnings += multiplier * winnings
        self.profit += multiplier * (self.cost - winnings)
        self.play_count += 1
        return multiplier * winnings

    def get_reel_weight(self, reel_position: int):
        weights_from_each_emoji = []
        for current_emoji in self.emojis:
            weights_from_each_emoji.append(current_emoji.weights[reel_position])
        return weights_from_each_emoji

    async def spin(self, ctx, multiplier: int = 1):
        """ This is where the machine will "spin" each of its wheels """
        spin_results = []
        for i in range(self.reels):
            spin_results.append(
                random.choices(
                    population=self.emojis,
                    weights=self.get_reel_weight(i),
                    k=self.rows
                )
            )
        else:
            emoji_matrix = [["?" for _ in range(self.reels)] for _ in range(self.rows)]
            ranks_matrix = [["#" for _ in range(self.reels)] for _ in range(self.rows)]
            msg = await ctx.send(f"Spinning! Good luck {ctx.author.name}!")
            for j in range(self.reels):
                await asyncio.sleep(random.uniform(1, 4))
                for i in range(self.rows):
                    ranks_matrix[i][j] = spin_results[j][i].rank
                    emoji_matrix[i][j] = spin_results[j][i].emoji
                output = '\n'.join(['|'.join([str(item) for item in row]) for row in emoji_matrix])
                await msg.edit(content=f"Spinning! Good luck {ctx.author.name}!\n{output}")
            else:
                output = self.calculate_winnings(ranks_matrix, multiplier)
                if output > (self.cost * multiplier * 3.5):
                    msg = await ctx.send(f'*HUGE WINNER!!* {str(output)}')
                    for i in range(10):
                        await asyncio.sleep(1)
                        await msg.edit(content=f'***HUGE WINNER!!*** {str(output)}')
                        await asyncio.sleep(.5)
                        await msg.edit(content=f'*HUGE WINNER!!* {str(output)}')
                elif output > (self.cost * multiplier):
                    await ctx.send(f'*Winner!* {str(output)}')
                else:
                    await ctx.send(f"Don't Give Up, Try Again! {str(output)}")
                return output

    def get_json(self):
        emoji_output = []
        for emoji in self.emojis:
            emoji_output.append(emoji.get_json())
        emoji_output = ",\n".join(emoji_output)
        return f'"{self.name}": SlotMachine(' \
               f'\n        name="{self.name}",' \
               f'\n        cost={self.cost},' \
               f'\n        rows={self.rows},' \
               f'\n        reels={self.reels},' \
               f'\n        machine_type="slot",' \
               f'\n        play_count={self.play_count},' \
               f'\n        winnings={self.winnings},' \
               f'\n        profit={self.profit}, ' \
               f'\n        emojis=[' \
               f'\n{emoji_output}' \
               f'\n        ]' \
               f'\n    )'


class Poker:
    def __init__(self, name, cost, machine_type="poker"):
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.name = name
        self.cost = cost
        self.type = machine_type
        self.deck = [Card(rank, suit) for rank in ranks for suit in suits]


class Account:
    def __init__(self, user_id, balance, jackpot_winner=False):
        self.user_id = user_id
        self.balance = balance
        self.jackpot_winner = jackpot_winner

    def get_json(self):
        return f'{self.user_id}: Account(' \
               f'\n\t\tuser_id={self.user_id},' \
               f'\n\t\tbalance={self.balance},' \
               f'\n\t\tjackpot_winner={self.jackpot_winner}' \
               f'\n\t)'


class Level:
    def __init__(self, level, exp):
        self.level = level,
        self.exp = exp


class Station:
    def __init__(self, station_id, name, url):
        self.station_id = station_id
        self.name = name
        self.url = url


class WebTable:
    def __init__(self, web_table):
        self.table = {
            "table": web_table,
            "rows": len(web_table.find_elements_by_xpath("tr")) - 1,
            "columns": len(web_table.find_elements_by_xpath("//tr[2]/td"))
        }

    def __getitem__(self, item):
        return self.table[item]

    def get_row_count(self):
        return len(self.table["table"].find_elements_by_tag_name("tr")) - 1

    def get_column_count(self):
        return len(self.table["table"].find_elements_by_xpath("//tr[2]/td"))

    def get_table_size(self):
        return {"rows": self.get_row_count(), "columns": self.get_column_count()}

    def row_data(self, row_number):
        if row_number == 0:
            raise Exception("Row number starts from 1")
        r_data = []
        for webElement in self.table["table"].find_elements_by_xpath(f'//tr[{str(row_number + 1)}]/td'):
            r_data.append(webElement.text)
        return r_data

    def column_data(self, column_number):
        r_data = []
        for webElement in self.table["table"].find_elements_by_xpath(f'//tr/td[{str(column_number)}]'):
            r_data.append(webElement.text)
        return r_data

    def get_all_data(self, max_rows=None):
        if max_rows:
            num_rows = len(self.table["table"].find_elements_by_xpath("//tr")) - 1
            if max_rows < num_rows:
                num_rows = max_rows
        else:
            num_rows = len(self.table["table"].find_elements_by_xpath("//tr")) - 1
        header = ["Form", "Plain", "Polite"]
        all_data = [" | ".join(header)]
        for i in range(2, num_rows):
            ro = ["**(" + self.table["table"].find_element_by_xpath(f'//tr[{str(i)}]/th').text + ")**"]
            for j in range(1, len(self.table["table"].find_elements_by_xpath(f'//tr[{str(i)}]/td')) - 1):
                try:
                    ro.append(
                        self.table["table"].find_element_by_xpath(
                            f'//tr[{str(i)}]/td[{str(j)}]'
                        ).text
                    )
                except NoSuchElementException:
                    pass
            all_data.append(" | ".join(ro))
        return all_data

    def presence_of_data(self, data):
        return len(self.table["table"].find_elements_by_xpath(f'//td[normalize-space(text())="{data}"]')) > 0

    def get_cell_data(self, row_number, column_number):
        if row_number == 0:
            raise Exception("Row number starts from 1")
        return self.table["table"].find_element_by_xpath(f'//tr[{str(row_number + 1)}]/td[{str(column_number)}]').text


class Guild:
    def __init__(self, guild_id, prefix, message_count=0, active=True, log_channel_id=None):
        self.guild_id = guild_id
        self.prefix = prefix
        self.message_count = message_count
        self.active = active
        self.log_channel_id = log_channel_id

    def get_json(self):
        return f'{self.guild_id}: Guild(guild_id={self.guild_id}, prefix="{self.prefix}", ' \
               f'message_count={self.message_count}, active={self.active}, log_channel_id={self.log_channel_id}'
