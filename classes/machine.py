import random


async def roll(max: str = 1):
    return random(max)


class Machine:
    def __init__(self, machine):
        self.machine = machine
        self.type = None
