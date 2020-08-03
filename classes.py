import random
import asyncio
from selenium.common.exceptions import NoSuchElementException


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.contents = [Card(rank, suit) for rank in ranks for suit in suits]


class Machine:
    def __init__(self, name, emojis, cost, machine_type):
        self.machine = {
            "name": name,
            "emojis": emojis,
            "cost": cost,
            "machine_type": machine_type
        }

    def __getitem__(self, key):
        return self.machine[key]

    def __setitem__(self, key, value):
        self.machine[key] = value

    def get_name(self):
        return self.__getitem__("name")

    def get_emojis(self):
        return self.__getitem__("emojis")

    def get_cost(self):
        return self.__getitem__("cost")

    def get_machine_type(self):
        return self.__getitem__("machine_type")

    def print(self):
        return f'Cost: {self.__getitem__("cost")} | ' \
               f'Name: {self.__getitem__("name")} | ' \
               f'Emojis: {self.__getitem__("emojis")}'

    def calculate_winnings(self, winnings_multiplier):
        return self.get_cost() * winnings_multiplier

    async def spin(self, ctx):
        a = random.choice(self.__getitem__("emojis"))
        b = random.choice(self.__getitem__("emojis"))
        c = random.choice(self.__getitem__("emojis"))

        msg = await ctx.send(f"**[ ? ? ? ] Spinning! Good luck!\n{ctx.author.name}**")
        await asyncio.sleep(3)
        await msg.edit(content=f"**[ {a} ? ? ]\n{ctx.author.name}**")
        await asyncio.sleep(1)
        await msg.edit(content=f"**[ {a} {b} ? ]\n{ctx.author.name}**")
        await asyncio.sleep(2.5)
        await msg.edit(content=f"**[ {a} {b} ? ]\n{ctx.author.name}**")
        if a == b == c:
            outcome = self.calculate_winnings(3)
            await msg.edit(
                content=f"**[{a} {b} {c}]**\n"
                        f"{ctx.author.name} All matching, you won {outcome}! 🎉"
            )
        elif a == b or a == c or b == c:
            outcome = self.calculate_winnings(1)
            await msg.edit(
                content=f"**[{a} {b} {c}]**\n"
                        f"{ctx.author.name} 2 in a row, you won {outcome}! 🎉")
        else:
            outcome = self.calculate_winnings(-1)
            await msg.edit(
                content=f"**[{a} {b} {c}]**\n"
                        f"{ctx.author.name} No match, you lost {-outcome}! 😢")
        return outcome


class SlotMachine:
    def __init__(self, machine, type, cost, emojis):
        self.machine = machine
        self.type = type
        self.cost = cost
        self.emojis = emojis


class Poker:
    def __init__(self, machine, type, cost, deck: Deck):
        __super__().__init__(machine, type, cost)
        self.machine = machine
        self.type = type
        self.cost = cost
        self.deck = deck


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
        return self.__getitem__("station")

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
        row_number = row_number + 1
        row = self.table["table"].find_elements_by_xpath(f'//tr[{str(row_number)}]/td')
        r_data = []
        for webElement in row:
            r_data.append(webElement.text)
        return r_data

    def column_data(self, column_number):
        col = self.table["table"].find_elements_by_xpath(f'//tr/td[{str(column_number)}]')
        r_data = []
        for webElement in col:
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
        data_size = len(self.table["table"].find_elements_by_xpath(f'//td[normalize-space(text())="{data}"]'))
        presence = False
        if data_size > 0:
            presence = True
        return presence

    def get_cell_data(self, row_number, column_number):
        if row_number == 0:
            raise Exception("Row number starts from 1")
        row_number = row_number + 1
        cell_data = self.table["table"].find_element_by_xpath(f'//tr[{str(row_number)}]/td[{str(column_number)}]').text
        return cell_data
