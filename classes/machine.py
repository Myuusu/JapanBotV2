import random


async def roll(max: str = 1):
    return random(max)


class Machine:
    def __init__(self, machine, type, cost):
        self.machine = machine
        self.type = type
        self.cost = cost


class SlotMachine:
    def __init__(self, machine, type, cost, emojis):
        __super__().__init__(machine, type, cost)
        self.machine = machine
        self.type = type
        self.cost = cost
        self.emojis = emojis


