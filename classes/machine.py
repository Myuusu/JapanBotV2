import random
import asyncio


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
        __super__().__init__(machine, type, cost)
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
