import asyncio
import random

from discord import Embed

from storage.winnings_table import \
    three_by_three_lines, three_by_one_lines, three_reel_winnings, \
    five_by_one_lines, five_by_three_lines, five_reel_winnings


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Rank:
    def __init__(self, string, value):
        self.string = string
        self.value = value

    def __str__(self):
        return self.string


class Deck:
    def __init__(self):
        ranks = [
            Rank("Ace", 1),
            Rank("2", 2),
            Rank("3", 3),
            Rank("4", 4),
            Rank("5", 5),
            Rank("6", 6),
            Rank("7", 7),
            Rank("8", 8),
            Rank("9", 9),
            Rank("10", 10),
            Rank("Jack", 11),
            Rank("Queen", 12),
            Rank("King", 13)
        ]
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.contents = [Card(rank, suit) for rank in ranks for suit in suits]


class Emoji:
    def __init__(self, emoji, rank, weights):
        self.emoji = emoji
        self.rank = rank
        self.weights = weights

    def get_json(self):
        return f"            Emoji(" \
               f"\n                emoji=u'{self.emoji}'," \
               f"\n                rank={self.rank}," \
               f"\n                weights={self.weights}" \
               f"\n            )"


class Machine:
    def __init__(self, name, cost, machine_type):
        self.name = name
        self.cost = cost
        self.machine_type = machine_type


class SlotMachine:
    def __init__(self, name: str, cost: int, rows: int, reels: int, emojis: [Emoji],
                 machine_type: str = "slot", jackpots=0, play_count=0, coins_out=0, coins_in=0
                 ):
        self.name = name
        self.cost = cost
        self.rows = rows
        self.reels = reels
        self.emojis = emojis
        self.machine_type = machine_type
        self.jackpots = jackpots
        self.play_count = play_count
        self.coins_out = coins_out
        self.coins_in = coins_in

    def print(self):
        return f'Cost: {self.cost} | Emojis: {" ".join([self.emojis.emoji])} | Name: {self.name}'

    async def resolve_line(self, ranks_matrix: [[]], line_coordinates: [[]], winnings_table: [[]]):
        output = ""
        for [row, reel] in line_coordinates:
            output += str(ranks_matrix[row][reel])
        else:
            try:
                line = int(output)
                if line == 0:
                    self.jackpots += 1
                return winnings_table[line]
            except KeyError:
                return 0

    async def calculate_winnings(self, ranks_matrix: [[]], multiplier=1):
        winnings = 0
        if self.reels == 3:
            if self.rows == 1:
                for line in three_by_one_lines:
                    winnings += await self.resolve_line(ranks_matrix, line, three_reel_winnings)
                else:
                    self.coins_out += multiplier * winnings
                    self.play_count += 1
                    self.coins_in += self.cost * multiplier
                    return multiplier * winnings
            if self.rows == 3:
                for line in three_by_three_lines:
                    winnings += await self.resolve_line(ranks_matrix, line, three_reel_winnings)
                else:
                    self.coins_out += multiplier * winnings
                    self.play_count += 1
                    self.coins_in += self.cost * multiplier
                    return multiplier * winnings
        if self.reels == 5:
            if self.rows == 1:
                for line in five_by_one_lines:
                    winnings += await self.resolve_line(ranks_matrix, line, five_reel_winnings)
                else:
                    self.coins_out += multiplier * winnings
                    self.play_count += 1
                    self.coins_in += self.cost * multiplier
                    return multiplier * winnings
            if self.rows == 3:
                for line in five_by_three_lines:
                    winnings += await self.resolve_line(ranks_matrix, line, five_reel_winnings)
                else:
                    self.coins_out += multiplier * winnings
                    self.play_count += 1
                    self.coins_in += self.cost * multiplier
                    return multiplier * winnings

    def get_reel_weight(self, reel_position: int):
        weights_from_each_emoji = []
        for current_emoji in self.emojis:
            weights_from_each_emoji.append(current_emoji.weights[reel_position])
        else:
            return weights_from_each_emoji

    async def spin(self, ctx, spins: int = 1, multiplier: int = 1, testing: str = "False"):
        results = 0
        for _ in range(spins):
            """ This is where the machine will "spin" each of its wheels """
            spin_results = []
            for i in range(self.reels):
                reel_result = random.choices(
                    population=self.emojis,
                    weights=self.get_reel_weight(i),
                    k=self.rows
                )
                spin_results.append(reel_result)
            else:
                if testing == "False":
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
                        current_jackpots = self.jackpots
                        output = await self.calculate_winnings(ranks_matrix, multiplier)
                        if self.jackpots > current_jackpots:
                            msg = await ctx.send(f'*JACKPOT WINNER!!* {str(output)}')
                            for _ in range(10):
                                await asyncio.sleep(1)
                                await msg.edit(content=f'***JACKPOT WINNER!!*** {str(output)}')
                                await asyncio.sleep(.5)
                                await msg.edit(content=f'*JACKPOT WINNER!!* {str(output)}')
                        elif output > (self.cost * multiplier):
                            await ctx.send(f'*Winner!* {str(output)}')
                        else:
                            await ctx.send(f"Don't Give Up, Try Again! {str(output)}")
                        results += output
                else:
                    ranks_matrix = [["#" for _ in range(self.reels)] for _ in range(self.rows)]
                    for reel in range(self.reels):
                        for row in range(self.rows):
                            ranks_matrix[row][reel] = spin_results[reel][row].rank
                    else:
                        results += await self.calculate_winnings(ranks_matrix, multiplier)
        else:
            return results

    async def reset(self):
        self.coins_out = 0
        self.coins_in = 0
        self.play_count = 0
        self.jackpots = 0

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
               f'\n        jackpots={self.jackpots},' \
               f'\n        play_count={self.play_count},' \
               f'\n        coins_out={self.coins_out},' \
               f'\n        coins_in={self.coins_in},' \
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


class LolAccount:
    def __init__(self, user_id, p_user_id, account_id, game_name, tag_line="NA1"):
        self.user_id = user_id
        self.p_user_id = p_user_id
        self.account_id = account_id
        self.game_name = game_name
        self.tag_line = tag_line

    def get_json(self):
        return f'\n            {self.user_id}: LolAccount(' \
               f'\n                user_id={self.user_id},' \
               f'\n                p_user_id={self.p_user_id},' \
               f'\n                account_id={self.account_id},' \
               f'\n                game_name={self.game_name},' \
               f'\n                tag_line={self.tag_line}' \
               f'\n            )'


class Account:
    def __init__(self, user_id: int, lol_account_id: str = "abc123", balance: int = 1000, jackpot_winner=False):
        self.user_id = user_id
        self.lol_account_id = lol_account_id
        self.balance = balance
        self.jackpot_winner = jackpot_winner

    def get_json(self):
        return f'{self.user_id}: Account(' \
               f'\n        user_id={self.user_id},' \
               f'\n        lol_account_id="{self.lol_account_id}",' \
               f'\n        balance={self.balance},' \
               f'\n        jackpot_winner={self.jackpot_winner}' \
               f'\n    )'


class Level:
    def __init__(self, level, exp):
        self.level = level
        self.exp = exp


class Station:
    def __init__(self, station_id, name, url):
        self.station_id = station_id
        self.name = name
        self.url = url


class Guild:
    def __init__(self, guild_id, prefix=None, message_count=0, active=True, log_channel_id=None):
        self.guild_id = guild_id
        if prefix is None:
            self.prefix = ["!"]
        else:
            self.prefix = prefix
        self.message_count = message_count
        self.active = active
        self.log_channel_id = log_channel_id

    def get_json(self):
        return f'{self.guild_id}: Guild(' \
               f'\n        guild_id={self.guild_id},' \
               f'\n        prefix={self.prefix},' \
               f'\n        message_count={self.message_count},' \
               f'\n        active={self.active},' \
               f'\n        log_channel_id={self.log_channel_id}' \
               f'\n    )'


class Timer:
    def __init__(self, end_time, user_id, name):
        self.end_time = end_time
        self.user_id = user_id
        self.name = name

    def get_json(self):
        return f'"{self.user_id | self.name}": Timer(' \
               f'\n        end_time="{self.end_time}",' \
               f'\n        user_id={self.user_id},' \
               f'\n        name="{self.name}"' \
               f'\n    )'


class Skill:
    def __init__(
            self,
            name,
            stat=0
    ):
        self.name = name
        self.stat = stat


class Attributes:
    def __init__(
            self,
            strength: int = 10,
            dexterity: int = 10,
            constitution: int = 10,
            intelligence: int = 10,
            wisdom: int = 10,
            charisma: int = 10
    ):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

        self.strength_mod = (strength - 10) // 2
        self.dexterity_mod = (dexterity - 10) // 2
        self.constitution_mod = (constitution - 10) // 2
        self.intelligence_mod = (intelligence - 10) // 2
        self.wisdom_mod = (wisdom - 10) // 2
        self.charisma_mod = (charisma - 10) // 2

    async def output(self):
        return f"Strength: {self.strength}\n" \
               f"Dexterity: {self.dexterity}\n" \
               f"Constitution: {self.constitution}\n" \
               f"Intelligence: {self.intelligence}\n" \
               f"Wisdom: {self.wisdom}\n" \
               f"Charisma: {self.charisma}"


class Class:
    def __init__(
            self,
            name,
            desc=None,
            hit_dice=None,
            prof_armor=None,
            prof_weapons=None,
            prof_tools=None,
            prof_saving_throws=None,
            prof_skills=None,
            equipment=None,
            table=None,
            spellcasting_ability=None,
            subtypes_name=None,
            archetypes=None
    ):
        self.name = name
        self.desc = desc
        self.hit_dice = hit_dice
        self.prof_armor = prof_armor
        self.prof_weapons = prof_weapons
        self.prof_tools = prof_tools
        self.prof_saving_throws = prof_saving_throws
        self.prof_skills = prof_skills
        self.equipment = equipment
        self.table = table
        self.spellcasting_ability = spellcasting_ability
        self.subtypes_name = subtypes_name
        self.archetypes = archetypes


class Character:
    def __init__(
            self,
            user_id,
            char_name=None,
            class_type=None,
            level=1,
            background=None,
            alignment=None,
            race=None,
            exp=0,
            proficiencies=None,
            attributes=None
    ):

        self.user_id = user_id
        self.char_name = char_name
        self.class_type = class_type if isinstance(class_type, Class) else Class(class_type)
        self.level = level
        self.background = background
        self.alignment = alignment
        self.race = race
        self.exp = exp
        self.proficiency_bonus = (self.level - 1) // 4 + 2
        self.proficiencies = proficiencies
        self.attributes = attributes if isinstance(attributes, Attributes) else Attributes()

        self.skills = {
            "athletics": Skill("athletics", self.attributes.strength_mod),
            "acrobatics": Skill("acrobatics", self.attributes.dexterity_mod),
            "sleight of hand": Skill("sleight of hand", self.attributes.dexterity_mod),
            "stealth": Skill("stealth", self.attributes.dexterity_mod),
            "arcana": Skill("arcana", self.attributes.intelligence_mod),
            "history": Skill("history", self.attributes.intelligence_mod),
            "investigation": Skill("investigation", self.attributes.intelligence_mod),
            "nature": Skill("nature", self.attributes.intelligence_mod),
            "religion": Skill("religion", self.attributes.intelligence_mod),
            "animal handling": Skill("animal handling", self.attributes.wisdom_mod),
            "insight": Skill("insight", self.attributes.wisdom_mod),
            "medicine": Skill("medicine", self.attributes.wisdom_mod),
            "perception": Skill("perception", self.attributes.wisdom_mod),
            "survival": Skill("survival", self.attributes.wisdom_mod),
            "deception": Skill("deception", self.attributes.charisma_mod),
            "intimidation": Skill("intimidation", self.attributes.charisma_mod),
            "performance": Skill("performance", self.attributes.charisma_mod),
            "persuasion": Skill("persuasion", self.attributes.charisma_mod)
        }
        for i in self.proficiencies:
            self.skills[i].stat += self.proficiency_bonus

    async def output(self, ctx):
        await ctx.send(
            embed=Embed(
                title=f"Name: {self.char_name}",
                description=f"Level {self.level} {self.race} {self.class_type.name}\n"
                            f"Background: {self.background} | Exp {self.exp}\n"
                            f"Attributes:\n{await self.attributes.output()}\n"
                            f"Proficiencies: {','.join(self.proficiencies)}"
            )
        )

    async def reload_skills(self):
        self.skills = {
            "athletics": Skill("athletics", self.attributes.strength_mod),
            "acrobatics": Skill("acrobatics", self.attributes.dexterity_mod),
            "sleight of hand": Skill("sleight of hand", self.attributes.dexterity_mod),
            "stealth": Skill("stealth", self.attributes.dexterity_mod),
            "arcana": Skill("arcana", self.attributes.intelligence_mod),
            "history": Skill("history", self.attributes.intelligence_mod),
            "investigation": Skill("investigation", self.attributes.intelligence_mod),
            "nature": Skill("nature", self.attributes.intelligence_mod),
            "religion": Skill("religion", self.attributes.intelligence_mod),
            "animal handling": Skill("animal handling", self.attributes.wisdom_mod),
            "insight": Skill("insight", self.attributes.wisdom_mod),
            "medicine": Skill("medicine", self.attributes.wisdom_mod),
            "perception": Skill("perception", self.attributes.wisdom_mod),
            "survival": Skill("survival", self.attributes.wisdom_mod),
            "deception": Skill("deception", self.attributes.charisma_mod),
            "intimidation": Skill("intimidation", self.attributes.charisma_mod),
            "performance": Skill("performance", self.attributes.charisma_mod),
            "persuasion": Skill("persuasion", self.attributes.charisma_mod)
        }
        for i in self.proficiencies:
            self.skills[i].stat += self.proficiency_bonus

    async def set_attribute(self, attribute, level):
        if attribute == "strength":
            self.attributes.strength = level
            self.attributes.strength_mod = (level - 10) // 2
        elif attribute == "dexterity":
            self.attributes.dexterity = level
            self.attributes.dexterity_mod = (level - 10) // 2
        elif attribute == "constitution":
            self.attributes.constitution = level
            self.attributes.constitution_mod = (level - 10) // 2
        elif attribute == "intelligence":
            self.attributes.intelligence = level
            self.attributes.intelligence_mod = (level - 10) // 2
        elif attribute == "wisdom":
            self.attributes.wisdom = level
            self.attributes.wisdom_mod = (level - 10) // 2
        elif attribute == "charisma":
            self.attributes.charisma = level
            self.attributes.charisma_mod = (level - 10) // 2
        else:
            return f"Could Not Set {attribute}!"
        await self.reload_skills()
        return f"Set {attribute}= {level}"
