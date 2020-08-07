import asyncio
import random
from selenium.common.exceptions import NoSuchElementException


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


class Machine:
    def __init__(self, name, cost, machine_type):
        self.name = name
        self.cost = cost
        self.machine_type = machine_type
        self.play_count = 0
        self.winnings = 0
        self.profit = 0


class SlotMachine:
    def __init__(self, name: str, cost: int, rows: int, reels: int, machine_type: str, emojis: [Emoji]):
        self.name = name
        self.cost = cost
        self.machine_type = machine_type
        self.rows = rows
        self.reels = reels
        self.emojis = emojis

    def print(self):
        return f'Cost: {self.cost} | Emojis: {" ".join([self.emojis.emoji])} | Name: {self.name}'

    def calculate_winnings(self, ctx, spin_results, multiplier=1):
        print(spin_results)
        print(ctx.author)
        return self.cost * multiplier

    def get_reel_weight(self):
        weights = []
        for i in self.emojis:
            weights.append(i.weights)
        return weights

    async def spin(self, ctx, multiplier=1):
        """ This is where the machine will "spin" each of its wheels """
        spin_results = []
        for _ in range(self.reels):
            current_reel_weight = []
            for curr in self.get_reel_weight():
                current_reel_weight.append(curr.pop())
            spin_results.append(
                random.choices(
                    population=self.emojis,
                    weights=current_reel_weight,
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
                return self.calculate_winnings(ctx, ranks_matrix, multiplier)


class Poker:
    def __init__(self, name, cost, machine_type="poker"):
        self.name = name
        self.cost = cost
        self.type = machine_type
        self.deck = Deck()


class Account:
    def __init__(self, user_id, balance):
        self.user_id = user_id
        self.balance = balance


class Level:
    def __init__(self, level, exp):
        self.level = {
            "level": level,
            "exp": exp
        }

    def __getitem__(self, key):
        return self.level[key]

    def __setitem__(self, key, value):
        return

    def get_exp(self):
        return self.__getitem__("exp")


class Station:
    def __init__(self, station_id, name, url):
        self.station = {
            "station_id": station_id,
            "name": name,
            "url": url
        }

    def __getitem__(self, item):
        return self.station[item]

    def get_station_id(self):
        return self.__getitem__("station_id")

    def get_name(self):
        return self.__getitem__("name")

    def get_url(self):
        return self.__getitem__("url")


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
