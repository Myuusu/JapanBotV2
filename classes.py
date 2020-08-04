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
    def __init__(self, emoji, rank, weight):
        self.emoji = {
            "emoji": emoji,
            "rank": rank,
            "weight": weight
        }

    def __getitem__(self, item):
        return self.emoji[item]

    def get_emoji(self):
        return self.__getitem__("emoji")

    def get_rank(self):
        return self.__getitem__("rank")

    def get_weight(self):
        return self.__getitem__("weight")


class SlotMachine:
    def __init__(self, name, cost, emojis):
        self.machine = {
            "name": name,
            "cost": cost,
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

    def get_emoji_data(self):
        emojis = []
        weights = []
        ranks = []
        for i in self.__getitem__("emojis"):
            emojis.append(i.get_emoji())
            ranks.append(i.get_rank())
            weights.append(i.get_weight())
        return emojis, ranks, weights

    def get_cost(self):
        return self.__getitem__("cost")

    def get_machine_type(self):
        return self.__getitem__("machine_type")

    def get_play_count(self):
        return self.__getitem__("play_count")

    def get_winnings(self):
        return self.__getitem__("winnings")

    def get_profit(self):
        return self.__getitem__("profit")

    def set_winnings(self, value):
        return self.__setitem__(key="winnings", value=value)

    def increment_play_count(self):
        return self.__setitem__(key="play_count", value=self.get_play_count()+1)

    def set_profit(self, value):
        return self.__setitem__(key="profit", value=value)

    def print(self):
        return f'Cost: {self.__getitem__("cost")} | ' \
               f'Name: {self.__getitem__("name")} | ' \
               f'Emojis: {self.__getitem__("emojis")}'

    def calculate_winnings(self, ctx, machine_output, winnings_multiplier):
        return self.__getitem__("cost") * winnings_multiplier

    async def spin(self, ctx, multiplier=1):
        """ This is where the machine will "spin" each of its wheels """
        emojis, ranks, weights = self.get_emoji_data()

        res = random.choices(
                population=emojis,
                weights=weights,
                cum_weights=None,
                k=9
            )

        msg = await ctx.send(
            f"Spinning! Good luck {ctx.author.name}!\n"
            f"|?|?|?|\n"
            f"|?|?|?|\n"
            f"|?|?|?|"
        )
        await asyncio.sleep(random.uniform(1, 4))
        await msg.edit(content=
                       f"Spinning! Good luck {ctx.author.name}!\n"
                       f"|{res[0]}|?|?|\n"
                       f"|{res[3]}|?|?|\n"
                       f"|{res[6]}|?|?|"
                       )
        await asyncio.sleep(random.uniform(2, 5))
        await msg.edit(content=
                       f"Spinning! Good luck {ctx.author.name}!\n"
                       f"|{res[0]}|{res[1]}|?|\n"
                       f"|{res[3]}|{res[4]}|?|\n"
                       f"|{res[6]}|{res[7]}|?|"
                       )
        await asyncio.sleep(random.uniform(2, 7))
        await msg.edit(content=
                       f"Spinning! Good luck {ctx.author.name}!\n"
                       f"|{res[0]}|{res[1]}|{res[2]}|\n"
                       f"|{res[3]}|{res[4]}|{res[5]}|\n"
                       f"|{res[6]}|{res[7]}|{res[8]}|"
                       )
        self.increment_play_count()
        await ctx.send(f'This machine has been played: {self.get_play_count()} times!')
        return self.calculate_winnings(ctx, res, multiplier)


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
        presence = False
        if len(self.table["table"].find_elements_by_xpath(f'//td[normalize-space(text())="{data}"]')) > 0:
            presence = True
        return presence

    def get_cell_data(self, row_number, column_number):
        if row_number == 0:
            raise Exception("Row number starts from 1")
        return self.table["table"].find_element_by_xpath(f'//tr[{str(row_number + 1)}]/td[{str(column_number)}]').text
