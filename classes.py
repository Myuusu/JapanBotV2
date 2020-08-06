import random
import asyncio
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


class Machine:
    def __init__(self, name, cost, machine_type):
        self.machine = {
            "name": name,
            "cost": cost,
            "machine_type": machine_type
        }


class Emoji:
    def __init__(self, emoji, rank, weights):
        self.emoji = {
            "emoji": emoji,
            "rank": rank,
            "weights": weights
        }

    def __getitem__(self, item):
        return self.emoji[item]

    def __setitem__(self, key, value):
        self.emoji[key] = value

    def __str__(self):
        return self.__getitem__("emoji")

    def get_emoji(self):
        return self.__getitem__("emoji")

    def get_rank(self):
        return self.__getitem__("rank")

    def get_weights(self):
        return self.__getitem__("weights")


class SlotMachine:
    def __init__(self, name: str, cost: int, rows: int, reels: int, emojis: list[Emoji] | Emoji):
        self.machine = {
            "name": name,
            "cost": cost,
            "rows": rows,
            "reels": reels,
            "emojis": emojis,
            "play_count": 0,
            "winnings": 0,
            "profit": 0
        }

    def __getitem__(self, key):
        return self.machine[key]

    def __setitem__(self, key, value):
        self.machine[key] = value

    def get_name(self):
        return self.__getitem__("name")

    def get_cost(self):
        return self.__getitem__("cost")

    def get_rows(self):
        return self.__getitem__("rows")

    def get_reels(self):
        return self.__getitem__("reels")

    def get_play_count(self):
        return self.__getitem__("play_count")

    def get_winnings(self):
        return self.__getitem__("winnings")

    def get_profit(self):
        return self.__getitem__("profit")

    def get_emojis(self):
        return self.__getitem__("emojis")

    def set_winnings(self, value):
        return self.__setitem__(key="winnings", value=value)

    def increment_play_count(self):
        return self.__setitem__(key="play_count", value=self.__getitem__("play_count")+1)

    def set_profit(self, value):
        return self.__setitem__(key="profit", value=value)

    def print(self):
        return " | ".join(
            f'Cost: {self.__getitem__("cost")}',
            f'Emojis: {" ".join(self.__getitem__("emojis").get_emoji())}',
            f'Name: {self.__getitem__("name")}'
        )

    def calculate_winnings(self, ctx, spin_results, multiplier=1):
        print(spin_results)
        print(ctx.author)
        return self.__getitem__("cost") * multiplier

    def get_reel_weight(self):
        weights = []
        for i in self.__getitem__("emojis"):
            weights.append(i.get_weights())
        return weights

    async def spin(self, ctx, multiplier=1):
        """ This is where the machine will "spin" each of its wheels """
        spin_results = []
        for i in range(self.__getitem__("reels")):
            current_reel_weight = []
            for curr in self.get_reel_weight():
                current_reel_weight.append(curr.pop())
            spin_results.append(
                random.choices(
                    population=self.__getitem__("emojis"),
                    weights=current_reel_weight,
                    k=self.__getitem__("rows")
                )
            )
        else:
            emoji_matrix = [["?" for j in range(self.__getitem__("reels"))] for i in range(self.__getitem__("rows"))]
            ranks_matrix = [["#" for j in range(self.__getitem__("reels"))] for i in range(self.__getitem__("rows"))]
            msg = await ctx.send(f"Spinning! Good luck {ctx.author.name}!")
            for j in range(self.__getitem__("reels")):
                await asyncio.sleep(random.uniform(1, 4))
                for i in range(self.__getitem__("rows")):
                    ranks_matrix[i][j] = spin_results[j][i].get_rank()
                    emoji_matrix[i][j] = spin_results[j][i].get_emoji()
                output = '\n'.join(['|'.join([str(item) for item in row]) for row in emoji_matrix])
                await msg.edit(content=f"Spinning! Good luck {ctx.author.name}!\n{output}")
            else:
                return self.calculate_winnings(ctx, ranks_matrix, multiplier)


class Poker:
    def __init__(self, machine, cost):
        self.machine = machine
        self.cost = cost
        self.deck = Deck()


class Account:
    def __init__(self, user_id, balance):
        self.account = {
            "user_id": user_id,
            "balance": balance
        }

    def __getitem__(self, key):
        return self.account[key]

    def __setitem__(self, key, value):
        self.account[key] = value

    def get_balance(self):
        return self.__getitem__("balance")

    def get_user_id(self):
        return self.__getitem__("user_id")

    def set_balance(self, balance):
        self.__setitem__("balance", balance)


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
