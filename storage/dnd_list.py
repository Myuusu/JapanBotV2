# |-------------------------------------------------------------------------------------------------------------------------------------------|
# | Source            | Site                        | Licence Type                                                                            |
# |-------------------|-----------------------------|-----------------------------------------------------------------------------------------|
# | open5e            | https://open5e.com/         | Content provided under the OGL 1.0a                                                     |
# |-------------------|-----------------------------|-----------------------------------------------------------------------------------------|
# | 5e.tools          | https://5e.tools/           | 5etools® is a Registered Trademark of The Norr Group Ltd. All rights reserved.          |
# |-------------------|-----------------------------|-----------------------------------------------------------------------------------------|
# | www.dndbeyond.com | https://www.dndbeyond.com/  | ©2020 D&D Beyond | All Rights Reserved | Powered by Fandom Games                        |
# |-------------------|-----------------------------|-----------------------------------------------------------------------------------------|
# | dnd.wizards.com   | https://dnd.wizards.com/    | © 1993-2020 Wizards of the Coast LLC, a subsidiary of Hasbro, Inc. All Rights Reserved. |
# |-------------------------------------------------------------------------------------------------------------------------------------------|

# https://api.open5e.com/races/
race_list = {
    "dwarf": {
        "name": "Dwarf",
        "slug": "dwarf",
        "desc": "## Dwarf Traits\n"
                "Your dwarf character has an assortment of inborn abilities, part and parcel of dwarven nature.",
        "asi_desc": "**_Ability Score Increase._** Your Constitution score increases by 2.",
        "asi": [
            {
                "attributes": [
                    "Constitution"
                ],
                "value": 2
            }
        ],
        "age": "**_Age._** Dwarves mature at the same rate as humans, but they're considered young until they reach the age of 50. On average, they live about 350 years.",
        "alignment": "**_Alignment._** Most dwarves are lawful, believing firmly in the benefits of a well-ordered society. They tend toward good as well, with a strong sense of fair play and a belief that everyone deserves to share in the benefits of a just order.",
        "size": "**_Size._** Dwarves stand between 4 and 5 feet tall and average about 150 pounds. Your size is Medium.",
        "speed": {
            "walk": 25
        },
        "speed_desc": "**_Speed._** Your base walking speed is 25 feet. Your speed is not reduced by wearing heavy armor.",
        "languages": "**_Languages._** You can speak, read, and write Common and Dwarvish. Dwarvish is full of hard consonants and guttural sounds, and those characteristics spill over into whatever other language a dwarf might speak.",
        "vision": "**_Darkvision._** Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
        "traits": "**_Dwarven Resilience._** You have advantage on saving throws against poison, and you have resistance against poison damage.\n\n"
                  "**_Dwarven Combat Training._** You have proficiency with the battleaxe, handaxe, light hammer, and warhammer.\n\n"
                  "**_Tool Proficiency._** You gain proficiency with the artisan's tools of your choice: smith's tools, brewer's supplies, or mason's tools.\n\n"
                  "**_Stonecunning._** Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus.",
        "subraces": [
            {
                "name": "Hill Dwarf",
                "slug": "hill-dwarf",
                "desc": "As a hill dwarf, you have keen senses, deep intuition, and remarkable resilience.",
                "asi": [
                    {
                        "attributes": [
                            "Wisdom"
                        ],
                        "value": 1
                    }
                ],
                "traits": "**_Dwarven Toughness._** Your hit point maximum increases by 1, and it increases by 1 every time you gain a level.",
                "asi_desc": "**_Ability Score Increase._** Your Wisdom score increases by 1",
                "document__slug": "wotc-srd",
                "document__title": "Systems Reference Document"
            }
        ],
        "document__slug": "wotc-srd",
        "document__title": "Systems Reference Document",
        "document__license_url": "http://open5e.com/legal"
    },
    "elf": {
        "name": "Elf",
        "slug": "elf",
        "desc": "## Elf Traits\n"
                "Your elf character has a variety of natural abilities, the result of thousands of years of elven refinement.",
        "asi_desc": "**_Ability Score Increase._** Your Dexterity score increases by 2.",
        "asi": [
            {
                "attributes": [
                    "Dexterity"
                ],
                "value": 2
            }
        ],
        "age": "**_Age._** Although elves reach physical maturity at about the same age as humans, the elven understanding of adulthood goes beyond physical growth to encompass worldly experience. An elf typically claims adulthood and an adult name around the age of 100 and can live to be 750 years old.",
        "alignment": "**_Alignment._** Elves love freedom, variety, and self- expression, so they lean strongly toward the gentler aspects of chaos. They value and protect others' freedom as well as their own, and they are more often good than not. The drow are an exception; their exile has made them vicious and dangerous. Drow are more often evil than not.",
        "size": "**_Size._** Elves range from under 5 to over 6 feet tall and have slender builds. Your size is Medium.",
        "speed": {
            "walk": 30
        },
        "speed_desc": "**_Speed._** Your base walking speed is 30 feet.",
        "languages": "**_Languages._** You can speak, read, and write Common and Elvish. Elvish is fluid, with subtle intonations and intricate grammar. Elven literature is rich and varied, and their songs and poems are famous among other races. Many bards learn their language so they can add Elvish ballads to their repertoires.",
        "vision": "**_Darkvision._** Accustomed to twilit forests and the night sky, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
        "traits": "**_Keen Senses._** You have proficiency in the Perception skill.\n\n"
                  "**_Fey Ancestry._** You have advantage on saving throws against being charmed, and magic can't put you to sleep.\n\n"
                  "**_Trance._** Elves don't need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. (The Common word for such meditation is “trance.”) While meditating, you can dream after a fashion; such dreams are actually mental exercises that have become reflexive through years of practice.\n"
                  "After resting in this way, you gain the same benefit that a human does from 8 hours of sleep.",
        "subraces": [
            {
                "name": "High Elf",
                "slug": "high-elf",
                "desc": "As a high elf, you have a keen mind and a mastery of at least the basics of magic. In many fantasy gaming worlds, there are two kinds of high elves. One type is haughty and reclusive, believing themselves to be superior to non-elves and even other elves. The other type is more common and more friendly, and often encountered among humans and other races.",
                "asi": [
                    {
                        "attributes": [
                            "Intelligence"
                        ],
                        "value": 1
                    }
                ],
                "traits": "**_Elf Weapon Training._** You have proficiency with the longsword, shortsword, shortbow, and longbow.\n\n"
                          "**_Cantrip._** You know one cantrip of your choice from the wizard spell list. Intelligence is your spellcasting ability for it.\n\n"
                          "**_Extra Language._** You can speak, read, and write one extra language of your choice.",
                "asi_desc": "**_Ability Score Increase._** Your Intelligence score increases by 1.",
                "document__slug": "wotc-srd",
                "document__title": "Systems Reference Document"
            }
        ],
        "document__slug": "wotc-srd",
        "document__title": "Systems Reference Document",
        "document__license_url": "http://open5e.com/legal"
    },
    "halfling": {
        "name": "Halfling",
        "slug": "halfling",
        "desc": "## Halfling Traits\n"
                "Your halfling character has a number of traits in common with all other halflings.",
        "asi_desc": "**_Ability Score Increase._** Your Dexterity score increases by 2.",
        "asi": [
            {
                "attributes": [
                    "Dexterity"
                ],
                "value": 2
            }
        ],
        "age": "**_Age._** A halfling reaches adulthood at the age of 20 and generally lives into the middle of his or her second century.",
        "alignment": "**_Alignment._** Most halflings are lawful good. As a rule, they are good-hearted and kind, hate to see others in pain, and have no tolerance for oppression. They are also very orderly and traditional, leaning heavily on the support of their community and the comfort of their old ways.",
        "size": "**_Size._** Halflings average about 3 feet tall and weigh about 40 pounds. Your size is Small.",
        "speed": {
            "walk": 25
        },
        "speed_desc": "**_Speed._** Your base walking speed is 25 feet.",
        "languages": "**_Languages._** You can speak, read, and write Common and Halfling. The Halfling language isn't secret, but halflings are loath to share it with others. They write very little, so they don't have a rich body of literature. Their oral tradition, however, is very strong. Almost all halflings speak Common to converse with the people in whose lands they dwell or through which they are traveling.",
        "vision": "",
        "traits": "**_Lucky._** When you roll a 1 on the d20 for an attack roll, ability check, or saving throw, you can reroll the die and must use the new roll.\n\n"
                  "**_Brave._** You have advantage on saving throws against being frightened.\n\n"
                  "**_Halfling Nimbleness._** You can move through the space of any creature that is of a size larger than yours.",
        "subraces": [
            {
                "name": "Lightfoot",
                "slug": "lightfoot",
                "desc": "As a lightfoot halfling, you can easily hide from notice, even using other people as cover. You're inclined to be affable and get along well with others.\n"
                        "Lightfoots are more prone to wanderlust than other halflings, and often dwell alongside other races or take up a nomadic life.",
                "asi": [
                    {
                        "attributes": [
                            "Charisma"
                        ],
                        "value": 1
                    }
                ],
                "traits": "**_Naturally Stealthy._** You can attempt to hide even when you are obscured only by a creature that is at least one size larger than you.",
                "asi_desc": "**_Ability Score Increase._** Your Charisma score increases by 1.",
                "document__slug": "wotc-srd",
                "document__title": "Systems Reference Document"
            }
        ],
        "document__slug": "wotc-srd",
        "document__title": "Systems Reference Document",
        "document__license_url": "http://open5e.com/legal"
    },
    "human": {
        "name": "Human",
        "slug": "human",
        "desc": "## Human Traits\n"
                "It's hard to make generalizations about humans, but your human character has these traits.",
        "asi_desc": "**_Ability Score Increase._** Your ability scores each increase by 1.",
        "asi": [
            {
                "attributes": [
                    "Strength"
                ],
                "value": 1
            },
            {
                "attributes": [
                    "Dexterity"
                ],
                "value": 1
            },
            {
                "attributes": [
                    "Constitution"
                ],
                "value": 1
            },
            {
                "attributes": [
                    "Intelligence"
                ],
                "value": 1
            },
            {
                "attributes": [
                    "Wisdom"
                ],
                "value": 1
            },
            {
                "attributes": [
                    "Charisma"
                ],
                "value": 1
            }
        ],
        "age": "**_Age._** Humans reach adulthood in their late teens and live less than a century.",
        "alignment": "**_Alignment._** Humans tend toward no particular alignment. The best and the worst are found among them.",
        "size": "**_Size._** Humans vary widely in height and build, from barely 5 feet to well over 6 feet tall. Regardless of your position in that range, your size is Medium.",
        "speed": {
            "walk": 30
        },
        "speed_desc": "**_Speed._** Your base walking speed is 30 feet.",
        "languages": "**_Languages._** You can speak, read, and write Common and one extra language of your choice. Humans typically learn the languages of other peoples they deal with, including obscure dialects. They are fond of sprinkling their speech with words borrowed from other tongues: Orc curses, Elvish musical expressions, Dwarvish military phrases, and so on.",
        "vision": "",
        "traits": "",
        "subraces": [],
        "document__slug": "wotc-srd",
        "document__title": "Systems Reference Document",
        "document__license_url": "http://open5e.com/legal"
    },
    "dragonborn": {
        "name": "Dragonborn",
        "slug": "dragonborn",
        "desc": "## Dragonborn Traits\n"
                "Your draconic heritage manifests in a variety of traits you share with other dragonborn.",
        "asi_desc": "**_Ability Score Increase._** Your Strength score increases by 2, and your Charisma score increases by 1.",
        "asi": [
            {
                "attributes": [
                    "Strength"
                ],
                "value": 2
            },
            {
                "attributes": [
                    "Charisma"
                ],
                "value": 1
            }
        ],
        "age": "**_Age._** Young dragonborn grow quickly. They walk hours after hatching, attain the size and development of a 10-year-old human child by the age of 3, and reach adulthood by 15. They live to be around 80.",
        "alignment": "**_Alignment._** Dragonborn tend to extremes, making a conscious choice for one side or the other in the cosmic war between good and evil. Most dragonborn are good, but those who side with evil can be terrible villains.",
        "size": "**_Size._** Dragonborn are taller and heavier than humans, standing well over 6 feet tall and averaging almost 250 pounds. Your size is Medium.",
        "speed": {
            "walk": 30
        },
        "speed_desc": "**_Speed._** Your base walking speed is 30 feet.",
        "languages": "**_Languages._** You can speak, read, and write Common and Draconic. Draconic is thought to be one of the oldest languages and is often used in the study of magic. The language sounds harsh to most other creatures and includes numerous hard consonants and sibilants.",
        "vision": "",
        "traits": "**Draconic Ancestry** \n\n"
                  "| Dragon       | Damage Type       | Breath Weapon                |\n"
                  "|--------------|-------------------|------------------------------|\n"
                  "| Black        | Acid              | 5 by 30 ft. line (Dex. save) |\n"
                  "| Blue         | Lightning         | 5 by 30 ft. line (Dex. save) |\n"
                  "| Brass        | Fire              | 5 by 30 ft. line (Dex. save) |\n"
                  "| Bronze       | Lightning         | 5 by 30 ft. line (Dex. save) |\n"
                  "| Copper       | Acid              | 5 by 30 ft. line (Dex. save) |\n"
                  "| Gold         | Fire              | 15 ft. cone (Dex. save)      |\n"
                  "| Green        | Poison            | 15 ft. cone (Con. save)      |\n"
                  "| Red          | Fire              | 15 ft. cone (Dex. save)      |\n"
                  "| Silver       | Cold              | 15 ft. cone (Con. save)      |\n"
                  "| White        | Cold              | 15 ft. cone (Con. save)      |\n\n\n"
                  "**_Draconic Ancestry._** You have draconic ancestry. Choose one type of dragon from the Draconic Ancestry table. Your breath weapon and damage resistance are determined by the dragon type, as shown in the table.\n\n"
                  "**_Breath Weapon._** You can use your action to exhale destructive energy. Your draconic ancestry determines the size, shape, and damage type of the exhalation.\n"
                  "When you use your breath weapon, each creature in the area of the exhalation must make a saving throw, the type of which is determined by your draconic ancestry. The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. The damage increases to 3d6 at 6th level, 4d6 at 11th level, and 5d6 at 16th level.\n"
                  "After you use your breath weapon, you can't use it again until you complete a short or long rest.\n\n"
                  "**_Damage Resistance._** You have resistance to the damage type associated with your draconic ancestry.",
        "subraces": [],
        "document__slug": "wotc-srd",
        "document__title": "Systems Reference Document",
        "document__license_url": "http://open5e.com/legal"
    },
    "gnome": {
        "name": "Gnome",
        "slug": "gnome",
        "desc": "## Gnome Traits\n"
                "Your gnome character has certain characteristics in common with all other gnomes.",
        "asi_desc": "**_Ability Score Increase._** Your Intelligence score increases by 2.",
        "asi": [
            {
                "attributes": [
                    "Intelligence"
                ],
                "value": 2
            }
        ],
        "age": "**_Age._** Gnomes mature at the same rate humans do, and most are expected to settle down into an adult life by around age 40. They can live 350 to almost 500 years.",
        "alignment": "**_Alignment._** Gnomes are most often good. Those who tend toward law are sages, engineers, researchers, scholars, investigators, or inventors. Those who tend toward chaos are minstrels, tricksters, wanderers, or fanciful jewelers. Gnomes are good-hearted, and even the tricksters among them are more playful than vicious.",
        "size": "**_Size._** Gnomes are between 3 and 4 feet tall and average about 40 pounds. Your size is Small.",
        "speed": {
            "walk": 25
        },
        "speed_desc": "**_Speed._** Your base walking speed is 25 feet.",
        "languages": "**_Languages._** You can speak, read, and write Common and Gnomish. The Gnomish language, which uses the Dwarvish script, is renowned for its technical treatises and its catalogs of knowledge about the natural world.",
        "vision": "**_Darkvision._** Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
        "traits": "**_Gnome Cunning._** You have advantage on all Intelligence, Wisdom, and Charisma saving throws against magic.",
        "subraces": [
            {
                "name": "Rock Gnome",
                "slug": "rock-gnome",
                "desc": "## Rock Gnome\n"
                        "As a rock gnome, you have a natural inventiveness and hardiness beyond that of other gnomes.",
                "asi": [
                    {
                        "attributes": [
                            "Constitution"
                        ],
                        "value": 1
                    }
                ],
                "traits": "**_Artificer's Lore._** Whenever you make an Intelligence (History) check related to magic items, alchemical objects, or technological devices, you can add twice your proficiency bonus, instead of any proficiency bonus you normally apply.\n\n"
                          "**_Tinker._** You have proficiency with artisan's tools (tinker's tools). Using those tools, you can spend 1 hour and 10 gp worth of materials to construct a Tiny clockwork device (AC 5, 1 hp). The device ceases to function after 24 hours (unless you spend 1 hour repairing it to keep the device functioning), or when you use your action to dismantle it; at that time, you can reclaim the materials used to create it. You can have up to three such devices active at a time.\n"
                          "When you create a device, choose one of the following options:\n"
                          "* _Clockwork Toy._ This toy is a clockwork animal, monster, or person, such as a frog, mouse, bird, dragon, or soldier. When placed on the ground, the toy moves 5 feet across the ground on each of your turns in a random direction. It makes noises as appropriate to the creature it represents.\n"
                          "* _Fire Starter._ The device produces a miniature flame, which you can use to light a candle, torch, or campfire. Using the device requires your action.\n"
                          "* _Music Box._ When opened, this music box plays a single song at a moderate volume. The box stops playing when it reaches the song's end or when it is closed.",
                "asi_desc": "**_Ability Score Increase._** Your Constitution score increases by 1.",
                "document__slug": "wotc-srd",
                "document__title": "Systems Reference Document"
            }
        ],
        "document__slug": "wotc-srd",
        "document__title": "Systems Reference Document",
        "document__license_url": "http://open5e.com/legal"
    },
    "half-elf": {
        "name": "Half-Elf",
        "slug": "half-elf",
        "desc": "## Half-Elf Traits\n"
                "Your half-elf character has some qualities in common with elves and some that are unique to half-elves.",
        "asi_desc": "**_Ability Score Increase._** Your Charisma score increases by 2, and two other ability scores of your choice increase by 1.",
        "asi": [
            {
                "attributes": [
                    "Charisma"
                ],
                "value": 2
            },
            {
                "attributes": [
                    "Other"
                ],
                "value": 1
            },
            {
                "attributes": [
                    "Other"
                ],
                "value": 1
            }
        ],
        "age": "**_Age._** Half-elves mature at the same rate humans do and reach adulthood around the age of 20. They live much longer than humans, however, often exceeding 180 years.",
        "alignment": "**_Alignment._** Half-elves share the chaotic bent of their elven heritage. They value both personal freedom and creative expression, demonstrating neither love of leaders nor desire for followers. They chafe at rules, resent others' demands, and sometimes prove unreliable, or at least unpredictable.",
        "size": "**_Size._** Half-elves are about the same size as humans, ranging from 5 to 6 feet tall. Your size is Medium.",
        "speed": {
            "walk": 30
        },
        "speed_desc": "**_Speed._** Your base walking speed is 30 feet.",
        "languages": "**_Languages._** You can speak, read, and write Common, Elvish, and one extra language of your choice.",
        "vision": "**_Darkvision._** Thanks to your elf blood, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
        "traits": "**_Fey Ancestry._** You have advantage on saving throws against being charmed, and magic can't put you to sleep.\n\n"
                  "**_Skill Versatility._** You gain proficiency in two skills of your choice.",
        "subraces": [],
        "document__slug": "wotc-srd",
        "document__title": "Systems Reference Document",
        "document__license_url": "http://open5e.com/legal"
    },
    "half-orc": {
        "name": "Half-Orc",
        "slug": "half-orc",
        "desc": "## Half-Orc Traits\n"
                "Your half-orc character has certain traits deriving from your orc ancestry.",
        "asi_desc": "**_Ability Score Increase._** Your Strength score increases by 2, and your Constitution score increases by 1.",
        "asi": [
            {
                "attributes": [
                    "Strength"
                ],
                "value": 2
            },
            {
                "attributes": [
                    "Constitution"
                ],
                "value": 1
            }
        ],
        "age": "**_Age._** Half-orcs mature a little faster than humans, reaching adulthood around age 14. They age noticeably faster and rarely live longer than 75 years.",
        "alignment": "**_Alignment._** Half-orcs inherit a tendency toward chaos from their orc parents and are not strongly inclined toward good. Half-orcs raised among orcs and willing to live out their lives among them are usually evil.",
        "size": "**_Size._** Half-orcs are somewhat larger and bulkier than humans, and they range from 5 to well over 6 feet tall. Your size is Medium.",
        "speed": {
            "walk": 30
        },
        "speed_desc": "**_Speed._** Your base walking speed is 30 feet.",
        "languages": "**_Languages._** You can speak, read, and write Common and Orc. Orc is a harsh, grating language with hard consonants. It has no script of its own but is written in the Dwarvish script.",
        "vision": "**_Darkvision._** Thanks to your orc blood, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
        "traits": "**_Menacing._** You gain proficiency in the Intimidation skill.\n\n"
                  "**_Relentless Endurance._** When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can't use this feature again until you finish a long rest.\n\n"
                  "**_Savage Attacks._** When you score a critical hit with a melee weapon attack, you can roll one of the weapon's damage dice one additional time and add it to the extra damage of the critical hit.",
        "subraces": [],
        "document__slug": "wotc-srd",
        "document__title": "Systems Reference Document",
        "document__license_url": "http://open5e.com/legal"
    },
    "tiefling": {
        "name": "Tiefling",
        "slug": "tiefling",
        "desc": "## Tiefling Traits\n"
                "Tieflings share certain racial traits as a result of their infernal descent.",
        "asi_desc": "**_Ability Score Increase._** Your Intelligence score increases by 1, and your Charisma score increases by 2.",
        "asi": [
            {
                "attributes": [
                    "Intelligence"
                ],
                "value": 1
            },
            {
                "attributes": [
                    "Charisma"
                ],
                "value": 2
            }
        ],
        "age": "**_Age._** Tieflings mature at the same rate as humans but live a few years longer.",
        "alignment": "**_Alignment._** Tieflings might not have an innate tendency toward evil, but many of them end up there. Evil or not, an independent nature inclines many tieflings toward a chaotic alignment.",
        "size": "**_Size._** Tieflings are about the same size and build as humans. Your size is Medium.",
        "speed": {
            "walk": 30
        },
        "speed_desc": "**_Speed._** Your base walking speed is 30 feet.",
        "languages": "**_Languages._** You can speak, read, and write Common and Infernal.",
        "vision": "**_Darkvision._** Thanks to your infernal heritage, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
        "traits": "**_Hellish Resistance._** You have resistance to fire damage.\n\n"
                  "**_Infernal Legacy._** You know the *thaumaturgy* cantrip. When you reach 3rd level, you can cast the *hellish rebuke* spell as a 2nd-level spell once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the *darkness* spell once with this trait and regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these spells.",
        "subraces": [],
        "document__slug": "wotc-srd",
        "document__title": "Systems Reference Document",
        "document__license_url": "http://open5e.com/legal"
    }
}

# https://api.open5e.com/classes/
class_list = {
    "barbarian": {
        "name": "Barbarian",
        "slug": "barbarian",
        "desc": "### Rage \n \n"
                "In battle, you fight with primal ferocity. On your turn, you can enter a rage as a bonus action. \n \n"
                "While raging, you gain the following benefits if you aren't wearing heavy armor: \n \n"
                "* You have advantage on Strength checks and Strength saving throws. \n"
                "* When you make a melee weapon attack using Strength, you gain a bonus to the damage roll that increases as you gain levels as a barbarian, as shown in the Rage Damage column of the Barbarian table. \n"
                "* You have resistance to bludgeoning, piercing, and slashing damage. \n \n"
                "If you are able to cast spells, you can't cast them or concentrate on them while raging. \n \n"
                "Your rage lasts for 1 minute. It ends early if you are knocked unconscious or if your turn ends and you haven't attacked a hostile creature since your last turn or taken damage since then. You can also end your rage on your turn as a bonus action. \n \n"
                "Once you have raged the number of times shown for your barbarian level in the Rages column of the Barbarian table, you must finish a long rest before you can rage again. \n \n"
                "### Unarmored Defense \n \n"
                "While you are not wearing any armor, your Armor Class equals 10 + your Dexterity modifier + your Constitution modifier. You can use a shield and still gain this benefit. \n \n"
                "### Reckless Attack \n \n"
                "Starting at 2nd level, you can throw aside all concern for defense to attack with fierce desperation. When you make your first attack on your turn, you can decide to attack recklessly. Doing so gives you advantage on melee weapon attack rolls using Strength during this turn, but attack rolls against you have advantage until your next turn. \n \n"
                "### Danger Sense \n \n"
                "At 2nd level, you gain an uncanny sense of when things nearby aren't as they should be, giving you an edge when you dodge away from danger. \n \n"
                "You have advantage on Dexterity saving throws against effects that you can see, such as traps and spells. To gain this benefit, you can't be blinded, deafened, or incapacitated. \n \n"
                "### Primal Path \n \n"
                "At 3rd level, you choose a path that shapes the nature of your rage. Choose the Path of the Berserker or the Path of the Totem Warrior, both detailed at the end of the class description. Your choice grants you features at 3rd level and again at 6th, 10th, and 14th levels. \n \n"
                "### Ability Score Improvement \n \n"
                "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature. \n \n"
                "### Extra Attack \n \n"
                "Beginning at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn. \n \n"
                "### Fast Movement \n \n"
                "Starting at 5th level, your speed increases by 10 feet while you aren't wearing heavy armor. \n \n"
                "### Feral Instinct \n \n"
                "By 7th level, your instincts are so honed that you have advantage on initiative rolls. \n \n"
                "Additionally, if you are surprised at the beginning of combat and aren't incapacitated, you can act normally on your first turn, but only if you enter your rage before doing anything else on that turn. \n \n"
                "### Brutal Critical \n \n"
                "Beginning at 9th level, you can roll one additional weapon damage die when determining the extra damage for a critical hit with a melee attack. \n \n"
                "This increases to two additional dice at 13th level and three additional dice at 17th level. \n \n"
                "### Relentless Rage \n \n"
                "Starting at 11th level, your rage can keep you fighting despite grievous wounds. If you drop to 0 hit points while you're raging and don't die outright, you can make a DC 10 Constitution saving throw. If you succeed, you drop to 1 hit point instead. \n \n"
                "Each time you use this feature after the first, the DC increases by 5. When you finish a short or long rest, the DC resets to 10. \n \n"
                "### Persistent Rage \n \n"
                "Beginning at 15th level, your rage is so fierce that it ends early only if you fall unconscious or if you choose to end it. \n \n"
                "### Indomitable Might \n \n"
                "Beginning at 18th level, if your total for a Strength check is less than your Strength score, you can use that score in place of the total. \n \n"
                "### Primal Champion \n \n"
                "At 20th level, you embody the power of the wilds. Your Strength and Constitution scores increase by 4. Your maximum for those scores is now 24.",
        "hit_dice": "1d12",
        "hp_at_1st_level": "12 + your Constitution modifier",
        "hp_at_higher_levels": "1d12 (or 7) + your Constitution modifier per barbarian level after 1st",
        "prof_armor": "Light armor, medium armor, shields",
        "prof_weapons": "Simple weapons, martial weapons",
        "prof_tools": "None",
        "prof_saving_throws": "Strength, Constitution",
        "prof_skills": "Choose two from Animal Handling, Athletics, Intimidation, Nature, Perception, and Survival",
        "equipment": "You start with the following equipment, in addition to the equipment granted by your background: \n \n"
                     "* (*a*) a greataxe or (*b*) any martial melee weapon \n"
                     "* (*a*) two handaxes or (*b*) any simple weapon \n"
                     "* An explorer's pack and four javelins",
        "table": "| Level  | Proficiency Bonus | Features                      | Rages     | Rage Damage | \n"
                 "|--------|-------------------|-------------------------------|-----------|-------------| \n"
                 "| 1st    | +2                | Rage, Unarmored Defense       | 2         | +2          | \n"
                 "| 2nd    | +2                | Reckless Attack, Danger Sense | 2         | +2          | \n"
                 "| 3rd    | +2                | Primal Path                   | 3         | +2          | \n"
                 "| 4th    | +2                | Ability Score Improvement     | 3         | +2          | \n"
                 "| 5th    | +3                | Extra Attack, Fast Movement   | 3         | +2          | \n"
                 "| 6th    | +3                | Path feature                  | 4         | +2          | \n"
                 "| 7th    | +3                | Feral Instinct                | 4         | +2          | \n"
                 "| 8th    | +3                | Ability Score Improvement     | 4         | +2          | \n"
                 "| 9th    | +4                | Brutal Critical (1 die)       | 4         | +3          | \n"
                 "| 10th   | +4                | Path feature                  | 4         | +3          | \n"
                 "| 11th   | +4                | Relentless                    | 4         | +3          | \n"
                 "| 12th   | +4                | Ability Score Improvement     | 5         | +3          | \n"
                 "| 13th   | +5                | Brutal Critical (2 dice)      | 5         | +3          | \n"
                 "| 14th   | +5                | Path feature                  | 5         | +3          | \n"
                 "| 15th   | +5                | Persistent Rage               | 5         | +3          | \n"
                 "| 16th   | +5                | Ability Score Improvement     | 5         | +4          | \n"
                 "| 17th   | +6                | Brutal Critical (3 dice)      | 6         | +4          | \n"
                 "| 18th   | +6                | Indomitable Might             | 6         | +4          | \n"
                 "| 19th   | +6                | Ability Score Improvement     | 6         | +4          | \n"
                 "| 20th   | +6                | Primal Champion               | Unlimited | +4          | ",
        "spellcasting_ability": "",
        "subtypes_name": "Paths",
        "archetypes": [
            {
                "name": "Path of the Berserker",
                "slug": "path-of-the-berserker",
                "desc": "For some barbarians, rage is a means to an end- that end being violence. The Path of the Berserker is a path of untrammeled fury, slick with blood. As you enter the berserker's rage, you thrill in the chaos of battle, heedless of your own health or well-being. \n \n"
                        "##### Frenzy \n \n"
                        "Starting when you choose this path at 3rd level, you can go into a frenzy when you rage. If you do so, for the duration of your rage you can make a single melee weapon attack as a bonus action on each of your turns after this one. When your rage ends, you suffer one level of exhaustion (as described in appendix A). \n \n"
                        "##### Mindless Rage \n \n"
                        "Beginning at 6th level, you can't be charmed or frightened while raging. If you are charmed or frightened when you enter your rage, the effect is suspended for the duration of the rage. \n \n"
                        "##### Intimidating Presence \n \n"
                        "Beginning at 10th level, you can use your action to frighten someone with your menacing presence. When you do so, choose one creature that you can see within 30 feet of you. If the creature can see or hear you, it must succeed on a Wisdom saving throw (DC equal to 8 + your proficiency bonus + your Charisma modifier) or be frightened of you until the end of your next turn. On subsequent turns, you can use your action to extend the duration of this effect on the frightened creature until the end of your next turn. This effect ends if the creature ends its turn out of line of sight or more than 60 feet away from you. \n \n"
                        "If the creature succeeds on its saving throw, you can't use this feature on that creature again for 24 hours. \n \n"
                        "##### Retaliation \n \n"
                        "Starting at 14th level, when you take damage from a creature that is within 5 feet of you, you can use your reaction to make a melee weapon attack against that creature.",
                "document__slug": "wotc-srd",
                "document__title": "Systems Reference Document",
                "document__license_url": "http://open5e.com/legal"
            }
        ],
        "document__slug": "wotc-srd",
        "document__title": "Systems Reference Document",
        "document__license_url": "http://open5e.com/legal"
    },
    "bard": {
        "name": "Bard",
        "slug": "bard",
        "desc": "### Spellcasting \n \n"
                "You have learned to untangle and reshape the fabric of reality in harmony with your wishes and music. \n \n"
                "Your spells are part of your vast repertoire, magic that you can tune to different situations. \n \n"
                "#### Cantrips \n \n"
                "You know two cantrips of your choice from the bard spell list. You learn additional bard cantrips of your choice at higher levels, as shown in the Cantrips Known column of the Bard table. \n \n"
                "#### Spell Slots \n \n"
                "The Bard table shows how many spell slots you have to cast your spells of 1st level and higher. To cast one of these spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest. \n \n"
                "For example, if you know the 1st-level spell *cure wounds* and have a 1st-level and a 2nd-level spell slot available, you can cast *cure wounds* using either slot. \n \n"
                "#### Spells Known of 1st Level and Higher \n \n"
                "You know four 1st-level spells of your choice from the bard spell list. \n \n"
                "The Spells Known column of the Bard table shows when you learn more bard spells of your choice. Each of these spells must be of a level for which you have spell slots, as shown on the table. For instance, when you reach 3rd level in this class, you can learn one new spell of 1st or 2nd level. \n \n"
                "Additionally, when you gain a level in this class, you can choose one of the bard spells you know and replace it with another spell from the bard spell list, which also must be of a level for which you have spell slots. \n \n"
                "#### Spellcasting Ability \n \n"
                "Charisma is your spellcasting ability for your bard spells. Your magic comes from the heart and soul you pour into the performance of your music or oration. You use your Charisma whenever a spell refers to your spellcasting ability. In addition, you use your Charisma modifier when setting the saving throw DC for a bard spell you cast and when making an attack roll with one. \n \n"
                "**Spell save DC** = 8 + your proficiency bonus + your Charisma modifier \n \n**Spell attack modifier** = your proficiency bonus + your Charisma modifier \n \n"
                "#### Ritual Casting \n \nYou can cast any bard spell you know as a ritual if that spell has the ritual tag. \n \n"
                "#### Spellcasting Focus \n \n"
                "You can use a musical instrument (see chapter 5, “Equipment”) as a spellcasting focus for your bard spells. \n \n"
                "### Bardic Inspiration \n \n"
                "You can inspire others through stirring words or music. To do so, you use a bonus action on your turn to choose one creature other than yourself within 60 feet of you who can hear you. That creature gains one Bardic Inspiration die, a d6. \n \n"
                "Once within the next 10 minutes, the creature can roll the die and add the number rolled to one ability check, attack roll, or saving throw it makes. The creature can wait until after it rolls the d20 before deciding to use the Bardic Inspiration die, but must decide before the GM says whether the roll succeeds or fails. Once the Bardic Inspiration die is rolled, it is lost. A creature can have only one Bardic Inspiration die at a time. \n \n"
                "You can use this feature a number of times equal to your Charisma modifier (a minimum of once). You regain any expended uses when you finish a long rest. \n \n"
                "Your Bardic Inspiration die changes when you reach certain levels in this class. The die becomes a d8 at 5th level, a d10 at 10th level, and a d12 at 15th level. \n \n"
                "### Jack of All Trades \n \n"
                "Starting at 2nd level, you can add half your proficiency bonus, rounded down, to any ability check you make that doesn't already include your proficiency bonus. \n \n"
                "### Song of Rest \n \n"
                "Beginning at 2nd level, you can use soothing music or oration to help revitalize your wounded allies during a short rest. If you or any friendly creatures who can hear your performance regain hit points at the end of the short rest by spending one or more Hit Dice, each of those creatures regains an extra 1d6 hit points. \n \n"
                "The extra hit points increase when you reach certain levels in this class: to 1d8 at 9th level, to 1d10 at 13th level, and to 1d12 at 17th level. \n \n"
                "### Bard College \n \n"
                "At 3rd level, you delve into the advanced techniques of a bard college of your choice: the College of Lore or the College of Valor, both detailed at the end of \n \n"
                "the class description. Your choice grants you features at 3rd level and again at 6th and 14th level. \n \n"
                "### Expertise \n \n"
                "At 3rd level, choose two of your skill proficiencies. Your proficiency bonus is doubled for any ability check you make that uses either of the chosen proficiencies. \n \n"
                "At 10th level, you can choose another two skill proficiencies to gain this benefit. \n \n"
                "### Ability Score Improvement \n \n"
                "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature. \n \n"
                "### Font of Inspiration \n \n"
                "Beginning when you reach 5th level, you regain all of your expended uses of Bardic Inspiration when you finish a short or long rest. \n \n"
                "### Countercharm \n \n"
                "At 6th level, you gain the ability to use musical notes or words of power to disrupt mind-influencing effects. As an action, you can start a performance that lasts until the end of your next turn. During that time, you and any friendly creatures within 30 feet of you have advantage on saving throws against being frightened or charmed. A creature must be able to hear you to gain this benefit. The performance ends early if you are incapacitated or silenced or if you voluntarily end it (no action required). \n \n"
                "### Magical Secrets \n \n"
                "By 10th level, you have plundered magical knowledge from a wide spectrum of disciplines. Choose two spells from any class, including this one. A spell you choose must be of a level you can cast, as shown on the Bard table, or a cantrip. \n \n"
                "The chosen spells count as bard spells for you and are included in the number in the Spells Known column of the Bard table. \n \n"
                "You learn two additional spells from any class at 14th level and again at 18th level. \n \n"
                "### Superior Inspiration \n \n"
                "At 20th level, when you roll initiative and have no uses of Bardic Inspiration left, you regain one use.",
        "hit_dice": "1d8",
        "hp_at_1st_level": "8 + your Constitution modifier",
        "hp_at_higher_levels": "1d8 (or 5) + your Constitution modifier per bard level after 1st",
        "prof_armor": "Light armor",
        "prof_weapons": "Simple weapons, hand crossbows, longswords, rapiers, shortswords",
        "prof_tools": "Three musical instruments of your choice",
        "prof_saving_throws": "Dexterity, Charisma",
        "prof_skills": "Choose any three",
        "equipment": "You start with the following equipment, in addition to the equipment granted by your background: \n \n"
                     "* (*a*) a rapier, (*b*) a longsword, or (*c*) any simple weapon \n"
                     "* (*a*) a diplomat's pack or (*b*) an entertainer's pack \n"
                     "* (*a*) a lute or (*b*) any other musical instrument \n"
                     "* Leather armor and a dagger",
        "table": "| Level | Proficiency Bonus| Features                                             | Spells Known | Cantrips Known | 1st | 2nd | 3rd | 4th | 5th | 6th | 7th | 8th | 9th | \n"
                 "|-------|------------------|------------------------------------------------------|--------------|----------------|-----|-----|-----|-----|-----|-----|-----|-----|-----| \n"
                 "| 1st   | +2               | Spellcasting, Bardic Inspiration (d6)                | 2            | 4              | 2   | -   | -   | -   | -   | -   | -   | -   | -   | \n"
                 "| 2nd   | +2               | Jack of All Trades, Song of Rest (d6)                | 2            | 5              | 3   | -   | -   | -   | -   | -   | -   | -   | -   | \n"
                 "| 3rd   | +2               | Bard College, Expertise                              | 2            | 6              | 4   | 2   | -   | -   | -   | -   | -   | -   | -   | \n"
                 "| 4th   | +2               | Ability Score Improvement                            | 3            | 7              | 4   | 3   | -   | -   | -   | -   | -   | -   | -   | \n"
                 "| 5th   | +3               | Bardic Inspiration (d8), Font of Inspiration         | 3            | 8              | 4   | 3   | 2   | -   | -   | -   | -   | -   | -   | \n"
                 "| 6th   | +3               | Countercharm, Bard College Feature                   | 3            | 9              | 4   | 3   | 3   | -   | -   | -   | -   | -   | -   | \n"
                 "| 7th   | +3               | -                                                    | 3            | 10             | 4   | 3   | 3   | 1   | -   | -   | -   | -   | -   | \n"
                 "| 8th   | +3               | Ability Score Improvement                            | 3            | 11             | 4   | 3   | 3   | 2   | -   | -   | -   | -   | -   | \n"
                 "| 9th   | +4               | Song of Rest (d8)                                    | 3            | 12             | 4   | 3   | 3   | 3   | 1   | -   | -   | -   | -   | \n"
                 "| 10th  | +4               | Bardic Inspiration (d10), Expertise, Magical Secrets | 4            | 14             | 4   | 3   | 3   | 3   | 2   | -   | -   | -   | -   | \n"
                 "| 11th  | +4               | -                                                    | 4            | 15             | 4   | 3   | 3   | 3   | 2   | 1   | -   | -   | -   | \n"
                 "| 12th  | +4               | Ability Score Improvement                            | 4            | 15             | 4   | 3   | 3   | 3   | 2   | 1   | -   | -   | -   | \n"
                 "| 13th  | +5               | Song of Rest (d10)                                   | 4            | 16             | 4   | 3   | 3   | 3   | 2   | 1   | 1   | -   | -   | \n"
                 "| 14th  | +5               | Magical Secrets, Bard College Feature                | 4            | 18             | 4   | 3   | 3   | 3   | 2   | 1   | 1   | -   | -   | \n"
                 "| 15th  | +5               | Bardic Inspiration (d12)                             | 4            | 19             | 4   | 3   | 3   | 3   | 2   | 1   | 1   | 1   | -   | \n"
                 "| 16th  | +5               | Ability Score Improvement                            | 4            | 19             | 4   | 3   | 3   | 3   | 2   | 1   | 1   | 1   | -   | \n"
                 "| 17th  | +6               | Song of Rest (d12)                                   | 4            | 20             | 4   | 3   | 3   | 3   | 2   | 1   | 1   | 1   | 1   | \n"
                 "| 18th  | +6               | Magical Secrets                                      | 4            | 22             | 4   | 3   | 3   | 3   | 3   | 1   | 1   | 1   | 1   | \n"
                 "| 19th  | +6               | Ability Score Improvement                            | 4            | 22             | 4   | 3   | 3   | 3   | 3   | 2   | 1   | 1   | 1   | \n"
                 "| 20th  | +6               | Superior Inspiration                                 | 4            | 22             | 4   | 3   | 3   | 3   | 3   | 2   | 2   | 1   | 1   | ",
        "spellcasting_ability": "Charisma",
        "subtypes_name": "Colleges",
        "archetypes": [
            {
                "name": "College of Lore",
                "slug": "college-of-lore",
                "desc": "Bards of the College of Lore know something about most things, collecting bits of knowledge from sources as diverse as scholarly tomes and peasant tales. Whether singing folk ballads in taverns or elaborate compositions in royal courts, these bards use their gifts to hold audiences spellbound. When the applause dies down, the audience members might find themselves questioning everything they held to be true, from their faith in the priesthood of the local temple to their loyalty to the king. \n \nThe loyalty of these bards lies in the pursuit of beauty and truth, not in fealty to a monarch or following the tenets of a deity. A noble who keeps such a bard as a herald or advisor knows that the bard would rather be honest than politic. \n \nThe college's members gather in libraries and sometimes in actual colleges, complete with classrooms and dormitories, to share their lore with one another. They also meet at festivals or affairs of state, where they can expose corruption, unravel lies, and poke fun at self-important figures of authority. \n \n##### Bonus Proficiencies \n \nWhen you join the College of Lore at 3rd level, you gain proficiency with three skills of your choice. \n \n##### Cutting Words \n \nAlso at 3rd level, you learn how to use your wit to distract, confuse, and otherwise sap the confidence and competence of others. When a creature that you can see within 60 feet of you makes an attack roll, an ability check, or a damage roll, you can use your reaction to expend one of your uses of Bardic Inspiration, rolling a Bardic Inspiration die and subtracting the number rolled from the creature's roll. You can choose to use this feature after the creature makes its roll, but before the GM determines whether the attack roll or ability check succeeds or fails, or before the creature deals its damage. The creature is immune if it can't hear you or if it's immune to being charmed. \n \n##### Additional Magical Secrets \n \nAt 6th level, you learn two spells of your choice from any class. A spell you choose must be of a level you can cast, as shown on the Bard table, or a cantrip. The chosen spells count as bard spells for you but don't count against the number of bard spells you know. \n \n##### Peerless Skill \n \nStarting at 14th level, when you make an ability check, you can expend one use of Bardic Inspiration. Roll a Bardic Inspiration die and add the number rolled to your ability check. You can choose to do so after you roll the die for the ability check, but before the GM tells you whether you succeed or fail.",
                "document__slug": "wotc-srd",
                "document__title": "Systems Reference Document",
                "document__license_url": "http://open5e.com/legal"
            }
        ],
        "document__slug": "wotc-srd",
        "document__title": "Systems Reference Document",
        "document__license_url": "http://open5e.com/legal"
    },
    "cleric": {
        "name": "Cleric",
        "slug": "cleric",
        "desc": "### Spellcasting \n \n"
                "As a conduit for divine power, you can cast cleric spells. \n \n"
                "#### Cantrips \n \n"
                "At 1st level, you know three cantrips of your choice from the cleric spell list. You learn additional cleric cantrips of your choice at higher levels, as shown in the Cantrips Known column of the Cleric table. \n \n"
                "#### Preparing and Casting Spells \n \n"
                "The Cleric table shows how many spell slots you have to cast your spells of 1st level and higher. To cast one of these spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest. \n \n"
                "You prepare the list of cleric spells that are available for you to cast, choosing from the cleric spell list. When you do so, choose a number of cleric spells equal to your Wisdom modifier + your cleric level (minimum of one spell). The spells must be of a level for which you have spell slots. \n \n"
                "For example, if you are a 3rd-level cleric, you have four \n"
                "1st-level and two 2nd-level spell slots. With a Wisdom of 16, your list of prepared spells can include six spells of 1st or 2nd level, in any combination. If you prepare the 1st-level spell *cure wounds*, you can cast it using a 1st-level or 2nd-level slot. Casting the spell doesn't remove it from your list of prepared spells. \n \n"
                "You can change your list of prepared spells when you finish a long rest. Preparing a new list of cleric spells requires time spent in prayer and meditation: at least 1 minute per spell level for each spell on your list. \n \n"
                "#### Spellcasting Ability \n \n"
                "Wisdom is your spellcasting ability for your cleric spells. The power of your spells comes from your devotion to your deity. You use your Wisdom whenever a cleric spell refers to your spellcasting ability. In addition, you use your Wisdom modifier when setting the saving throw DC for a cleric spell you cast and when making an attack roll with one. \n \n"
                "**Spell save DC** = 8 + your proficiency bonus + your Wisdom modifier \n \n"
                "**Spell attack modifier** = your proficiency bonus + your Wisdom modifier \n \n"
                "#### Ritual Casting \n \n"
                "You can cast a cleric spell as a ritual if that spell has the ritual tag and you have the spell prepared. \n \n"
                "#### Spellcasting Focus \n \n"
                "You can use a holy symbol (see chapter 5, “Equipment”) as a spellcasting focus for your cleric spells. \n \n"
                "### Divine Domain \n \n"
                "Choose one domain related to your deity: Knowledge, Life, Light, Nature, Tempest, Trickery, or War. Each domain is detailed at the end of the class description, and each one provides examples of gods associated with it. Your choice grants you domain spells and other features when you choose it at 1st level. It also grants you additional ways to use Channel Divinity when you gain that feature at 2nd level, and additional benefits at 6th, 8th, and 17th levels. \n \n"
                "#### Domain Spells \n \n"
                "Each domain has a list of spells-its domain spells- that you gain at the cleric levels noted in the domain description. Once you gain a domain spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. \n \n"
                "If you have a domain spell that doesn't appear on the cleric spell list, the spell is nonetheless a cleric spell for you. \n \n"
                "### Channel Divinity \n \n"
                "At 2nd level, you gain the ability to channel divine energy directly from your deity, using that energy to fuel magical effects. You start with two such effects: Turn Undead and an effect determined by your domain. Some domains grant you additional effects as you advance in levels, as noted in the domain description. \n \n"
                "When you use your Channel Divinity, you choose which effect to create. You must then finish a short or long rest to use your Channel Divinity again. \n \n"
                "Some Channel Divinity effects require saving throws. When you use such an effect from this class, the DC equals your cleric spell save DC. \n \n"
                "Beginning at 6th level, you can use your Channel \n \n"
                "Divinity twice between rests, and beginning at 18th level, you can use it three times between rests. When you finish a short or long rest, you regain your expended uses. \n \n"
                "#### Channel Divinity: Turn Undead \n \n"
                "As an action, you present your holy symbol and speak a prayer censuring the undead. Each undead that can see or hear you within 30 feet of you must make a Wisdom saving throw. If the creature fails its saving throw, it is turned for 1 minute or until it takes any damage. \n \n"
                "A turned creature must spend its turns trying to move as far away from you as it can, and it can't willingly move to a space within 30 feet of you. It also can't take reactions. For its action, it can use only the Dash action or try to escape from an effect that prevents it from moving. If there's nowhere to move, the creature can use the Dodge action. \n \n"
                "### Ability Score Improvement \n \n"
                "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature. \n \n"
                "### Destroy Undead \n \n"
                "Starting at 5th level, when an undead fails its saving throw against your Turn Undead feature, the creature is instantly destroyed if its challenge rating is at or below a certain threshold, as shown in the Destroy Undead table. \n \n"
                "**Destroy Undead (table)** \n \n"
                "| Cleric Level | Destroys Undead of CR... | \n"
                "|--------------|--------------------------| \n"
                "| 5th          | 1/2 or lower             | \n"
                "| 8th          | 1 or lower               | \n"
                "| 11th         | 2 or lower               | \n"
                "| 14th         | 3 or lower               | \n"
                "| 17th         | 4 or lower               | \n \n"
                "### Divine Intervention \n \n"
                "Beginning at 10th level, you can call on your deity to intervene on your behalf when your need is great. \n \n"
                "Imploring your deity's aid requires you to use your action. Describe the assistance you seek, and roll percentile dice. If you roll a number equal to or lower than your cleric level, your deity intervenes. The GM chooses the nature of the intervention; the effect of any cleric spell or cleric domain spell would be appropriate. \n \n"
                "If your deity intervenes, you can't use this feature again for 7 days. Otherwise, you can use it again after you finish a long rest. \n \n"
                "At 20th level, your call for intervention succeeds automatically, no roll required.",
        "hit_dice": "1d8",
        "hp_at_1st_level": "8 + your Constitution modifier",
        "hp_at_higher_levels": "1d8 (or 5) + your Constitution modifier per cleric level after 1st",
        "prof_armor": "Light armor, medium armor, shields",
        "prof_weapons": "Simple weapons",
        "prof_tools": "None",
        "prof_saving_throws": "Wisdom, Charisma",
        "prof_skills": "Choose two from History, Insight, Medicine, Persuasion, and Religion",
        "equipment": "You start with the following equipment, in addition to the equipment granted by your background: \n \n* (*a*) a mace or (*b*) a warhammer (if proficient) \n* (*a*) scale mail, (*b*) leather armor, or (*c*) chain mail (if proficient) \n* (*a*) a light crossbow and 20 bolts or (*b*) any simple weapon \n* (*a*) a priest's pack or (*b*) an explorer's pack \n* A shield and a holy symbol",
        "table": "| Level | Proficiency Bonus | Features                                                                | Cantrips Known | 1st | 2nd | 3rd | 4th | 5th | 6th | 7th | 8th | 9th | \n|-------|-------------------|-------------------------------------------------------------------------|----------------|-----|-----|-----|-----|-----|-----|-----|-----|-----| \n| 1st   | +2                | Spellcasting, Divine Domain                                             | 3              | 2   | -   | -   | -   | -   | -   | -   | -   | -   | \n| 2nd   | +2                | Channel Divinity (1/rest), Divine Domain Feature                        | 3              | 3   | -   | -   | -   | -   | -   | -   | -   | -   | \n| 3rd   | +2                | -                                                                       | 3              | 4   | 2   | -   | -   | -   | -   | -   | -   | -   | \n| 4th   | +2                | Ability Score Improvement                                               | 4              | 4   | 3   | -   | -   | -   | -   | -   | -   | -   | \n| 5th   | +3                | Destroy Undead (CR 1/2)                                                 | 4              | 4   | 3   | 2   | -   | -   | -   | -   | -   | -   | \n| 6th   | +3                | Channel Divinity (2/rest), Divine Domain Feature                        | 4              | 4   | 3   | 3   | -   | -   | -   | -   | -   | -   | \n| 7th   | +3                | -                                                                       | 4              | 4   | 3   | 3   | 1   | -   | -   | -   | -   | -   | \n| 8th   | +3                | Ability Score Improvement, Destroy Undead (CR 1), Divine Domain Feature | 4              | 4   | 3   | 3   | 2   | -   | -   | -   | -   | -   | \n| 9th   | +4                | -                                                                       | 4              | 4   | 3   | 3   | 3   | 1   | -   | -   | -   | -   | \n| 10th  | +4                | Divine Intervention                                                     | 5              | 4   | 3   | 3   | 3   | 2   | -   | -   | -   | -   | \n| 11th  | +4                | Destroy Undead (CR 2)                                                   | 5              | 4   | 3   | 3   | 3   | 2   | 1   | -   | -   | -   | \n| 12th  | +4                | Ability Score Improvement                                               | 5              | 4   | 3   | 3   | 3   | 2   | 1   | -   | -   | -   | \n| 13th  | +5                | -                                                                       | 5              | 4   | 3   | 3   | 3   | 2   | 1   | 1   | -   | -   | \n| 14th  | +5                | Destroy Undead (CR 3)                                                   | 5              | 4   | 3   | 3   | 3   | 2   | 1   | 1   | -   | -   | \n| 15th  | +5                | -                                                                       | 5              | 4   | 3   | 3   | 3   | 2   | 1   | 1   | 1   | -   | \n| 16th  | +5                | Ability Score Improvement                                               | 5              | 4   | 3   | 3   | 3   | 2   | 1   | 1   | 1   | -   | \n| 17th  | +6                | Destroy Undead (CR 4), Divine Domain Feature                            | 5              | 4   | 3   | 3   | 3   | 2   | 1   | 1   | 1   | 1   | \n| 18th  | +6                | Channel Divinity (3/rest)                                               | 5              | 4   | 3   | 3   | 3   | 3   | 1   | 1   | 1   | 1   | \n| 19th  | +6                | Ability Score Improvement                                               | 5              | 4   | 3   | 3   | 3   | 3   | 2   | 1   | 1   | 1   | \n| 20th  | +6                | Divine Intervention improvement                                         | 5              | 4   | 3   | 3   | 3   | 3   | 2   | 2   | 1   | 1   |",
        "spellcasting_ability": "Wisdom",
        "subtypes_name": "Domains",
        "archetypes": [
            {
                "name": "Life Domain",
                "slug": "life-domain",
                "desc": "The Life domain focuses on the vibrant positive energy-one of the fundamental forces of the universe-that sustains all life. The gods of life promote vitality and health through healing the sick and wounded, caring for those in need, and driving away the forces of death and undeath. Almost any non-evil deity can claim influence over this domain, particularly agricultural deities (such as Chauntea, Arawai, and Demeter), sun gods (such as Lathander, Pelor, and Re-Horakhty), gods of healing or endurance (such as Ilmater, Mishakal, Apollo, and Diancecht), and gods of home and community (such as Hestia, Hathor, and Boldrei). \n \n**Life Domain Spells (table)** \n \n| Cleric Level | Spells                               | \n|--------------|--------------------------------------| \n| 1st          | bless, cure wounds                   | \n| 3rd          | lesser restoration, spiritual weapon | \n| 5th          | beacon of hope, revivify             | \n| 7th          | death ward, guardian of faith        | \n| 9th          | mass cure wounds, raise dead         | \n \n##### Bonus Proficiency \n \nWhen you choose this domain at 1st level, you gain proficiency with heavy armor. \n \n##### Disciple of Life \n \nAlso starting at 1st level, your healing spells are more effective. Whenever you use a spell of 1st level or higher to restore hit points to a creature, the creature regains additional hit points equal to 2 + the spell's level. \n \n##### Channel Divinity: Preserve Life \n \nStarting at 2nd level, you can use your Channel Divinity to heal the badly injured. \n \nAs an action, you present your holy symbol and evoke healing energy that can restore a number of hit points equal to five times your cleric level. Choose any creatures within 30 feet of you, and divide those hit points among them. This feature can restore a creature to no more than half of its hit point maximum. You can't use this feature on an undead or a construct. \n \n##### Blessed Healer \n \nBeginning at 6th level, the healing spells you cast on others heal you as well. When you cast a spell of 1st level or higher that restores hit points to a creature other than you, you regain hit points equal to 2 + the spell's level. \n \n##### Divine Strike \n \nAt 8th level, you gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 radiant damage to the target. When you reach 14th level, the extra damage increases to 2d8. \n \n##### Supreme Healing \n \nStarting at 17th level, when you would normally roll one or more dice to restore hit points with a spell, you instead use the highest number possible for each die. For example, instead of restoring 2d6 hit points to a creature, you restore 12.",
                "document__slug": "wotc-srd",
                "document__title": "Systems Reference Document",
                "document__license_url": "http://open5e.com/legal"
            }
        ],
        "document__slug": "wotc-srd",
        "document__title": "Systems Reference Document",
        "document__license_url": "http://open5e.com/legal"
    },
    "druid": {
        "name": "Druid",
        "slug": "druid",
        "desc": "### Druidic \n \n"
                "You know Druidic, the secret language of druids. You can speak the language and use it to leave hidden messages. You and others who know this language automatically spot such a message. Others spot the message's presence with a successful DC 15 Wisdom (Perception) check but can't decipher it without magic. \n \n"
                "### Spellcasting \n \n"
                "Drawing on the divine essence of nature itself, you can cast spells to shape that essence to your will. \n \n"
                "#### Cantrips \n \n"
                "At 1st level, you know two cantrips of your choice from the druid spell list. You learn additional druid cantrips of your choice at higher levels, as shown in the Cantrips Known column of the Druid table. \n \n"
                "#### Preparing and Casting Spells \n \n"
                "The Druid table shows how many spell slots you have to cast your spells of 1st level and higher. To cast one of these druid spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest. \n \n"
                "You prepare the list of druid spells that are available for you to cast, choosing from the druid spell list. When you do so, choose a number of druid spells equal to your Wisdom modifier + your druid level (minimum of one spell). The spells must be of a level for which you have spell slots. \n \n"
                "For example, if you are a 3rd-level druid, you have four 1st-level and two 2nd-level spell slots. With a Wisdom of 16, your list of prepared spells can include six spells of 1st or 2nd level, in any combination. If you prepare the 1st-level spell *cure wounds,* you can cast it using a 1st-level or 2nd-level slot. Casting the spell doesn't remove it from your list of prepared spells. \n \n"
                "You can also change your list of prepared spells when you finish a long rest. Preparing a new list of druid spells requires time spent in prayer and meditation: at least 1 minute per spell level for each spell on your list. \n \n"
                "### Spellcasting Ability \n \n"
                "Wisdom is your spellcasting ability for your druid spells, since your magic draws upon your devotion and attunement to nature. You use your Wisdom whenever a spell refers to your spellcasting ability. In addition, you use your Wisdom modifier when setting the saving throw DC for a druid spell you cast and when making an attack roll with one. \n \n"
                "**Spell save DC** = 8 + your proficiency bonus + your Wisdom modifier \n \n"
                "**Spell attack modifier** = your proficiency bonus + your Wisdom modifier \n \n"
                "### Ritual Casting \n \n"
                "You can cast a druid spell as a ritual if that spell has the ritual tag and you have the spell prepared. \n \n"
                "#### Spellcasting Focus \n \n"
                "You can use a druidic focus (see chapter 5, “Equipment”) as a spellcasting focus for your druid spells. \n \n"
                "### Wild Shape \n \n"
                "Starting at 2nd level, you can use your action to magically assume the shape of a beast that you have seen before. You can use this feature twice. You regain expended uses when you finish a short or long rest. \n \n"
                "Your druid level determines the beasts you can transform into, as shown in the Beast Shapes table. At 2nd level, for example, you can transform into any beast that has a challenge rating of 1/4 or lower that doesn't have a flying or swimming speed. \n \n"
                "**Beast Shapes (table)** \n \n"
                "| Level | Max. CR | Limitations                 | Example     | \n"
                "|-------|---------|-----------------------------|-------------| \n"
                "| 2nd   | 1/4     | No flying or swimming speed | Wolf        | \n"
                "| 4th   | 1/2     | No flying speed             | Crocodile   | \n"
                "| 8th   | 1       | -                           | Giant eagle | \n \n"
                "You can stay in a beast shape for a number of hours equal to half your druid level (rounded down). You then revert to your normal form unless you expend another use of this feature. You can revert to your normal form earlier by using a bonus action on your turn. You automatically revert if you fall unconscious, drop to 0 hit points, or die. \n \n"
                "While you are transformed, the following rules apply: \n \n"
                "* Your game statistics are replaced by the statistics of the beast, but you retain your alignment, personality, and Intelligence, Wisdom, and Charisma scores. You also retain all of your skill and saving throw proficiencies, in addition to gaining those of the creature. If the creature has the same proficiency as you and the bonus in its stat block is higher than yours, use the creature's bonus instead of yours. If the creature has any legendary or lair actions, you can't use them. \n"
                "* When you transform, you assume the beast's hit points and Hit Dice. When you revert to your normal form, you return to the number of hit points you had before you transformed. However, if you revert as a result of dropping to 0 hit points, any excess damage carries over to your normal form. For example, if you take 10 damage in animal form and have only 1 hit point left, you revert and take 9 damage. As long as the excess damage doesn't reduce your normal form to 0 hit points, you aren't knocked unconscious. \n"
                "* You can't cast spells, and your ability to speak or take any action that requires hands is limited to the capabilities of your beast form. Transforming doesn't break your concentration on a spell you've already cast, however, or prevent you from taking actions that are part of a spell, such as *call lightning*, that you've already cast. \n"
                "* You retain the benefit of any features from your class, race, or other source and can use them if the new form is physically capable of doing so. However, you can't use any of your special senses, such as darkvision, unless your new form also has that sense. \n"
                "* You choose whether your equipment falls to the ground in your space, merges into your new form, or is worn by it. Worn equipment functions as normal, but the GM decides whether it is practical for the new form to wear a piece of equipment, based on the creature's shape and size. Your equipment doesn't change size or shape to match the new form, and any equipment that the new form can't wear must either fall to the ground or merge with it. Equipment that merges with the form has no effect until you leave the form. \n \n"
                "### Druid Circle \n \n"
                "At 2nd level, you choose to identify with a circle of druids: the Circle of the Land or the Circle of the Moon, both detailed at the end of the class description. Your choice grants you features at 2nd level and again at 6th, 10th, and 14th level. \n \n"
                "### Ability Score Improvement \n \n"
                "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature. \n \n"
                "### Timeless Body \n \n"
                "Starting at 18th level, the primal magic that you wield causes you to age more slowly. For every 10 years that pass, your body ages only 1 year. \n \n"
                "### Beast Spells \n \n"
                "Beginning at 18th level, you can cast many of your druid spells in any shape you assume using Wild Shape. You can perform the somatic and verbal components of a druid spell while in a beast shape, but you aren't able to provide material components. \n \n"
                "### Archdruid \n \n"
                "At 20th level, you can use your Wild Shape an unlimited number of times. \n \n"
                "Additionally, you can ignore the verbal and somatic components of your druid spells, as well as any material components that lack a cost and aren't consumed by a spell. You gain this benefit in both your normal shape and your beast shape from Wild Shape.",
        "hit_dice": "1d8",
        "hp_at_1st_level": "8 + your Constitution modifier",
        "hp_at_higher_levels": "1d8 (or 5) + your Constitution modifier per druid level after 1st",
        "prof_armor": "Light armor, medium armor, shields (druids will not wear armor or use shields made of metal)",
        "prof_weapons": "Clubs, daggers, darts, javelins, maces, quarterstaffs, scimitars, sickles, slings, spears",
        "prof_tools": "Herbalism kit",
        "prof_saving_throws": "Intelligence, Wisdom",
        "prof_skills": "Choose two from Arcana, Animal Handling, Insight, Medicine, Nature, Perception, Religion, and Survival",
        "equipment": "You start with the following equipment, in addition to the equipment granted by your background: \n \n"
                     "* (*a*) a wooden shield or (*b*) any simple weapon \n"
                     "* (*a*) a scimitar or (*b*) any simple melee weapon \n"
                     "* Leather armor, an explorer's pack, and a druidic focus",
        "table": "| Level | Proficiency Bonus | Features                                          | Cantrips Known | 1st | 2nd | 3rd | 4th | 5th | 6th | 7th | 8th | 9th | \n"
                 "|-------|-------------------|---------------------------------------------------|----------------|-----|-----|-----|-----|-----|-----|-----|-----|-----| \n"
                 "| 1st   | +2                | Druidic, Spellcasting                             | 2              | 2   | -   | -   | -   | -   | -   | -   | -   | -   | \n"
                 "| 2nd   | +2                | Wild Shape, Druid Circle                          | 2              | 3   | -   | -   | -   | -   | -   | -   | -   | -   | \n"
                 "| 3rd   | +2                | -                                                 | 2              | 4   | 2   | -   | -   | -   | -   | -   | -   | -   | \n"
                 "| 4th   | +2                | Wild Shape Improvement, Ability Score Improvement | 3              | 4   | 3   | -   | -   | -   | -   | -   | -   | -   | \n"
                 "| 5th   | +3                | -                                                 | 3              | 4   | 3   | 2   | -   | -   | -   | -   | -   | -   | \n"
                 "| 6th   | +3                | Druid Circle feature                              | 3              | 4   | 3   | 3   | -   | -   | -   | -   | -   | -   | \n"
                 "| 7th   | +3                | -                                                 | 3              | 4   | 3   | 3   | 1   | -   | -   | -   | -   | -   | \n"
                 "| 8th   | +3                | Wild Shape Improvement, Ability Score Improvement | 3              | 4   | 3   | 3   | 2   | -   | -   | -   | -   | -   | \n"
                 "| 9th   | +4                | -                                                 | 3              | 4   | 3   | 3   | 3   | 1   | -   | -   | -   | -   | \n"
                 "| 10th  | +4                | Druid Circle feature                              | 4              | 4   | 3   | 3   | 3   | 2   | -   | -   | -   | -   | \n"
                 "| 11th  | +4                | -                                                 | 4              | 4   | 3   | 3   | 3   | 2   | 1   | -   | -   | -   | \n"
                 "| 12th  | +4                | Ability Score Improvement                         | 4              | 4   | 3   | 3   | 3   | 2   | 1   | -   | -   | -   | \n"
                 "| 13th  | +5                | -                                                 | 4              | 4   | 3   | 3   | 3   | 2   | 1   | 1   | -   | -   | \n"
                 "| 14th  | +5                | Druid Circle feature                              | 4              | 4   | 3   | 3   | 3   | 2   | 1   | 1   | -   | -   | \n"
                 "| 15th  | +5                | -                                                 | 4              | 4   | 3   | 3   | 3   | 2   | 1   | 1   | 1   | -   | \n"
                 "| 16th  | +5                | Ability Score Improvement                         | 4              | 4   | 3   | 3   | 3   | 2   | 1   | 1   | 1   | -   | \n"
                 "| 17th  | +6                | -                                                 | 4              | 4   | 3   | 3   | 3   | 2   | 1   | 1   | 1   | 1   | \n"
                 "| 18th  | +6                | Timeless Body, Beast Spells                       | 4              | 4   | 3   | 3   | 3   | 3   | 1   | 1   | 1   | 1   | \n"
                 "| 19th  | +6                | Ability Score Improvement                         | 4              | 4   | 3   | 3   | 3   | 3   | 2   | 1   | 1   | 1   | \n"
                 "| 20th  | +6                | Archdruid                                         | 4              | 4   | 3   | 3   | 3   | 3   | 2   | 2   | 1   | 1   | ",
        "spellcasting_ability": "Wisdom",
        "subtypes_name": "Circles",
        "archetypes": [
            {
                "name": "Circle of the Land",
                "slug": "circle-of-the-land",
                "desc": "The Circle of the Land is made up of mystics and sages who safeguard ancient knowledge and rites through a vast oral tradition. These druids meet within sacred circles of trees or standing stones to whisper primal secrets in Druidic. The circle's wisest members preside as the chief priests of communities that hold to the Old Faith and serve as advisors to the rulers of those folk. As a member of this circle, your magic is influenced by the land where you were initiated into the circle's mysterious rites. \n \n"
                        "##### Bonus Cantrip \n \n"
                        "When you choose this circle at 2nd level, you learn one additional druid cantrip of your choice. \n \n"
                        "##### Natural Recovery \n \n"
                        "Starting at 2nd level, you can regain some of your magical energy by sitting in meditation and communing with nature. During a short rest, you choose expended spell slots to recover. The spell slots can have a combined level that is equal to or less than half your druid level \n"
                        "(rounded up), and none of the slots can be 6th level or higher. You can't use this feature again until you finish a long rest. \n \n"
                        "For example, when you are a 4th-level druid, you can recover up to two levels worth of spell slots. You can recover either a 2nd-level slot or two 1st-level slots. \n \n"
                        "##### Circle Spells \n \n"
                        "Your mystical connection to the land infuses you with the ability to cast certain spells. At 3rd, 5th, 7th, and 9th level you gain access to circle spells connected to the land where you became a druid. Choose that land-arctic, coast, desert, forest, grassland, mountain, or swamp-and consult the associated list of spells. \n \n"
                        "Once you gain access to a circle spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you gain access to a spell that doesn't appear on the druid spell list, the spell is nonetheless a druid spell for you. \n \n"
                        "**Arctic (table)** \n \n"
                        "| Druid Level | Circle Spells                     | \n"
                        "|-------------|-----------------------------------| \n"
                        "| 3rd         | hold person, spike growth         | \n"
                        "| 5th         | sleet storm, slow                 | \n"
                        "| 7th         | freedom of movement, ice storm    | \n"
                        "| 9th         | commune with nature, cone of cold | \n \n"
                        "**Coast (table)** \n \n"
                        "| Druid Level | Circle Spells                      | \n"
                        "|-------------|------------------------------------| \n"
                        "| 3rd         | mirror image, misty step           | \n"
                        "| 5th         | water breathing, water walk        | \n"
                        "| 7th         | control water, freedom of movement | \n"
                        "| 9th         | conjure elemental, scrying         | \n \n"
                        "**Desert (table)** \n \n"
                        "| Druid Level | Circle Spells                                 | \n"
                        "|-------------|-----------------------------------------------| \n"
                        "| 3rd         | blur, silence                                 | \n"
                        "| 5th         | create food and water, protection from energy | \n"
                        "| 7th         | blight, hallucinatory terrain                 | \n"
                        "| 9th         | insect plague, wall of stone                  | \n \n"
                        "**Forest (table)** \n \n"
                        "| Druid Level | Circle Spells                    | \n"
                        "|-------------|----------------------------------| \n"
                        "| 3rd         | barkskin, spider climb           | \n"
                        "| 5th         | call lightning, plant growth     | \n"
                        "| 7th         | divination, freedom of movement  | \n"
                        "| 9th         | commune with nature, tree stride | \n \n"
                        "**Grassland (table)** \n \n"
                        "| Druid Level | Circle Spells                    | \n"
                        "|-------------|----------------------------------| \n"
                        "| 3rd         | invisibility, pass without trace | \n"
                        "| 5th         | daylight, haste                  | \n"
                        "| 7th         | divination, freedom of movement  | \n"
                        "| 9th         | dream, insect plague             | \n \n"
                        "**Mountain (table)** \n \n"
                        "| Druid Level | Circle Spells                   | \n"
                        "|-------------|---------------------------------| \n"
                        "| 3rd         | spider climb, spike growth      | \n"
                        "| 5th         | lightning bolt, meld into stone | \n"
                        "| 7th         | stone shape, stoneskin          | \n"
                        "| 9th         | passwall, wall of stone         | \n \n"
                        "**Swamp (table)** \n \n"
                        "| Druid Level | Circle Spells                        | \n"
                        "|-------------|--------------------------------------| \n"
                        "| 3rd         | acid arrow, darkness                 | \n"
                        "| 5th         | water walk, stinking cloud           | \n"
                        "| 7th         | freedom of movement, locate creature | \n"
                        "| 9th         | insect plague, scrying               | \n \n"
                        "##### Land's Stride \n \n"
                        "Starting at 6th level, moving through nonmagical difficult terrain costs you no extra movement. You can also pass through nonmagical plants without being slowed by them and without taking damage from them if they have thorns, spines, or a similar hazard. \n \n"
                        "In addition, you have advantage on saving throws against plants that are magically created or manipulated to impede movement, such those created by the *entangle* spell. \n \n"
                        "##### Nature's Ward \n \n"
                        "When you reach 10th level, you can't be charmed or frightened by elementals or fey, and you are immune to poison and disease. \n \n"
                        "##### Nature's Sanctuary \n \n"
                        "When you reach 14th level, creatures of the natural world sense your connection to nature and become hesitant to attack you. When a beast or plant creature attacks you, that creature must make a Wisdom saving throw against your druid spell save DC. On a failed save, the creature must choose a different target, or the attack automatically misses. On a successful save, the creature is immune to this effect for 24 hours. \n \n"
                        "The creature is aware of this effect before it makes its attack against you. \n \n"
                        "> ### Sacred Plants and Wood \n> \n"
                        "> A druid holds certain plants to be sacred, particularly alder, ash, birch, elder, hazel, holly, juniper, mistletoe, oak, rowan, willow, and yew. Druids often use such plants as part of a spellcasting focus, incorporating lengths of oak or yew or sprigs of mistletoe. \n> \n"
                        "> Similarly, a druid uses such woods to make other objects, such as weapons and shields. Yew is associated with death and rebirth, so weapon handles for scimitars or sickles might be fashioned from it. Ash is associated with life and oak with strength. These woods make excellent hafts or whole weapons, such as clubs or quarterstaffs, as well as shields. Alder is associated with air, and it might be used for thrown weapons, such as darts or javelins. \n> \n"
                        "> Druids from regions that lack the plants described here have chosen other plants to take on similar uses. For instance, a druid of a desert region might value the yucca tree and cactus plants. \n \n"
                        "> ### Druids and the Gods \n> \n"
                        "> Some druids venerate the forces of nature themselves, but most druids are devoted to one of the many nature deities worshiped in the multiverse (the lists of gods in appendix B include many such deities). The worship of these deities is often considered a more ancient tradition than the faiths of clerics and urbanized peoples.",
                "document__slug": "wotc-srd",
                "document__title": "Systems Reference Document",
                "document__license_url": "http://open5e.com/legal"
            }
        ],
        "document__slug": "wotc-srd",
        "document__title": "Systems Reference Document",
        "document__license_url": "http://open5e.com/legal"
    },
    "fighter": {
        "name": "Fighter",
        "slug": "fighter",
        "desc": "### Fighting Style \n \n"
                "You adopt a particular style of fighting as your specialty. Choose one of the following options. You can't take a Fighting Style option more than once, even if you later get to choose again. \n \n"
                "#### Archery \n \n"
                "You gain a +2 bonus to attack rolls you make with ranged weapons. \n \n"
                "#### Defense \n \n"
                "While you are wearing armor, you gain a +1 bonus to AC. \n \n"
                "#### Dueling \n \n"
                "When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon. \n \n"
                "#### Great Weapon Fighting \n \n"
                "When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll, even if the new roll is a 1 or a 2. The weapon must have the two-handed or versatile property for you to gain this benefit. \n \n"
                "#### Protection \n \n"
                "When a creature you can see attacks a target other than you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield. \n \n"
                "#### Two-Weapon Fighting \n \n"
                "When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack. \n \n"
                "### Second Wind \n \n"
                "You have a limited well of stamina that you can draw on to protect yourself from harm. On your turn, you can use a bonus action to regain hit points equal to 1d10 + your fighter level. Once you use this feature, you must finish a short or long rest before you can use it again. \n \n"
                "### Action Surge \n \n"
                "Starting at 2nd level, you can push yourself beyond your normal limits for a moment. On your turn, you can take one additional action on top of your regular action and a possible bonus action. \n \n"
                "Once you use this feature, you must finish a short or long rest before you can use it again. Starting at 17th level, you can use it twice before a rest, but only once on the same turn. \n \n"
                "### Martial Archetype \n \n"
                "At 3rd level, you choose an archetype that you strive to emulate in your combat styles and techniques. Choose Champion, Battle Master, or Eldritch Knight, all detailed at the end of the class description. The archetype you choose grants you features at 3rd level and again at 7th, 10th, 15th, and 18th level. \n \n"
                "### Ability Score Improvement \n \n"
                "When you reach 4th level, and again at 6th, 8th, 12th, 14th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature. \n \n"
                "### Extra Attack \n \n"
                "Beginning at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn. \n \n"
                "The number of attacks increases to three when you reach 11th level in this class and to four when you reach 20th level in this class. \n \n"
                "### Indomitable \n \n"
                "Beginning at 9th level, you can reroll a saving throw that you fail. If you do so, you must use the new roll, and you can't use this feature again until you finish a long rest. \n \n"
                "You can use this feature twice between long rests starting at 13th level and three times between long rests starting at 17th level.\n \n"
                "### Martial Archetypes \n \n"
                "Different fighters choose different approaches to perfecting their fighting prowess. The martial archetype you choose to emulate reflects your approach.",
        "hit_dice": "1d10",
        "hp_at_1st_level": "10 + your Constitution modifier",
        "hp_at_higher_levels": "1d10 (or 6) + your Constitution modifier per fighter level after 1st",
        "prof_armor": "All armor, shields",
        "prof_weapons": "Simple weapons, martial weapons",
        "prof_tools": "None",
        "prof_saving_throws": "Strength, Constitution",
        "prof_skills": "Choose two skills from Acrobatics, Animal, Handling, Athletics, History, Insight, Intimidation, Perception, and Survival",
        "equipment": "You start with the following equipment, in addition to the equipment granted by your background: \n \n"
                     "* (*a*) chain mail or (*b*) leather armor, longbow, and 20 arrows \n"
                     "* (*a*) a martial weapon and a shield or (*b*) two martial weapons \n"
                     "* (*a*) a light crossbow and 20 bolts or (*b*) two handaxes \n"
                     "* (*a*) a dungeoneer's pack or (*b*) an explorer's pack",
        "table": "| Level | Proficiency Bonus | Features                                          | \n"
                 "|-------|-------------------|---------------------------------------------------| \n"
                 "| 1st   | +2                | Fighting Style, Second Wind                       | \n"
                 "| 2nd   | +2                | Action Surge (one use)                            | \n"
                 "| 3rd   | +2                | Martial Archetype                                 | \n"
                 "| 4th   | +2                | Ability Score Improvement                         | \n"
                 "| 5th   | +3                | Extra Attack                                      | \n"
                 "| 6th   | +3                | Ability Score Improvement                         | \n"
                 "| 7th   | +3                | Martial Archetype Feature                         | \n"
                 "| 8th   | +3                | Ability Score Improvement                         | \n"
                 "| 9th   | +4                | Indomitable (one use)                             | \n"
                 "| 10th  | +4                | Martial Archetype Feature                         | \n"
                 "| 11th  | +4                | Extra Attack (2)                                  | \n"
                 "| 12th  | +4                | Ability Score Improvement                         | \n"
                 "| 13th  | +5                | Indomitable (two uses)                            | \n"
                 "| 14th  | +5                | Ability Score Improvement                         | \n"
                 "| 15th  | +5                | Martial Archetype Feature                         | \n"
                 "| 16th  | +5                | Ability Score Improvement                         | \n"
                 "| 17th  | +6                | Action Surge (two uses), Indomitable (three uses) | \n"
                 "| 18th  | +6                | Martial Archetype Feature                         | \n"
                 "| 19th  | +6                | Ability Score Improvement                         | \n"
                 "| 20th  | +6                | Extra Attack (3)                                  | ",
        "spellcasting_ability": "",
        "subtypes_name": "Martial Archetypes",
        "archetypes": [
            {
                "name": "Champion",
                "slug": "champion",
                "desc": "The archetypal Champion focuses on the development of raw physical power honed to deadly perfection. Those who model themselves on this archetype combine rigorous training with physical excellence to deal devastating blows. \n \n"
                        "##### Improved Critical \n \n"
                        "Beginning when you choose this archetype at 3rd level, your weapon attacks score a critical hit on a roll of 19 or 20. \n \n"
                        "##### Remarkable Athlete \n \n"
                        "Starting at 7th level, you can add half your proficiency bonus (round up) to any Strength, Dexterity, or Constitution check you make that doesn't already use your proficiency bonus. \n \n"
                        "In addition, when you make a running long jump, the distance you can cover increases by a number of feet equal to your Strength modifier. \n \n"
                        "##### Additional Fighting Style \n \n"
                        "At 10th level, you can choose a second option from the Fighting Style class feature. \n \n"
                        "##### Superior Critical \n \n"
                        "Starting at 15th level, your weapon attacks score a critical hit on a roll of 18-20. \n \n"
                        "##### Survivor \n \n"
                        "At 18th level, you attain the pinnacle of resilience in battle. At the start of each of your turns, you regain hit points equal to 5 + your Constitution modifier if you have no more than half of your hit points left. You don't gain this benefit if you have 0 hit points.",
                "document__slug": "wotc-srd",
                "document__title": "Systems Reference Document",
                "document__license_url": "http://open5e.com/legal"
            }
        ],
        "document__slug": "wotc-srd",
        "document__title": "Systems Reference Document",
        "document__license_url": "http://open5e.com/legal"
    },
    "monk": {
        "name": "Monk",
        "slug": "monk",
        "desc": "### Unarmored Defense \n \n"
                "Beginning at 1st level, while you are wearing no armor and not wielding a shield, your AC equals 10 + your Dexterity modifier + your Wisdom modifier. \n \n"
                "### Martial Arts \n \n"
                "At 1st level, your practice of martial arts gives you mastery of combat styles that use unarmed strikes and monk weapons, which are shortswords and any simple melee weapons that don't have the two- handed or heavy property. \n \n"
                "You gain the following benefits while you are unarmed or wielding only monk weapons and you aren't wearing armor or wielding a shield: \n \n"
                "* You can use Dexterity instead of Strength for the attack and damage rolls of your unarmed strikes and monk weapons. \n"
                "* You can roll a d4 in place of the normal damage of your unarmed strike or monk weapon. This die changes as you gain monk levels, as shown in the Martial Arts column of the Monk table. \n"
                "* When you use the Attack action with an unarmed strike or a monk weapon on your turn, you can make one unarmed strike as a bonus action. For example, if you take the Attack action and attack with a quarterstaff, you can also make an unarmed strike as a bonus action, assuming you haven't already taken a bonus action this turn. \n \n"
                "Certain monasteries use specialized forms of the monk weapons. For example, you might use a club that is two lengths of wood connected by a short chain (called a nunchaku) or a sickle with a shorter, straighter blade (called a kama). Whatever name you use for a monk weapon, you can use the game statistics provided for the weapon. \n \n"
                "### Ki \n \n"
                "Starting at 2nd level, your training allows you to harness the mystic energy of ki. Your access to this energy is represented by a number of ki points. Your monk level determines the number of points you have, as shown in the Ki Points column of the Monk table. \n \n"
                "You can spend these points to fuel various ki features. You start knowing three such features: Flurry of Blows, Patient Defense, and Step of the Wind. You learn more ki features as you gain levels in this class. \n \n"
                "When you spend a ki point, it is unavailable until you finish a short or long rest, at the end of which you draw all of your expended ki back into yourself. You must spend at least 30 minutes of the rest meditating to regain your ki points. \n \n"
                "Some of your ki features require your target to make a saving throw to resist the feature's effects. The saving throw DC is calculated as follows: \n \n"
                "**Ki save DC** = 8 + your proficiency bonus + your Wisdom modifier \n \n"
                "#### Flurry of Blows \n \n"
                "Immediately after you take the Attack action on your turn, you can spend 1 ki point to make two unarmed strikes as a bonus action. \n \n"
                "#### Patient Defense \n \n"
                "You can spend 1 ki point to take the Dodge action as a bonus action on your turn. \n \n"
                "#### Step of the Wind \n \n"
                "You can spend 1 ki point to take the Disengage or Dash action as a bonus action on your turn, and your jump distance is doubled for the turn. \n \n"
                "### Unarmored Movement \n \n"
                "Starting at 2nd level, your speed increases by 10 feet while you are not wearing armor or wielding a shield. This bonus increases when you reach certain monk levels, as shown in the Monk table. \n \n"
                "At 9th level, you gain the ability to move along vertical surfaces and across liquids on your turn without falling during the move. \n \n"
                "### Monastic Tradition \n \n"
                "When you reach 3rd level, you commit yourself to a monastic tradition: the Way of the Open Hand, the Way of Shadow, or the Way of the Four Elements, all detailed at the end of the class description. Your tradition grants you features at 3rd level and again at 6th, 11th, and 17th level. \n \n"
                "### Deflect Missiles \n \n"
                "Starting at 3rd level, you can use your reaction to deflect or catch the missile when you are hit by a ranged weapon attack. When you do so, the damage you take from the attack is reduced by 1d10 + your Dexterity modifier + your monk level. \n \n"
                "If you reduce the damage to 0, you can catch the missile if it is small enough for you to hold in one hand and you have at least one hand free. If you catch a missile in this way, you can spend 1 ki point to make a ranged attack with the weapon or piece of ammunition you just caught, as part of the same reaction. You make this attack with proficiency, regardless of your weapon proficiencies, and the missile counts as a monk weapon for the attack, which has a normal range of 20 feet and a long range of 60 feet. \n \n"
                "### Ability Score Improvement \n \n"
                "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature. \n \n"
                "### Slow Fall \n \n"
                "Beginning at 4th level, you can use your reaction when you fall to reduce any falling damage you take by an amount equal to five times your monk level. \n \n"
                "### Extra Attack \n \n"
                "Beginning at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn. \n \n"
                "### Stunning Strike \n \n"
                "Starting at 5th level, you can interfere with the flow of ki in an opponent's body. When you hit another creature with a melee weapon attack, you can spend 1 ki point to attempt a stunning strike. The target must succeed on a Constitution saving throw or be stunned until the end of your next turn. \n \n"
                "### Ki-Empowered Strikes \n \n"
                "Starting at 6th level, your unarmed strikes count as magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage. \n \n"
                "### Evasion \n \n"
                "At 7th level, your instinctive agility lets you dodge out of the way of certain area effects, such as a blue dragon's lightning breath or a *fireball* spell. When you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on the saving throw, and only half damage if you fail. \n \n"
                "### Stillness of Mind \n \n"
                "Starting at 7th level, you can use your action to end one effect on yourself that is causing you to be charmed or frightened. \n \n"
                "### Purity of Body \n \n"
                "At 10th level, your mastery of the ki flowing through you makes you immune to disease and poison. \n \n"
                "### Tongue of the Sun and Moon \n \n"
                "Starting at 13th level, you learn to touch the ki of other minds so that you understand all spoken languages. Moreover, any creature that can understand a language can understand what you say. \n \n"
                "### Diamond Soul \n \n"
                "Beginning at 14th level, your mastery of ki grants you proficiency in all saving throws. \n \n"
                "Additionally, whenever you make a saving throw and fail, you can spend 1 ki point to reroll it and take the second result. \n \n"
                "### Timeless Body \n \n"
                "At 15th level, your ki sustains you so that you suffer none of the frailty of old age, and you can't be aged magically. You can still die of old age, however. In addition, you no longer need food or water. \n \n"
                "### Empty Body \n \n"
                "Beginning at 18th level, you can use your action to spend 4 ki points to become invisible for 1 minute. During that time, you also have resistance to all damage but force damage. \n \n"
                "Additionally, you can spend 8 ki points to cast the *astral projection* spell, without needing material components. When you do so, you can't take any other creatures with you. \n \n"
                "### Perfect Self \n \n"
                "At 20th level, when you roll for initiative and have no ki points remaining, you regain 4 ki points. \n \n"
                "### Monastic Traditions \n \n"
                "Three traditions of monastic pursuit are common in the monasteries scattered across the multiverse. Most monasteries practice one tradition exclusively, but a few honor the three traditions and instruct each monk according to his or her aptitude and interest. All three traditions rely on the same basic techniques, diverging as the student grows more adept. Thus, a monk need choose a tradition only upon reaching 3rd level.",
        "hit_dice": "1d8",
        "hp_at_1st_level": "8 + your Constitution modifier",
        "hp_at_higher_levels": "1d8 (or 5) + your Constitution modifier per monk level after 1st",
        "prof_armor": "None",
        "prof_weapons": "Simple weapons, shortswords",
        "prof_tools": "Choose one type of artisan's tools or one musical instrument",
        "prof_saving_throws": "Strength, Dexterity",
        "prof_skills": "Choose two from Acrobatics, Athletics, History, Insight, Religion, and Stealth",
        "equipment": "You start with the following equipment, in addition to the equipment granted by your background: \n \n"
                     "* (*a*) a shortsword or (*b*) any simple weapon \n"
                     "* (*a*) a dungeoneer's pack or (*b*) an explorer's pack \n"
                     "* 10 darts",
        "table": "| Level | Proficiency Bonus | Martial Arts | Ki Points | Unarmored Movement | Features                                         | \n"
                 "|-------|-------------------|--------------|-----------|--------------------|--------------------------------------------------| \n"
                 "| 1st   | +2                | 1d4          | -         | -                  | Unarmored Defense, Martial Arts                  | \n"
                 "| 2nd   | +2                | 1d4          | 2         | +10 ft.            | Ki, Unarmored Movement                           | \n"
                 "| 3rd   | +2                | 1d4          | 3         | +10 ft.            | Monastic Tradition, Deflect Missiles             | \n"
                 "| 4th   | +2                | 1d4          | 4         | +10 ft.            | Ability Score Improvement, Slow Fall             | \n"
                 "| 5th   | +3                | 1d6          | 5         | +10 ft.            | Extra Attack, Stunning Strike                    | \n"
                 "| 6th   | +3                | 1d6          | 6         | +15 ft.            | Ki-Empowered Strikes, Monastic Tradition Feature | \n"
                 "| 7th   | +3                | 1d6          | 7         | +15 ft.            | Evasion, Stillness of Mind                       | \n"
                 "| 8th   | +3                | 1d6          | 8         | +15 ft.            | Ability Score Improvement                        | \n"
                 "| 9th   | +4                | 1d6          | 9         | +15 ft.            | Unarmored Movement improvement                   | \n"
                 "| 10th  | +4                | 1d6          | 10        | +20 ft.            | Purity of Body                                   | \n"
                 "| 11th  | +4                | 1d8          | 11        | +20 ft.            | Monastic Tradition Feature                       | \n"
                 "| 12th  | +4                | 1d8          | 12        | +20 ft.            | Ability Score Improvement                        | \n"
                 "| 13th  | +5                | 1d8          | 13        | +20 ft.            | Tongue of the Sun and Moon                       | \n"
                 "| 14th  | +5                | 1d8          | 14        | +25 ft.            | Diamond Soul                                     | \n"
                 "| 15th  | +5                | 1d8          | 15        | +25 ft.            | Timeless Body                                    | \n"
                 "| 16th  | +5                | 1d8          | 16        | +25 ft.            | Ability Score Improvement                        | \n"
                 "| 17th  | +6                | 1d10         | 17        | +25 ft.            | Monastic Tradition Feature                       | \n"
                 "| 18th  | +6                | 1d10         | 18        | +30 ft.            | Empty Body                                       | \n"
                 "| 19th  | +6                | 1d10         | 19        | +30 ft.            | Ability Score Improvement                        | \n"
                 "| 20th  | +6                | 1d10         | 20        | +30 ft.            | Perfect Self                                     |",
        "spellcasting_ability": "",
        "subtypes_name": "Monastic Traditions",
        "archetypes": [
            {
                "name": "Way of the Open Hand",
                "slug": "way-of-the-open-hand",
                "desc": "Monks of the Way of the Open Hand are the ultimate masters of martial arts combat, whether armed or unarmed. They learn techniques to push and trip their opponents, manipulate ki to heal damage to their bodies, and practice advanced meditation that can protect them from harm. \n \n"
                        "##### Open Hand Technique \n \n"
                        "Starting when you choose this tradition at 3rd level, you can manipulate your enemy's ki when you harness your own. Whenever you hit a creature with one of the attacks granted by your Flurry of Blows, you can impose one of the following effects on that target: \n"
                        "* It must succeed on a Dexterity saving throw or be knocked prone. \n"
                        "* It must make a Strength saving throw. If it fails, you can push it up to 15 feet away from you. \n"
                        "* It can't take reactions until the end of your next turn. \n \n"
                        "##### Wholeness of Body \n \n"
                        "At 6th level, you gain the ability to heal yourself. As an action, you can regain hit points equal to three times your monk level. You must finish a long rest before you can use this feature again. \n \n"
                        "##### Tranquility \n \n"
                        "Beginning at 11th level, you can enter a special meditation that surrounds you with an aura of peace. At the end of a long rest, you gain the effect of a *sanctuary* spell that lasts until the start of your next long rest (the spell can end early as normal). The saving throw DC for the spell equals 8 + your Wisdom modifier + your proficiency bonus. \n \n"
                        "##### Quivering Palm \n \n"
                        "At 17th level, you gain the ability to set up lethal vibrations in someone's body. When you hit a creature with an unarmed strike, you can spend 3 ki points to start these imperceptible vibrations, which last for a number of days equal to your monk level. The vibrations are harmless unless you use your action to end them. To do so, you and the target must be on the same plane of existence. When you use this action, the creature must make a Constitution saving throw. If it fails, it is reduced to 0 hit points. If it succeeds, it takes 10d10 necrotic damage. \n \n"
                        "You can have only one creature under the effect of this feature at a time. You can choose to end the vibrations harmlessly without using an action.",
                "document__slug": "wotc-srd",
                "document__title": "Systems Reference Document",
                "document__license_url": "http://open5e.com/legal"
            }
        ],
        "document__slug": "wotc-srd",
        "document__title": "Systems Reference Document",
        "document__license_url": "http://open5e.com/legal"
    },
    "paladin": {
        "name": "Paladin",
        "slug": "paladin",
        "desc": "### Divine Sense \n \n"
                "The presence of strong evil registers on your senses like a noxious odor, and powerful good rings like heavenly music in your ears. As an action, you can open your awareness to detect such forces. Until the end of your next turn, you know the location of any celestial, fiend, or undead within 60 feet of you that is not behind total cover. You know the type (celestial, fiend, or undead) of any being whose presence you sense, but not its identity (the vampire \n \n"
                "Count Strahd von Zarovich, for instance). Within the same radius, you also detect the presence of any place or object that has been consecrated or desecrated, as with the *hallow* spell. \n \n"
                "You can use this feature a number of times equal to 1 + your Charisma modifier. When you finish a long rest, you regain all expended uses. \n \n"
                "### Lay on Hands \n \n"
                "Your blessed touch can heal wounds. You have a pool of healing power that replenishes when you take a long rest. With that pool, you can restore a total number of hit points equal to your paladin level × 5. \n \n"
                "As an action, you can touch a creature and draw power from the pool to restore a number of hit points to that creature, up to the maximum amount remaining in your pool. \n \n"
                "Alternatively, you can expend 5 hit points from your pool of healing to cure the target of one disease or neutralize one poison affecting it. You can cure multiple diseases and neutralize multiple poisons with a single use of Lay on Hands, expending hit points separately for each one. \n \n"
                "This feature has no effect on undead and constructs. \n \n"
                "### Fighting Style \n \n"
                "At 2nd level, you adopt a style of fighting as your specialty. Choose one of the following options. You can't take a Fighting Style option more than once, even if you later get to choose again. \n \n"
                "#### Defense \n \n"
                "While you are wearing armor, you gain a +1 bonus to AC. \n \n"
                "#### Dueling \n \n"
                "When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon. \n \n"
                "#### Great Weapon Fighting \n \n"
                "When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll. The weapon must have the two-handed or versatile property for you to gain this benefit. \n \n"
                "#### Protection \n \n"
                "When a creature you can see attacks a target other than you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield. \n \n"
                "### Spellcasting \n \n"
                "By 2nd level, you have learned to draw on divine magic through meditation and prayer to cast spells as a cleric does. \n \n"
                "#### Preparing and Casting Spells \n \n"
                "The Paladin table shows how many spell slots you have to cast your spells. To cast one of your paladin spells of 1st level or higher, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest. \n \n"
                "You prepare the list of paladin spells that are available for you to cast, choosing from the paladin spell list. When you do so, choose a number of paladin spells equal to your Charisma modifier + half your paladin level, rounded down (minimum of one spell). The spells must be of a level for which you have spell slots. \n \n"
                "For example, if you are a 5th-level paladin, you have four 1st-level and two 2nd-level spell slots. With a Charisma of 14, your list of prepared spells can include four spells of 1st or 2nd level, in any combination. If you prepare the 1st-level spell *cure wounds,* you can cast it using a 1st-level or a 2nd- level slot. Casting the spell doesn't remove it from your list of prepared spells. \n \n"
                "You can change your list of prepared spells when you finish a long rest. Preparing a new list of paladin spells requires time spent in prayer and meditation: at least 1 minute per spell level for each spell on your list. \n \n"
                "#### Spellcasting Ability \n \n"
                "Charisma is your spellcasting ability for your paladin spells, since their power derives from the strength of your convictions. You use your Charisma whenever a spell refers to your spellcasting ability. In addition, you use your Charisma modifier when setting the saving throw DC for a paladin spell you cast and when making an attack roll with one. \n \n"
                "**Spell save DC** = 8 + your proficiency bonus + your Charisma modifier \n \n"
                "**Spell attack modifier** = your proficiency bonus + your Charisma modifier \n \n"
                "#### Spellcasting Focus \n \n"
                "You can use a holy symbol as a spellcasting focus for your paladin spells. \n \n"
                "### Divine Smite \n \n"
                "Starting at 2nd level, when you hit a creature with a melee weapon attack, you can expend one spell slot to deal radiant damage to the target, in addition to the weapon's damage. The extra damage is 2d8 for a 1st-level spell slot, plus 1d8 for each spell level higher than 1st, to a maximum of 5d8. The damage increases by 1d8 if the target is an undead or a fiend. \n \n"
                "### Divine Health \n \n"
                "By 3rd level, the divine magic flowing through you makes you immune to disease. \n \n"
                "### Sacred Oath \n \n"
                "When you reach 3rd level, you swear the oath that binds you as a paladin forever. Up to this time you have been in a preparatory stage, committed to the path but not yet sworn to it. Now you choose the Oath of Devotion, the Oath of the Ancients, or the Oath of Vengeance, all detailed at the end of the class description. \n \n"
                "Your choice grants you features at 3rd level and again at 7th, 15th, and 20th level. Those features include oath spells and the Channel Divinity feature. \n \n"
                "#### Oath Spells \n \n"
                "Each oath has a list of associated spells. You gain access to these spells at the levels specified in the oath description. Once you gain access to an oath spell, you always have it prepared. Oath spells don't count against the number of spells you can prepare each day. \n \n"
                "If you gain an oath spell that doesn't appear on the paladin spell list, the spell is nonetheless a paladin spell for you. \n \n"
                "#### Channel Divinity \n \n"
                "Your oath allows you to channel divine energy to fuel magical effects. Each Channel Divinity option provided by your oath explains how to use it. \n \n"
                "When you use your Channel Divinity, you choose which option to use. You must then finish a short or long rest to use your Channel Divinity again. \n \n"
                "Some Channel Divinity effects require saving throws. When you use such an effect from this class, the DC equals your paladin spell save DC. \n \n"
                "### Ability Score Improvement \n \n"
                "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature. \n \n"
                "### Extra Attack \n \n"
                "Beginning at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn. \n \n"
                "### Aura of Protection \n \n"
                "Starting at 6th level, whenever you or a friendly creature within 10 feet of you must make a saving throw, the creature gains a bonus to the saving throw equal to your Charisma modifier (with a minimum bonus of +1). You must be conscious to grant this bonus. \n \n"
                "At 18th level, the range of this aura increases to 30 feet. \n \n"
                "### Aura of Courage \n \n"
                "Starting at 10th level, you and friendly creatures within 10 feet of you can't be frightened while you are conscious. \n \n"
                "At 18th level, the range of this aura increases to 30 feet. \n \n"
                "### Improved Divine Smite \n \n"
                "By 11th level, you are so suffused with righteous might that all your melee weapon strikes carry divine power with them. Whenever you hit a creature with a melee weapon, the creature takes an extra 1d8 radiant damage. If you also use your Divine Smite with an attack, you add this damage to the extra damage of your Divine Smite. \n \n"
                "### Cleansing Touch \n \n"
                "Beginning at 14th level, you can use your action to end one spell on yourself or on one willing creature that you touch. \n \n"
                "You can use this feature a number of times equal to your Charisma modifier (a minimum of once). You regain expended uses when you finish a long rest. \n \n"
                "### Sacred Oaths \n \n"
                "Becoming a paladin involves taking vows that commit the paladin to the cause of righteousness, an active path of fighting wickedness. The final oath, taken when he or she reaches 3rd level, is the culmination of all the paladin's training. Some characters with this class don't consider themselves true paladins until they have reached 3rd level and made this oath. For others, the actual swearing of the oath is a formality, an official stamp on what has always been true in the paladin's heart.  \n"
                "> ### Breaking Your Oath \n> \n"
                "> A paladin tries to hold to the highest standards of conduct, but even the most virtuous paladin is fallible. Sometimes the right path proves too demanding, sometimes a situation calls for the lesser of two evils, and sometimes the heat of emotion causes a paladin to transgress his or her oath. \n> \n"
                "> A paladin who has broken a vow typically seeks absolution from a cleric who shares his or her faith or from another paladin of the same order. The paladin might spend an all- night vigil in prayer as a sign of penitence, or undertake a fast or similar act of self-denial. After a rite of confession and forgiveness, the paladin starts fresh. \n> \n"
                "> If a paladin willfully violates his or her oath and shows no sign of repentance, the consequences can be more serious. At the GM's discretion, an impenitent paladin might be forced to abandon this class and adopt another.",
        "hit_dice": "1d10",
        "hp_at_1st_level": "10 + your Constitution modifier",
        "hp_at_higher_levels": "1d10 (or 6) + your Constitution modifier per paladin level after 1st",
        "prof_armor": "All armor, shields",
        "prof_weapons": "Simple weapons, martial weapons",
        "prof_tools": "None",
        "prof_saving_throws": "Wisdom, Charisma",
        "prof_skills": "Choose two from Athletics, Insight, Intimidation, Medicine, Persuasion, and Religion",
        "equipment": "You start with the following equipment, in addition to the equipment granted by your background: \n"
                     "* (*a*) a martial weapon and a shield or (*b*) two martial weapons \n"
                     "* (*a*) five javelins or (*b*) any simple melee weapon \n"
                     "* (*a*) a priest's pack or (*b*) an explorer's pack \n"
                     "* Chain mail and a holy symbol",
        "table": "| Level | Proficiency Bonus | Features                                   | 1st | 2nd | 3rd | 4th | 5th | \n"
                 "|-------|-------------------|--------------------------------------------|-----|-----|-----|-----|-----| \n"
                 "| 1st   | +2                | Divine Sense, Lay on Hands                 | -   | -   | -   | -   | -   | \n"
                 "| 2nd   | +2                | Fighting Style, Spellcasting, Divine Smite | 2   | -   | -   | -   | -   | \n"
                 "| 3rd   | +2                | Divine Health, Sacred Oath                 | 3   | -   | -   | -   | -   | \n"
                 "| 4th   | +2                | Ability Score Improvement                  | 3   | -   | -   | -   | -   | \n"
                 "| 5th   | +3                | Extra Attack                               | 4   | 2   | -   | -   | -   | \n"
                 "| 6th   | +3                | Aura of Protection                         | 4   | 2   | -   | -   | -   | \n"
                 "| 7th   | +3                | Sacred Oath feature                        | 4   | 3   | -   | -   | -   | \n"
                 "| 8th   | +3                | Ability Score Improvement                  | 4   | 3   | -   | -   | -   | \n"
                 "| 9th   | +4                | -                                          | 4   | 3   | 2   | -   | -   | \n"
                 "| 10th  | +4                | Aura of Courage                            | 4   | 3   | 2   | -   | -   | \n"
                 "| 11th  | +4                | Improved Divine Smite                      | 4   | 3   | 3   | -   | -   | \n"
                 "| 12th  | +4                | Ability Score Improvement                  | 4   | 3   | 3   | -   | -   | \n"
                 "| 13th  | +5                | -                                          | 4   | 3   | 3   | 1   | -   | \n"
                 "| 14th  | +5                | Cleansing Touch                            | 4   | 3   | 3   | 1   | -   | \n"
                 "| 15th  | +5                | Sacred Oath feature                        | 4   | 3   | 3   | 2   | -   | \n"
                 "| 16th  | +5                | Ability Score Improvement                  | 4   | 3   | 3   | 2   | -   | \n"
                 "| 17th  | +6                | -                                          | 4   | 3   | 3   | 3   | 1   | \n"
                 "| 18th  | +6                | Aura improvements                          | 4   | 3   | 3   | 3   | 1   | \n"
                 "| 19th  | +6                | Ability Score Improvement                  | 4   | 3   | 3   | 3   | 2   | \n"
                 "| 20th  | +6                | Sacred Oath feature                        | 4   | 3   | 3   | 3   | 2   |",
        "spellcasting_ability": "Charisma",
        "subtypes_name": "",
        "archetypes": [
            {
                "name": "Oaths",
                "slug": "oaths",
                "desc": "The Oath of Devotion binds a paladin to the loftiest ideals of justice, virtue, and order. Sometimes called cavaliers, white knights, or holy warriors, these paladins meet the ideal of the knight in shining armor, acting with honor in pursuit of justice and the greater good. They hold themselves to the highest standards of conduct, and some, for better or worse, hold the rest of the world to the same standards. Many who swear this oath are devoted to gods of law and good and use their gods' tenets as the measure of their devotion. They hold angels-the perfect servants of good-as their ideals, and incorporate images of angelic wings into their helmets or coats of arms. \n \n"
                        "##### Tenets of Devotion \n \n"
                        "Though the exact words and strictures of the Oath of Devotion vary, paladins of this oath share these tenets. \n \n"
                        "**_Honesty._** Don't lie or cheat. Let your word be your promise. \n \n"
                        "**_Courage._** Never fear to act, though caution is wise. \n \n"
                        "**_Compassion._** Aid others, protect the weak, and punish those who threaten them. Show mercy to your foes, but temper it with wisdom. \n \n"
                        "**_Honor._** Treat others with fairness, and let your honorable deeds be an example to them. Do as much good as possible while causing the least amount of harm. \n \n"
                        "**_Duty._** Be responsible for your actions and their consequences, protect those entrusted to your care, and obey those who have just authority over you. \n \n"
                        "##### Oath Spells \n \n"
                        "You gain oath spells at the paladin levels listed. \n \n"
                        "**Oath of Devotion Spells (table)** \n \n"
                        "| Level | Paladin Spells                           | \n"
                        "|-------|------------------------------------------| \n"
                        "| 3rd   | protection from evil and good, sanctuary | \n"
                        "| 5th   | lesser restoration, zone of truth        | \n"
                        "| 9th   | beacon of hope, dispel magic             | \n"
                        "| 13th  | freedom of movement, guardian of faith   | \n"
                        "| 17th  | commune, flame strike                    | \n \n"
                        "##### Channel Divinity \n \n"
                        "When you take this oath at 3rd level, you gain the following two Channel Divinity options. \n \n"
                        "**_Sacred Weapon._** As an action, you can imbue one weapon that you are holding with positive energy, using your Channel Divinity. For 1 minute, you add your Charisma modifier to attack rolls made with that weapon (with a minimum bonus of +1). The weapon also emits bright light in a 20-foot radius and dim light 20 feet beyond that. If the weapon is not already magical, it becomes magical for the duration. \n \n"
                        "You can end this effect on your turn as part of any other action. If you are no longer holding or carrying this weapon, or if you fall unconscious, this effect ends. \n \n"
                        "**_Turn the Unholy._** As an action, you present your holy symbol and speak a prayer censuring fiends and undead, using your Channel Divinity. Each fiend or undead that can see or hear you within 30 feet of you must make a Wisdom saving throw. If the creature fails its saving throw, it is turned for 1 minute or until it takes damage. \n \n"
                        "A turned creature must spend its turns trying to move as far away from you as it can, and it can't willingly move to a space within 30 feet of you. It also can't take reactions. For its action, it can use only the Dash action or try to escape from an effect that prevents it from moving. If there's nowhere to move, the creature can use the Dodge action. \n \n"
                        "##### Aura of Devotion \n \n"
                        "Starting at 7th level, you and friendly creatures within 10 feet of you can't be charmed while you are conscious. \n \n"
                        "At 18th level, the range of this aura increases to 30 feet. \n \n"
                        "##### Purity of Spirit \n \n"
                        "Beginning at 15th level, you are always under the effects of a *protection from evil and good* spell. \n \n"
                        "##### Holy Nimbus \n \n"
                        "At 20th level, as an action, you can emanate an aura of sunlight. For 1 minute, bright light shines from you in a 30-foot radius, and dim light shines 30 feet beyond that. \n \n"
                        "Whenever an enemy creature starts its turn in the bright light, the creature takes 10 radiant damage. \n \n"
                        "In addition, for the duration, you have advantage on saving throws against spells cast by fiends or undead. \n \n"
                        "Once you use this feature, you can't use it again until you finish a long rest.",
                "document__slug": "wotc-srd",
                "document__title": "Systems Reference Document",
                "document__license_url": "http://open5e.com/legal"
            }
        ],
        "document__slug": "wotc-srd",
        "document__title": "Systems Reference Document",
        "document__license_url": "http://open5e.com/legal"
    },
    "ranger": {
        "name": "Ranger",
        "slug": "ranger",
        "desc": "### Favored Enemy \n \n"
                "Beginning at 1st level, you have significant experience studying, tracking, hunting, and even talking to a certain type of enemy. \n \n"
                "Choose a type of favored enemy: aberrations, beasts, celestials, constructs, dragons, elementals, fey, fiends, giants, monstrosities, oozes, plants, or undead. Alternatively, you can select two races of humanoid (such as gnolls and orcs) as favored enemies. \n \n"
                "You have advantage on Wisdom (Survival) checks to track your favored enemies, as well as on Intelligence checks to recall information about them. \n \n"
                "When you gain this feature, you also learn one language of your choice that is spoken by your favored enemies, if they speak one at all. \n \n"
                "You choose one additional favored enemy, as well as an associated language, at 6th and 14th level. As you gain levels, your choices should reflect the types of monsters you have encountered on your adventures. \n \n"
                "### Natural Explorer \n \n"
                "You are particularly familiar with one type of natural environment and are adept at traveling and surviving in such regions. Choose one type of favored terrain: arctic, coast, desert, forest, grassland, mountain, or swamp. When you make an Intelligence or Wisdom check related to your favored terrain, your proficiency bonus is doubled if you are using a skill that you're proficient in. \n \n"
                "While traveling for an hour or more in your favored terrain, you gain the following benefits: \n"
                "* Difficult terrain doesn't slow your group's travel. \n"
                "* Your group can't become lost except by magical means. \n"
                "* Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger. \n"
                "* If you are traveling alone, you can move stealthily at a normal pace. \n"
                "* When you forage, you find twice as much food as you normally would. \n"
                "* While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area. \n \n"
                "You choose additional favored terrain types at 6th and 10th level. \n \n"
                "### Fighting Style \n \n"
                "At 2nd level, you adopt a particular style of fighting as your specialty. Choose one of the following options. You can't take a Fighting Style option more than once, even if you later get to choose again. \n \n"
                "#### Archery \n \n"
                "You gain a +2 bonus to attack rolls you make with ranged weapons. \n \n"
                "#### Defense \n \n"
                "While you are wearing armor, you gain a +1 bonus to AC. \n \n"
                "#### Dueling \n \n"
                "When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon. \n \n"
                "#### Two-Weapon Fighting \n \n"
                "When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack. \n \n"
                "### Spellcasting \n \n"
                "By the time you reach 2nd level, you have learned to use the magical essence of nature to cast spells, much as a druid does. See chapter 10 for the general rules of spellcasting and chapter 11 for the ranger spell list. \n \n"
                "#### Spell Slots \n \n"
                "The Ranger table shows how many spell slots you have to cast your spells of 1st level and higher. To cast one of these spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest. \n \n"
                "For example, if you know the 1st-level spell *animal friendship* and have a 1st-level and a 2nd-level spell slot available, you can cast *animal friendship* using either slot. \n \n"
                "#### Spells Known of 1st Level and Higher \n \n"
                "You know two 1st-level spells of your choice from the ranger spell list. \n \n"
                "The Spells Known column of the Ranger table shows when you learn more ranger spells of your choice. Each of these spells must be of a level for which you have spell slots. For instance, when you reach 5th level in this class, you can learn one new spell of 1st or 2nd level. \n \n"
                "Additionally, when you gain a level in this class, you can choose one of the ranger spells you know and replace it with another spell from the ranger spell list, which also must be of a level for which you have spell slots. \n \n"
                "#### Spellcasting Ability \n \n"
                "Wisdom is your spellcasting ability for your ranger spells, since your magic draws on your attunement to nature. You use your Wisdom whenever a spell refers to your spellcasting ability. In addition, you use your Wisdom modifier when setting the saving throw DC for a ranger spell you cast and when making an attack roll with one. \n \n"
                "**Spell save DC** = 8 + your proficiency bonus + your Wisdom modifier \n \n"
                "**Spell attack modifier** = your proficiency bonus + your Wisdom modifier \n \n"
                "### Ranger Archetype \n \n"
                "At 3rd level, you choose an archetype that you strive to emulate: Hunter or Beast Master, both detailed at the end of the class description. Your choice grants you features at 3rd level and again at 7th, 11th, and 15th level. \n \n"
                "### Primeval Awareness \n \n"
                "Beginning at 3rd level, you can use your action and expend one ranger spell slot to focus your awareness on the region around you. For 1 minute per level of the spell slot you expend, you can sense whether the following types of creatures are present within 1 mile of you (or within up to 6 miles if you are in your favored terrain): aberrations, celestials, dragons, elementals, fey, fiends, and undead. This feature doesn't reveal the creatures' location or number. \n \n"
                "### Ability Score Improvement \n \n"
                "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature. \n \n"
                "### Extra Attack \n \n"
                "Beginning at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn. \n \n"
                "### Land's Stride \n \n"
                "Starting at 8th level, moving through nonmagical difficult terrain costs you no extra movement. You can also pass through nonmagical plants without being slowed by them and without taking damage from them if they have thorns, spines, or a similar hazard. \n \n"
                "In addition, you have advantage on saving throws against plants that are magically created or manipulated to impede movement, such those created by the *entangle* spell. \n \n"
                "### Hide in Plain Sight \n \n"
                "Starting at 10th level, you can spend 1 minute creating camouflage for yourself. You must have access to fresh mud, dirt, plants, soot, and other naturally occurring materials with which to create your camouflage. \n \n"
                "Once you are camouflaged in this way, you can try to hide by pressing yourself up against a solid surface, such as a tree or wall, that is at least as tall and wide as you are. You gain a +10 bonus to Dexterity (Stealth) checks as long as you remain there without moving or taking actions. Once you move or take an action or a reaction, you must camouflage yourself again to gain this benefit. \n \n"
                "### Vanish \n \n"
                "Starting at 14th level, you can use the Hide action as a bonus action on your turn. Also, you can't be tracked by nonmagical means, unless you choose to leave a trail. \n \n"
                "### Feral Senses \n \n"
                "At 18th level, you gain preternatural senses that help you fight creatures you can't see. When you attack a creature you can't see, your inability to see it doesn't impose disadvantage on your attack rolls against it. \n \n"
                "You are also aware of the location of any invisible creature within 30 feet of you, provided that the creature isn't hidden from you and you aren't blinded or deafened. \n \n"
                "### Foe Slayer \n \n"
                "At 20th level, you become an unparalleled hunter of your enemies. Once on each of your turns, you can add your Wisdom modifier to the attack roll or the damage roll of an attack you make against one of your favored enemies. You can choose to use this feature before or after the roll, but before any effects of the roll are applied.",
        "hit_dice": "1d10",
        "hp_at_1st_level": "10 + your Constitution modifier",
        "hp_at_higher_levels": "1d10 (or 6) + your Constitution modifier per ranger level after 1st",
        "prof_armor": "Light armor, medium armor, shields",
        "prof_weapons": "Simple weapons, martial weapons",
        "prof_tools": "None",
        "prof_saving_throws": "Strength, Dexterity",
        "prof_skills": "Choose three from Animal Handling, Athletics, Insight, Investigation, Nature, Perception, Stealth, and Survival",
        "equipment": "You start with the following equipment, in addition to the equipment granted by your background: \n"
                     "* (*a*) scale mail or (*b*) leather armor \n"
                     "* (*a*) two shortswords or (*b*) two simple melee weapons \n"
                     "* (*a*) a dungeoneer's pack or (*b*) an explorer's pack \n"
                     "* A longbow and a quiver of 20 arrows",
        "table": "| Level | Proficiency Bonus | Features                                          | Spells Known | 1st | 2nd | 3rd | 4th | 5th | \n"
                 "|-------|-------------------|---------------------------------------------------|--------------|-----|-----|-----|-----|-----| \n"
                 "| 1st   | +2                | Favored Enemy, Natural Explorer                   | -            | -   | -   | -   | -   | -   | \n"
                 "| 2nd   | +2                | Fighting Style, Spellcasting                      | 2            | 2   | -   | -   | -   | -   | \n"
                 "| 3rd   | +2                | Ranger Archetype, Primeval Awareness              | 3            | 3   | -   | -   | -   | -   | \n"
                 "| 4th   | +2                | Ability Score Improvement                         | 3            | 3   | -   | -   | -   | -   | \n"
                 "| 5th   | +3                | Extra Attack                                      | 4            | 4   | 2   | -   | -   | -   | \n"
                 "| 6th   | +3                | Favored Enemy and Natural Explorer improvements   | 4            | 4   | 2   | -   | -   | -   | \n"
                 "| 7th   | +3                | Ranger Archetype feature                          | 5            | 4   | 3   | -   | -   | -   | \n"
                 "| 8th   | +3                | Ability Score Improvement, Land's Stride          | 5            | 4   | 3   | -   | -   | -   | \n"
                 "| 9th   | +4                | -                                                 | 6            | 4   | 3   | 2   | -   | -   | \n"
                 "| 10th  | +4                | Natural Explorer improvement, Hide in Plain Sight | 6            | 4   | 3   | 2   | -   | -   | \n"
                 "| 11th  | +4                | Ranger Archetype feature                          | 7            | 4   | 3   | 3   | -   | -   | \n"
                 "| 12th  | +4                | Ability Score Improvement                         | 7            | 4   | 3   | 3   | -   | -   | \n"
                 "| 13th  | +5                | -                                                 | 8            | 4   | 3   | 3   | 1   | -   | \n"
                 "| 14th  | +5                | Favored Enemy improvement, Vanish                 | 8            | 4   | 3   | 3   | 1   | -   | \n"
                 "| 15th  | +5                | Ranger Archetype feature                          | 9            | 4   | 3   | 3   | 2   | -   | \n"
                 "| 16th  | +5                | Ability Score Improvement                         | 9            | 4   | 3   | 3   | 2   | -   | \n"
                 "| 17th  | +6                | -                                                 | 10           | 4   | 3   | 3   | 3   | 1   | \n"
                 "| 18th  | +6                | Feral Senses                                      | 10           | 4   | 3   | 3   | 3   | 1   | \n"
                 "| 19th  | +6                | Ability Score Improvement                         | 11           | 4   | 3   | 3   | 3   | 2   | \n"
                 "| 20th  | +6                | Foe Slayer                                        | 11           | 4   | 3   | 3   | 3   | 2   | ",
        "spellcasting_ability": "Wisdom",
        "subtypes_name": "Archetypes",
        "archetypes": [
            {
                "name": "Hunter",
                "slug": "hunter",
                "desc": "Emulating the Hunter archetype means accepting your place as a bulwark between civilization and the terrors of the wilderness. As you walk the Hunter's path, you learn specialized techniques for fighting the threats you face, from rampaging ogres and hordes of orcs to towering giants and terrifying dragons. \n \n"
                        "##### Hunter's Prey \n \n"
                        "At 3rd level, you gain one of the following features of your choice. \n \n"
                        "**_Colossus Slayer._** Your tenacity can wear down the most potent foes. When you hit a creature with a weapon attack, the creature takes an extra 1d8 damage if it's below its hit point maximum. You can deal this extra damage only once per turn. \n \n"
                        "**_Giant Killer._** When a Large or larger creature within 5 feet of you hits or misses you with an attack, you can use your reaction to attack that creature immediately after its attack, provided that you can see the creature. \n \n"
                        "**_Horde Breaker._** Once on each of your turns when you make a weapon attack, you can make another attack with the same weapon against a different creature that is within 5 feet of the original target and within range of your weapon. \n \n"
                        "##### Defensive Tactics \n \n"
                        "At 7th level, you gain one of the following features of your choice. \n \n"
                        "**_Escape the Horde._** Opportunity attacks against you are made with disadvantage. \n \n"
                        "**_Multiattack Defense._** When a creature hits you with an attack, you gain a +4 bonus to AC against all subsequent attacks made by that creature for the rest of the turn. \n \n"
                        "**_Steel Will._** You have advantage on saving throws against being frightened. \n \n"
                        "##### Multiattack \n \n"
                        "At 11th level, you gain one of the following features of your choice. \n \n"
                        "**_Volley._** You can use your action to make a ranged attack against any number of creatures within 10 feet of a point you can see within your weapon's range. You must have ammunition for each target, as normal, and you make a separate attack roll for each target. \n \n"
                        "**_Whirlwind Attack._** You can use your action to make a melee attack against any number of creatures within 5 feet of you, with a separate attack roll for each target. \n \n"
                        "##### Superior Hunter's Defense \n \n"
                        "At 15th level, you gain one of the following features of your choice. \n \n"
                        "**_Evasion._** When you are subjected to an effect, such as a red dragon's fiery breath or a *lightning bolt* spell, that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on the saving throw, and only half damage if you fail. \n \n"
                        "**_Stand Against the Tide._** When a hostile creature misses you with a melee attack, you can use your reaction to force that creature to repeat the same attack against another creature (other than itself) of your choice. \n \n"
                        "**_Uncanny Dodge._** When an attacker that you can see hits you with an attack, you can use your reaction to halve the attack's damage against you.",
                "document__slug": "wotc-srd",
                "document__title": "Systems Reference Document",
                "document__license_url": "http://open5e.com/legal"
            }
        ],
        "document__slug": "wotc-srd",
        "document__title": "Systems Reference Document",
        "document__license_url": "http://open5e.com/legal"
    },
    "rogue": {
        "name": "Rogue",
        "slug": "rogue",
        "desc": "### Expertise \n \n"
                "At 1st level, choose two of your skill proficiencies, or one of your skill proficiencies and your proficiency with thieves' tools. Your proficiency bonus is doubled for any ability check you make that uses either of the chosen proficiencies. \n \nAt 6th level, you can choose two more of your proficiencies (in skills or with thieves' tools) to gain this benefit. \n \n### Sneak Attack \n \nBeginning at 1st level, you know how to strike subtly and exploit a foe's distraction. Once per turn, you can deal an extra 1d6 damage to one creature you hit with an attack if you have advantage on the attack roll. The attack must use a finesse or a ranged weapon. \n \nYou don't need advantage on the attack roll if another enemy of the target is within 5 feet of it, that enemy isn't incapacitated, and you don't have disadvantage on the attack roll. \n \nThe amount of the extra damage increases as you gain levels in this class, as shown in the Sneak Attack column of the Rogue table. \n \n### Thieves' Cant \n \nDuring your rogue training you learned thieves' cant, a secret mix of dialect, jargon, and code that allows you to hide messages in seemingly normal conversation. Only another creature that knows thieves' cant understands such messages. It takes four times longer to convey such a message than it does to speak the same idea plainly. \n \nIn addition, you understand a set of secret signs and symbols used to convey short, simple messages, such as whether an area is dangerous or the territory of a thieves' guild, whether loot is nearby, or whether the people in an area are easy marks or will provide a safe house for thieves on the run. \n \n### Cunning Action \n \nStarting at 2nd level, your quick thinking and agility allow you to move and act quickly. You can take a bonus action on each of your turns in combat. This action can be used only to take the Dash, Disengage, or Hide action. \n \n### Roguish Archetype \n \nAt 3rd level, you choose an archetype that you emulate in the exercise of your rogue abilities: Thief, Assassin, or Arcane Trickster, all detailed at the end of the class description. Your archetype choice grants you features at 3rd level and then again at 9th, 13th, and 17th level. \n \n### Ability Score Improvement \n \nWhen you reach 4th level, and again at 8th, 10th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature. \n \n### Uncanny Dodge \n \nStarting at 5th level, when an attacker that you can see hits you with an attack, you can use your reaction to halve the attack's damage against you. \n \n### Evasion \n \nBeginning at 7th level, you can nimbly dodge out of the way of certain area effects, such as a red dragon's fiery breath or an *ice storm* spell. When you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on the saving throw, and only half damage if you fail. \n \n### Reliable Talent \n \nBy 11th level, you have refined your chosen skills until they approach perfection. Whenever you make an ability check that lets you add your proficiency bonus, you can treat a d20 roll of 9 or lower as a 10. \n \n### Blindsense \n \nStarting at 14th level, if you are able to hear, you are aware of the location of any hidden or invisible creature within 10 feet of you. \n \n### Slippery Mind \n \nBy 15th level, you have acquired greater mental strength. You gain proficiency in Wisdom saving throws. \n \n### Elusive \n \nBeginning at 18th level, you are so evasive that attackers rarely gain the upper hand against you. No attack roll has advantage against you while you aren't incapacitated. \n \n### Stroke of Luck \n \nAt 20th level, you have an uncanny knack for succeeding when you need to. If your attack misses a target within range, you can turn the miss into a hit. Alternatively, if you fail an ability check, you can treat the d20 roll as a 20. \n \nOnce you use this feature, you can't use it again until you finish a short or long rest. \n \n### Roguish Archetypes \n \nRogues have many features in common, including their emphasis on perfecting their skills, their precise and deadly approach to combat, and their increasingly quick reflexes. But different rogues steer those talents in varying directions, embodied by the rogue archetypes. Your choice of archetype is a reflection of your focus-not necessarily an indication of your chosen profession, but a description of your preferred techniques.",
        "hit_dice": "1d8",
        "hp_at_1st_level": "8 + your Constitution modifier",
        "hp_at_higher_levels": "1d8 (or 5) + your Constitution modifier per rogue level after 1st",
        "prof_armor": "Light armor",
        "prof_weapons": "Simple weapons, hand crossbows, longswords, rapiers, shortswords",
        "prof_tools": "Thieves' tools",
        "prof_saving_throws": "Dexterity, Intelligence",
        "prof_skills": "Choose four from Acrobatics, Athletics, Deception, Insight, Intimidation, Investigation, Perception, Performance, Persuasion, Sleight of Hand, and Stealth",
        "equipment": "You start with the following equipment, in addition to the equipment granted by your background: \n"
                     "* (*a*) a rapier or (*b*) a shortsword \n"
                     "* (*a*) a shortbow and quiver of 20 arrows or (*b*) a shortsword \n"
                     "* (*a*) a burglar's pack, (*b*) a dungeoneer's pack, or (*c*) an explorer's pack \n"
                     "* (*a*) Leather armor, two daggers, and thieves' tools",
        "table": "| Level | Proficiency Bonus | Sneak Attack | Features                               | \n"
                 "|-------|-------------------|--------------|----------------------------------------| \n"
                 "| 1st   | +2                | 1d6          | Expertise, Sneak Attack, Thieves' Cant | \n"
                 "| 2nd   | +2                | 1d6          | Cunning Action                         | \n"
                 "| 3rd   | +2                | 2d6          | Roguish Archetype                      | \n"
                 "| 4th   | +2                | 2d6          | Ability Score Improvement              | \n"
                 "| 5th   | +3                | 3d6          | Uncanny Dodge                          | \n"
                 "| 6th   | +3                | 3d6          | Expertise                              | \n"
                 "| 7th   | +3                | 4d6          | Evasion                                | \n"
                 "| 8th   | +3                | 4d6          | Ability Score Improvement              | \n"
                 "| 9th   | +4                | 5d6          | Roguish Archetype feature              | \n"
                 "| 10th  | +4                | 5d6          | Ability Score Improvement              | \n"
                 "| 11th  | +4                | 6d6          | Reliable Talent                        | \n"
                 "| 12th  | +4                | 6d6          | Ability Score Improvement              | \n"
                 "| 13th  | +5                | 7d6          | Roguish Archetype Feature              | \n"
                 "| 14th  | +5                | 7d6          | Blindsense                             | \n"
                 "| 15th  | +5                | 8d6          | Slippery Mind                          | \n"
                 "| 16th  | +5                | 8d6          | Ability Score Improvement              | \n"
                 "| 17th  | +6                | 9d6          | Roguish Archetype Feature              | \n"
                 "| 18th  | +6                | 9d6          | Elusive                                | \n"
                 "| 19th  | +6                | 10d6         | Ability Score Improvement              | \n"
                 "| 20th  | +6                | 10d6         | Stroke of Luck                         | ",
        "spellcasting_ability": "",
        "subtypes_name": "Roguish Archetypes",
        "archetypes": [
            {
                "name": "Thief",
                "slug": "thief",
                "desc": "You hone your skills in the larcenous arts. Burglars, bandits, cutpurses, and other criminals typically follow this archetype, but so do rogues who prefer to think of themselves as professional treasure seekers, explorers, delvers, and investigators. In addition to improving your agility and stealth, you learn skills useful for delving into ancient ruins, reading unfamiliar languages, and using magic items you normally couldn't employ. \n \n"
                        "##### Fast Hands \n \n"
                        "Starting at 3rd level, you can use the bonus action granted by your Cunning Action to make a Dexterity (Sleight of Hand) check, use your thieves' tools to disarm a trap or open a lock, or take the Use an Object action. \n \n"
                        "##### Second-Story Work \n \n"
                        "When you choose this archetype at 3rd level, you gain the ability to climb faster than normal; climbing no longer costs you extra movement. \n \n"
                        "In addition, when you make a running jump, the distance you cover increases by a number of feet equal to your Dexterity modifier. \n \n"
                        "##### Supreme Sneak \n \n"
                        "Starting at 9th level, you have advantage on a Dexterity (Stealth) check if you move no more than half your speed on the same turn. \n \n"
                        "##### Use Magic Device \n \n"
                        "By 13th level, you have learned enough about the workings of magic that you can improvise the use of items even when they are not intended for you. You ignore all class, race, and level requirements on the use of magic items. \n \n"
                        "##### Thief's Reflexes \n \n"
                        "When you reach 17th level, you have become adept at laying ambushes and quickly escaping danger. You can take two turns during the first round of any combat. You take your first turn at your normal initiative and your second turn at your initiative minus 10. You can't use this feature when you are surprised.",
                "document__slug": "wotc-srd",
                "document__title": "Systems Reference Document",
                "document__license_url": "http://open5e.com/legal"
            }
        ],
        "document__slug": "wotc-srd",
        "document__title": "Systems Reference Document",
        "document__license_url": "http://open5e.com/legal"
    },
    "sorcerer": {
        "name": "Sorcerer",
        "slug": "sorcerer",
        "desc": "### Spellcasting \n \n"
                "An event in your past, or in the life of a parent or ancestor, left an indelible mark on you, infusing you with arcane magic. This font of magic, whatever its origin, fuels your spells. \n \n"
                "#### Cantrips \n \n"
                "At 1st level, you know four cantrips of your choice from the sorcerer spell list. You learn additional sorcerer cantrips of your choice at higher levels, as shown in the Cantrips Known column of the Sorcerer table. \n \n"
                "#### Spell Slots \n \n"
                "The Sorcerer table shows how many spell slots you have to cast your spells of 1st level and higher. To cast one of these sorcerer spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest. \n \n"
                "For example, if you know the 1st-level spell *burning hands* and have a 1st-level and a 2nd-level spell slot available, you can cast *burning hands* using either slot. \n \n"
                "#### Spells Known of 1st Level and Higher \n \n"
                "You know two 1st-level spells of your choice from the sorcerer spell list. \n \n"
                "The Spells Known column of the Sorcerer table shows when you learn more sorcerer spells of your choice. Each of these spells must be of a level for which you have spell slots. For instance, when you reach 3rd level in this class, you can learn one new spell of 1st or 2nd level. \n \n"
                "Additionally, when you gain a level in this class, you can choose one of the sorcerer spells you know and replace it with another spell from the sorcerer spell list, which also must be of a level for which you have spell slots. \n \n"
                "#### Spellcasting Ability \n \n"
                "Charisma is your spellcasting ability for your sorcerer spells, since the power of your magic relies on your ability to project your will into the world. You use your Charisma whenever a spell refers to your spellcasting ability. In addition, you use your Charisma modifier when setting the saving throw DC for a sorcerer spell you cast and when making an attack roll with one. \n \n"
                "**Spell save DC** = 8 + your proficiency bonus + your Charisma modifier \n \n"
                "**Spell attack modifier** = your proficiency bonus + your Charisma modifier \n \n"
                "#### Spellcasting Focus \n \n"
                "You can use an arcane focus as a spellcasting focus for your sorcerer spells. \n \n"
                "### Sorcerous Origin \n \n"
                "Choose a sorcerous origin, which describes the source of your innate magical power: Draconic Bloodline or Wild Magic, both detailed at the end of the class description. \n \n"
                "Your choice grants you features when you choose it at 1st level and again at 6th, 14th, and 18th level. \n \n"
                "### Font of Magic \n \n"
                "At 2nd level, you tap into a deep wellspring of magic within yourself. This wellspring is represented by sorcery points, which allow you to create a variety of magical effects. \n \n"
                "#### Sorcery Points \n \n"
                "You have 2 sorcery points, and you gain more as you reach higher levels, as shown in the Sorcery Points column of the Sorcerer table. You can never have more sorcery points than shown on the table for your level. You regain all spent sorcery points when you finish a long rest. \n \n"
                "#### Flexible Casting \n \n"
                "You can use your sorcery points to gain additional spell slots, or sacrifice spell slots to gain additional sorcery points. You learn other ways to use your sorcery points as you reach higher levels. \n \n"
                "**_Creating Spell Slots._** You can transform unexpended sorcery points into one spell slot as a bonus action on your turn. The Creating Spell Slots table shows the cost of creating a spell slot of a given level. You can create spell slots no higher in level than 5th. \n \n"
                "Any spell slot you create with this feature vanishes when you finish a long rest. \n \n"
                "**Creating Spell Slots (table)** \n \n"
                "| Spell Slot Level | Sorcery Point Cost | \n"
                "|------------------|--------------------| \n"
                "| 1st              | 2                  | \n"
                "| 2nd              | 3                  | \n"
                "| 3rd              | 5                  | \n"
                "| 4th              | 6                  | \n"
                "| 5th              | 7                  | \n \n"
                "**_Converting a Spell Slot to Sorcery Points._** As a bonus action on your turn, you can expend one spell slot and gain a number of sorcery points equal to the slot's level. \n \n"
                "### Metamagic \n \n"
                "At 3rd level, you gain the ability to twist your spells to suit your needs. You gain two of the following Metamagic options of your choice. You gain another one at 10th and 17th level. \n \n"
                "You can use only one Metamagic option on a spell when you cast it, unless otherwise noted. \n \n"
                "#### Careful Spell \n \n"
                "When you cast a spell that forces other creatures to make a saving throw, you can protect some of those creatures from the spell's full force. To do so, you spend 1 sorcery point and choose a number of those creatures up to your Charisma modifier (minimum of one creature). A chosen creature automatically succeeds on its saving throw against the spell. \n \n"
                "#### Distant Spell \n \n"
                "When you cast a spell that has a range of 5 feet or greater, you can spend 1 sorcery point to double the range of the spell. \n \n"
                "When you cast a spell that has a range of touch, you can spend 1 sorcery point to make the range of the spell 30 feet. \n \n"
                "#### Empowered Spell \n \n"
                "When you roll damage for a spell, you can spend 1 sorcery point to reroll a number of the damage dice up to your Charisma modifier (minimum of one). You must use the new rolls. \n \n"
                "You can use Empowered Spell even if you have already used a different Metamagic option during the casting of the spell. \n \n"
                "#### Extended Spell \n \n"
                "When you cast a spell that has a duration of 1 minute or longer, you can spend 1 sorcery point to double its duration, to a maximum duration of 24 hours. \n \n"
                "#### Heightened Spell \n \n"
                "When you cast a spell that forces a creature to make a saving throw to resist its effects, you can spend 3 sorcery points to give one target of the spell disadvantage on its first saving throw made against the spell. \n \n"
                "#### Quickened Spell \n \n"
                "When you cast a spell that has a casting time of 1 action, you can spend 2 sorcery points to change the casting time to 1 bonus action for this casting. \n \n"
                "#### Subtle Spell \n \n"
                "When you cast a spell, you can spend 1 sorcery point to cast it without any somatic or verbal components. \n \n"
                "#### Twinned Spell \n \n"
                "When you cast a spell that targets only one creature and doesn't have a range of self, you can spend a number of sorcery points equal to the spell's level to target a second creature in range with the same spell (1 sorcery point if the spell is a cantrip). \n \n"
                "To be eligible, a spell must be incapable of targeting more than one creature at the spell's current level. For example, *magic missile* and *scorching ray* aren't eligible, but *ray of frost* and *chromatic orb* are. \n \n"
                "### Ability Score Improvement \n \n"
                "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature. \n \n"
                "### Sorcerous Restoration \n \n"
                "At 20th level, you regain 4 expended sorcery points whenever you finish a short rest. \n \n"
                "### Sorcerous Origins \n \n"
                "Different sorcerers claim different origins for their innate magic. Although many variations exist, most of these origins fall into two categories: a draconic bloodline and wild magic.",
        "hit_dice": "1d6",
        "hp_at_1st_level": "6 + your Constitution modifier",
        "hp_at_higher_levels": "1d6 (or 4) + your Constitution modifier per sorcerer level after 1st",
        "prof_armor": "None",
        "prof_weapons": "Daggers, darts, slings, quarterstaffs, light crossbows",
        "prof_tools": "None",
        "prof_saving_throws": "Constitution, Charisma",
        "prof_skills": "Choose two from Arcana, Deception, Insight, Intimidation, Persuasion, and Religion",
        "equipment": "You start with the following equipment, in addition to the equipment granted by your background: \n"
                     "* (*a*) a light crossbow and 20 bolts or (*b*) any simple weapon \n"
                     "* (*a*) a component pouch or (*b*) an arcane focus \n"
                     "* (*a*) a dungeoneer's pack or (*b*) an explorer's pack \n"
                     "* Two daggers",
        "table": "| Level | Proficiency Bonus | Sorcery Points | Features                       | Cantrips Known | Spells Known | 1st | 2nd | 3rd | 4th | 5th | 6th | 7th | 8th | 9th | \n"
                 "|-------|-------------------|----------------|--------------------------------|----------------|--------------|-----|-----|-----|-----|-----|-----|-----|-----|-----| \n"
                 "| 1st   | +2                | -              | Spellcasting, Sorcerous Origin | 4              | 2            | 2   | -   | -   | -   | -   | -   | -   | -   | -   | \n"
                 "| 2nd   | +2                | 2              | Font of Magic                  | 4              | 3            | 3   | -   | -   | -   | -   | -   | -   | -   | -   | \n"
                 "| 3rd   | +2                | 3              | Metamagic                      | 4              | 4            | 4   | 2   | -   | -   | -   | -   | -   | -   | -   | \n"
                 "| 4th   | +2                | 4              | Ability Score Improvement      | 5              | 5            | 4   | 3   | -   | -   | -   | -   | -   | -   | -   | \n"
                 "| 5th   | +3                | 5              | -                              | 5              | 6            | 4   | 3   | 2   | -   | -   | -   | -   | -   | -   | \n"
                 "| 6th   | +3                | 6              | Sorcerous Origin Feature       | 5              | 7            | 4   | 3   | 3   | -   | -   | -   | -   | -   | -   | \n"
                 "| 7th   | +3                | 7              | -                              | 5              | 8            | 4   | 3   | 3   | 1   | -   | -   | -   | -   | -   | \n"
                 "| 8th   | +3                | 8              | Ability Score Improvement      | 5              | 9            | 4   | 3   | 3   | 2   | -   | -   | -   | -   | -   | \n"
                 "| 9th   | +4                | 9              | -                              | 5              | 10           | 4   | 3   | 3   | 3   | 1   | -   | -   | -   | -   | \n"
                 "| 10th  | +4                | 10             | Metamagic                      | 6              | 11           | 4   | 3   | 3   | 3   | 2   | -   | -   | -   | -   | \n"
                 "| 11th  | +4                | 11             | -                              | 6              | 12           | 4   | 3   | 3   | 3   | 2   | 1   | -   | -   | -   | \n"
                 "| 12th  | +4                | 12             | Ability Score Improvement      | 6              | 12           | 4   | 3   | 3   | 3   | 2   | 1   | -   | -   | -   | \n"
                 "| 13th  | +5                | 13             | -                              | 6              | 13           | 4   | 3   | 3   | 3   | 2   | 1   | 1   | -   | -   | \n"
                 "| 14th  | +5                | 14             | Sorcerous Origin Feature       | 6              | 13           | 4   | 3   | 3   | 3   | 2   | 1   | 1   | -   | -   | \n"
                 "| 15th  | +5                | 15             | -                              | 6              | 14           | 4   | 3   | 3   | 3   | 2   | 1   | 1   | 1   | -   | \n"
                 "| 16th  | +5                | 16             | Ability Score Improvement      | 6              | 14           | 4   | 3   | 3   | 3   | 2   | 1   | 1   | 1   | -   | \n"
                 "| 17th  | +6                | 17             | Metamagic                      | 6              | 15           | 4   | 3   | 3   | 3   | 2   | 1   | 1   | 1   | 1   | \n"
                 "| 18th  | +6                | 18             | Sorcerous Origin Feature       | 6              | 15           | 4   | 3   | 3   | 3   | 3   | 1   | 1   | 1   | 1   | \n"
                 "| 19th  | +6                | 19             | Ability Score Improvement      | 6              | 15           | 4   | 3   | 3   | 3   | 3   | 2   | 1   | 1   | 1   | \n"
                 "| 20th  | +6                | 20             | Sorcerous Restoration          | 6              | 15           | 4   | 3   | 3   | 3   | 3   | 2   | 2   | 1   | 1   |",
        "spellcasting_ability": "Charisma",
        "subtypes_name": "Sorcerous Origins",
        "archetypes": [
            {
                "name": "Draconic Bloodline",
                "slug": "draconic-bloodline",
                "desc": "Your innate magic comes from draconic magic that was mingled with your blood or that of your ancestors. Most often, sorcerers with this origin trace their descent back to a mighty sorcerer of ancient times who made a bargain with a dragon or who might even have claimed a dragon parent. Some of these bloodlines are well established in the world, but most are obscure. Any given sorcerer could be the first of a new bloodline, as a result of a pact or some other exceptional circumstance. \n \n"
                        "##### Dragon Ancestor \n \n"
                        "At 1st level, you choose one type of dragon as your ancestor. The damage type associated with each dragon is used by features you gain later. \n \n"
                        "**Draconic Ancestry (table)** \n \n"
                        "| Dragon | Damage Type | \n"
                        "|--------|-------------| \n"
                        "| Black  | Acid        | \n"
                        "| Blue   | Lightning   | \n"
                        "| Brass  | Fire        | \n"
                        "| Bronze | Lightning   | \n"
                        "| Copper | Acid        | \n"
                        "| Gold   | Fire        | \n"
                        "| Green  | Poison      | \n"
                        "| Red    | Fire        | \n"
                        "| Silver | Cold        | \n"
                        "| White  | Cold        | \n \n"
                        "You can speak, read, and write Draconic. Additionally, whenever you make a Charisma check when interacting with dragons, your proficiency bonus is doubled if it applies to the check. \n \n"
                        "##### Draconic Resilience \n \n"
                        "As magic flows through your body, it causes physical traits of your dragon ancestors to emerge. At 1st level, your hit point maximum increases by 1 and increases by 1 again whenever you gain a level in this class. \n \n"
                        "Additionally, parts of your skin are covered by a thin sheen of dragon-like scales. When you aren't wearing armor, your AC equals 13 + your Dexterity modifier. \n \n"
                        "##### Elemental Affinity \n \n"
                        "Starting at 6th level, when you cast a spell that deals damage of the type associated with your draconic ancestry, you can add your Charisma modifier to one damage roll of that spell. At the same time, you can spend 1 sorcery point to gain resistance to that damage type for 1 hour. \n \n"
                        "##### Dragon Wings \n \n"
                        "At 14th level, you gain the ability to sprout a pair of dragon wings from your back, gaining a flying speed equal to your current speed. You can create these wings as a bonus action on your turn. They last until you dismiss them as a bonus action on your turn. \n \n"
                        "You can't manifest your wings while wearing armor unless the armor is made to accommodate them, and clothing not made to accommodate your wings might be destroyed when you manifest them. \n \n"
                        "##### Draconic Presence \n \n"
                        "Beginning at 18th level, you can channel the dread presence of your dragon ancestor, causing those around you to become awestruck or frightened. As an action, you can spend 5 sorcery points to draw on this power and exude an aura of awe or fear (your choice) to a distance of 60 feet. For 1 minute or until you lose your concentration (as if you were casting a concentration spell), each hostile creature that starts its turn in this aura must succeed on a Wisdom saving throw or be charmed (if you chose awe) or frightened (if you chose fear) until the aura ends. A creature that succeeds on this saving throw is immune to your aura for 24 hours.",
                "document__slug": "wotc-srd",
                "document__title": "Systems Reference Document",
                "document__license_url": "http://open5e.com/legal"
            }
        ],
        "document__slug": "wotc-srd",
        "document__title": "Systems Reference Document",
        "document__license_url": "http://open5e.com/legal"
    },
    "warlock": {
        "name": "Warlock",
        "slug": "warlock",
        "desc": "### Otherworldly Patron \n \n"
                "At 1st level, you have struck a bargain with an otherworldly being of your choice: the Archfey, the Fiend, or the Great Old One, each of which is detailed at the end of the class description. Your choice grants you features at 1st level and again at 6th, 10th, and 14th level. \n \n"
                "### Pact Magic \n \n"
                "Your arcane research and the magic bestowed on you by your patron have given you facility with spells. \n \n"
                "#### Cantrips \n \n"
                "You know two cantrips of your choice from the warlock spell list. You learn additional warlock cantrips of your choice at higher levels, as shown in the Cantrips Known column of the Warlock table. \n \n"
                "#### Spell Slots \n \n"
                "The Warlock table shows how many spell slots you have. The table also shows what the level of those slots is; all of your spell slots are the same level. To cast one of your warlock spells of 1st level or higher, you must expend a spell slot. You regain all expended spell slots when you finish a short or long rest. \n \n"
                "For example, when you are 5th level, you have two 3rd-level spell slots. To cast the 1st-level spell *thunderwave*, you must spend one of those slots, and you cast it as a 3rd-level spell. \n \n"
                "#### Spells Known of 1st Level and Higher \n \n"
                "At 1st level, you know two 1st-level spells of your choice from the warlock spell list. \n \n"
                "The Spells Known column of the Warlock table shows when you learn more warlock spells of your choice of 1st level and higher. A spell you choose must be of a level no higher than what's shown in the table's Slot Level column for your level. When you reach 6th level, for example, you learn a new warlock spell, which can be 1st, 2nd, or 3rd level. \n \n"
                "Additionally, when you gain a level in this class, you can choose one of the warlock spells you know and replace it with another spell from the warlock spell list, which also must be of a level for which you have spell slots. \n \n"
                "#### Spellcasting Ability \n \n"
                "Charisma is your spellcasting ability for your warlock spells, so you use your Charisma whenever a spell refers to your spellcasting ability. In addition, you use your Charisma modifier when setting the saving throw DC for a warlock spell you cast and when making an attack roll with one. \n \n"
                "**Spell save DC** = 8 + your proficiency bonus + your Charisma modifier \n \n"
                "**Spell attack modifier** = your proficiency bonus + your Charisma modifier \n \n"
                "#### Spellcasting Focus \n \n"
                "You can use an arcane focus as a spellcasting focus for your warlock spells. \n \n"
                "### Eldritch Invocations \n \n"
                "In your study of occult lore, you have unearthed eldritch invocations, fragments of forbidden knowledge that imbue you with an abiding magical ability. \n \n"
                "At 2nd level, you gain two eldritch invocations of your choice. Your invocation options are detailed at the end of the class description. When you gain certain warlock levels, you gain additional invocations of your choice, as shown in the Invocations Known column of the Warlock table. \n \n"
                "Additionally, when you gain a level in this class, you can choose one of the invocations you know and replace it with another invocation that you could learn at that level. \n \n"
                "### Pact Boon \n \n"
                "At 3rd level, your otherworldly patron bestows a gift upon you for your loyal service. You gain one of the following features of your choice. \n \n"
                "#### Pact of the Chain \n \nYou learn the *find familiar* spell and can cast it as a ritual. The spell doesn't count against your number of spells known. \n \n"
                "When you cast the spell, you can choose one of the normal forms for your familiar or one of the following special forms: imp, pseudodragon, quasit, or sprite. \n \n"
                "Additionally, when you take the Attack action, you can forgo one of your own attacks to allow your familiar to make one attack of its own with its reaction. \n \n"
                "#### Pact of the Blade \n \n"
                "You can use your action to create a pact weapon in your empty hand. You can choose the form that this melee weapon takes each time you create it. You are proficient with it while you wield it. This weapon counts as magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage. \n \n"
                "Your pact weapon disappears if it is more than 5 feet away from you for 1 minute or more. It also disappears if you use this feature again, if you dismiss the weapon (no action required), or if you die. \n \n"
                "You can transform one magic weapon into your pact weapon by performing a special ritual while you hold the weapon. You perform the ritual over the course of 1 hour, which can be done during a short rest. You can then dismiss the weapon, shunting it into an extradimensional space, and it appears whenever you create your pact weapon thereafter. You can't affect an artifact or a sentient weapon in this way. The weapon ceases being your pact weapon if you die, if you perform the 1-hour ritual on a different weapon, or if you use a 1-hour ritual to break your bond to it. The weapon appears at your feet if it is in the extradimensional space when the bond breaks. \n \n"
                "#### Pact of the Tome \n \n"
                "Your patron gives you a grimoire called a Book of Shadows. When you gain this feature, choose three cantrips from any class's spell list (the three needn't be from the same list). While the book is on your person, you can cast those cantrips at will. They don't count against your number of cantrips known. If they don't appear on the warlock spell list, they are nonetheless warlock spells for you. \n \n"
                "If you lose your Book of Shadows, you can perform a 1-hour ceremony to receive a replacement from your patron. This ceremony can be performed during a short or long rest, and it destroys the previous book. The book turns to ash when you die. \n \n"
                "### Ability Score Improvement \n \n"
                "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature. \n \n"
                "### Mystic Arcanum \n \nAt 11th level, your patron bestows upon you a magical secret called an arcanum. Choose one 6th- level spell from the warlock spell list as this arcanum. \n \n"
                "You can cast your arcanum spell once without expending a spell slot. You must finish a long rest before you can do so again. \n \n"
                "At higher levels, you gain more warlock spells of your choice that can be cast in this way: one 7th- level spell at 13th level, one 8th-level spell at 15th level, and one 9th-level spell at 17th level. You regain all uses of your Mystic Arcanum when you finish a long rest. \n \n"
                "### Eldritch Master \n \n"
                "At 20th level, you can draw on your inner reserve of mystical power while entreating your patron to regain expended spell slots. You can spend 1 minute entreating your patron for aid to regain all your expended spell slots from your Pact Magic feature. Once you regain spell slots with this feature, you must finish a long rest before you can do so again. \n \n"
                "### Eldritch Invocations \n \n"
                "If an eldritch invocation has prerequisites, you must meet them to learn it. You can learn the invocation at the same time that you meet its prerequisites. A level prerequisite refers to your level in this class. \n \n"
                "#### Agonizing Blast \n \n"
                "*Prerequisite:* eldritch blast *cantrip* \n \n"
                "When you cast *eldritch blast*, add your Charisma modifier to the damage it deals on a hit. \n \n"
                "#### Armor of Shadows \n \n"
                "You can cast *mage armor* on yourself at will, without expending a spell slot or material components. \n \n"
                "#### Ascendant Step \n \n"
                "*Prerequisite: 9th level* \n \n"
                "You can cast *levitate* on yourself at will, without expending a spell slot or material components. \n \n"
                "#### Beast Speech \n \n"
                "You can cast *speak with animals* at will, without expending a spell slot. \n \n"
                "#### Beguiling Influence \n \n"
                "You gain proficiency in the Deception and Persuasion skills. \n \n"
                "#### Bewitching Whispers \n \n"
                "*Prerequisite: 7th level* \n \n"
                "You can cast *compulsion* once using a warlock spell slot. You can't do so again until you finish a long rest. \n \n"
                "#### Book of Ancient Secrets \n \n"
                "*Prerequisite: Pact of the Tome feature* \n \n"
                "You can now inscribe magical rituals in your Book of Shadows. Choose two 1st-level spells that have the ritual tag from any class's spell list (the two needn't be from the same list). The spells appear in the book and don't count against the number of spells you know. With your Book of Shadows in hand, you can cast the chosen spells as rituals. You can't cast the spells except as rituals, unless you've learned them by some other means. You can also cast a warlock spell you know as a ritual if it has the ritual tag. \n \nOn your adventures, you can add other ritual spells to your Book of Shadows. When you find such a spell, you can add it to the book if the spell's level is equal to or less than half your warlock level (rounded up) and if you can spare the time to transcribe the spell. For each level of the spell, the transcription process takes 2 hours and costs 50 gp for the rare inks needed to inscribe it. \n \n#### Chains of Carceri \n \n*Prerequisite: 15th level, Pact of the Chain feature* \n \nYou can cast *hold monster* at will-targeting a celestial, fiend, or elemental-without expending a spell slot or material components. You must finish a long rest before you can use this invocation on the same creature again. \n \n#### Devil's Sight \n \nYou can see normally in darkness, both magical and nonmagical, to a distance of 120 feet. \n \n#### Dreadful Word \n \n*Prerequisite: 7th level* \n \nYou can cast *confusion* once using a warlock spell slot. You can't do so again until you finish a long rest. \n \n#### Eldritch Sight \n \nYou can cast *detect magic* at will, without expending a spell slot. \n \n#### Eldritch Spear \n \n*Prerequisite:* eldritch blast *cantrip* \n \nWhen you cast *eldritch blast*, its range is 300 feet. \n \n#### Eyes of the Rune Keeper \n \nYou can read all writing. \n \n#### Fiendish Vigor \n \nYou can cast *false life* on yourself at will as a 1st-level spell, without expending a spell slot or material components. \n \n#### Gaze of Two Minds \n \nYou can use your action to touch a willing humanoid and perceive through its senses until the end of your next turn. As long as the creature is on the same plane of existence as you, you can use your action on subsequent turns to maintain this connection, extending the duration until the end of your next turn. While perceiving through the other creature's senses, you benefit from any special senses possessed by that creature, and you are blinded and deafened to your own surroundings. \n \n#### Lifedrinker \n \n*Prerequisite: 12th level, Pact of the Blade feature* \n \nWhen you hit a creature with your pact weapon, the creature takes extra necrotic damage equal to your Charisma modifier (minimum 1). \n \n"
                "#### Mask of Many Faces \n \n"
                "You can cast *disguise self* at will, without expending a spell slot. \n \n"
                "#### Master of Myriad Forms \n \n"
                "*Prerequisite: 15th level* \n \n"
                "You can cast *alter self* at will, without expending a spell slot. \n \n"
                "#### Minions of Chaos \n \n*Prerequisite: 9th level* \n \n"
                "You can cast *conjure elemental* once using a warlock spell slot. You can't do so again until you finish a long rest. \n \n"
                "#### Mire the Mind \n \n"
                "*Prerequisite: 5th level* \n \n"
                "You can cast *slow* once using a warlock spell slot. You can't do so again until you finish a long rest. \n \n"
                "#### Misty Visions \n \n"
                "You can cast *silent image* at will, without expending a spell slot or material components. \n \n"
                "#### One with Shadows \n \n"
                "*Prerequisite: 5th level* \n \n"
                "When you are in an area of dim light or darkness, you can use your action to become invisible until you move or take an action or a reaction. \n \n"
                "#### Otherworldly Leap \n \n"
                "*Prerequisite: 9th level* \n \n"
                "You can cast *jump* on yourself at will, without expending a spell slot or material components. \n \n"
                "#### Repelling Blast \n \n"
                "*Prerequisite:* eldritch blast *cantrip* \n \n"
                "When you hit a creature with *eldritch blast*, you can push the creature up to 10 feet away from you in a straight line. \n \n"
                "#### Sculptor of Flesh \n \n"
                "*Prerequisite: 7th level* \n \n"
                "You can cast *polymorph* once using a warlock spell slot. You can't do so again until you finish a long rest. \n \n"
                "#### Sign of Ill Omen \n \n"
                "*Prerequisite: 5th level* \n \n"
                "You can cast *bestow curse* once using a warlock spell slot. You can't do so again until you finish a long rest. \n \n"
                "#### Thief of Five Fates \n \n"
                "You can cast *bane* once using a warlock spell slot. You can't do so again until you finish a long rest. \n \n"
                "#### Thirsting Blade \n \n*Prerequisite: 5th level, Pact of the Blade feature* \n \n"
                "You can attack with your pact weapon twice, instead of once, whenever you take the Attack action on your turn. \n \n"
                "#### Visions of Distant Realms \n \n"
                "*Prerequisite: 15th level* \n \n"
                "You can cast *arcane eye* at will, without expending a spell slot. \n \n"
                "#### Voice of the Chain Master \n \n"
                "*Prerequisite: Pact of the Chain feature* \n \n"
                "You can communicate telepathically with your familiar and perceive through your familiar's senses as long as you are on the same plane of existence. Additionally, while perceiving through your familiar's senses, you can also speak through your familiar in your own voice, even if your familiar is normally incapable of speech. \n \n"
                "#### Whispers of the Grave \n \n"
                "*Prerequisite: 9th level* \n \n"
                "You can cast *speak with dead* at will, without expending a spell slot. \n \n"
                "#### Witch Sight \n \n"
                "*Prerequisite: 15th level* \n \n"
                "You can see the true form of any shapechanger or creature concealed by illusion or transmutation magic while the creature is within 30 feet of you and within line of sight. \n \n"
                "### Otherworldly Patrons \n \n"
                "The beings that serve as patrons for warlocks are mighty inhabitants of other planes of existence-not gods, but almost godlike in their power. Various patrons give their warlocks access to different powers and invocations, and expect significant favors in return. \n \n"
                "Some patrons collect warlocks, doling out mystic knowledge relatively freely or boasting of their ability to bind mortals to their will. Other patrons bestow their power only grudgingly, and might make a pact with only one warlock. Warlocks who serve the same patron might view each other as allies, siblings, or rivals.",
        "hit_dice": "1d8",
        "hp_at_1st_level": "8 + your Constitution modifier",
        "hp_at_higher_levels": "1d8 (or 5) + your Constitution modifier per warlock level after 1st",
        "prof_armor": "Light armor",
        "prof_weapons": "Simple weapons",
        "prof_tools": "None",
        "prof_saving_throws": "Wisdom, Charisma",
        "prof_skills": "Choose two skills from Arcana, Deception, History, Intimidation, Investigation, Nature, and Religion",
        "equipment": "You start with the following equipment, in addition to the equipment granted by your background: \n"
                     "* *(a)* a light crossbow and 20 bolts or (*b*) any simple weapon \n"
                     "* *(a)* a component pouch or (*b*) an arcane focus \n"
                     "* *(a)* a scholar's pack or (*b*) a dungeoneer's pack \n"
                     "* Leather armor, any simple weapon, and two daggers",
        "table": "| Level | Proficiency Bonus | Features                        | Cantrips Known | Spells Known | Spell Slots | Slot Level | Invocations Known | \n"
                 "|-------|-------------------|---------------------------------|----------------|--------------|-------------|------------|-------------------| \n"
                 "| 1st   | +2                | Otherworldly Patron, Pact Magic | 2              | 2            | 1           | 1st        | -                 | \n"
                 "| 2nd   | +2                | Eldritch Invocations            | 2              | 3            | 2           | 1st        | 2                 | \n"
                 "| 3rd   | +2                | Pact Boon                       | 2              | 4            | 2           | 2nd        | 2                 | \n"
                 "| 4th   | +2                | Ability Score Improvement       | 3              | 5            | 2           | 2nd        | 2                 | \n"
                 "| 5th   | +3                | -                               | 3              | 6            | 2           | 3rd        | 3                 | \n"
                 "| 6th   | +3                | Otherworldly Patron feature     | 3              | 7            | 2           | 3rd        | 3                 | \n"
                 "| 7th   | +3                | -                               | 3              | 8            | 2           | 4th        | 4                 | \n"
                 "| 8th   | +3                | Ability Score Improvement       | 3              | 9            | 2           | 4th        | 4                 | \n"
                 "| 9th   | +4                | -                               | 3              | 10           | 2           | 5th        | 5                 | \n"
                 "| 10th  | +4                | Otherworldly Patron feature     | 4              | 10           | 2           | 5th        | 5                 | \n"
                 "| 11th  | +4                | Mystic Arcanum (6th level)      | 4              | 11           | 3           | 5th        | 5                 | \n"
                 "| 12th  | +4                | Ability Score Improvement       | 4              | 11           | 3           | 5th        | 6                 | \n"
                 "| 13th  | +5                | Mystic Arcanum (7th level)      | 4              | 12           | 3           | 5th        | 6                 | \n"
                 "| 14th  | +5                | Otherworldly Patron feature     | 4              | 12           | 3           | 5th        | 6                 | \n"
                 "| 15th  | +5                | Mystic Arcanum (8th level)      | 4              | 13           | 3           | 5th        | 7                 | \n"
                 "| 16th  | +5                | Ability Score Improvement       | 4              | 13           | 3           | 5th        | 7                 | \n"
                 "| 17th  | +6                | Mystic Arcanum (9th level)      | 4              | 14           | 4           | 5th        | 7                 | \n"
                 "| 18th  | +6                | -                               | 4              | 14           | 4           | 5th        | 8                 | \n"
                 "| 19th  | +6                | Ability Score Improvement       | 4              | 15           | 4           | 5th        | 8                 | \n"
                 "| 20th  | +6                | Eldritch Master                 | 4              | 15           | 4           | 5th        | 8                 |",
        "spellcasting_ability": "Charisma",
        "subtypes_name": "Otherworldly Patrons",
        "archetypes": [
            {
                "name": "The Fiend",
                "slug": "the-fiend",
                "desc": "You have made a pact with a fiend from the lower planes of existence, a being whose aims are evil, even if you strive against those aims. Such beings desire the corruption or destruction of all things, ultimately including you. Fiends powerful enough to forge a pact include demon lords such as Demogorgon, Orcus, Fraz'Urb-luu, and Baphomet; archdevils such as Asmodeus, Dispater, Mephistopheles, and Belial; pit fiends and balors that are especially mighty; and ultroloths and other lords of the yugoloths. \n \n"
                        "##### Expanded Spell List \n \n"
                        "The Fiend lets you choose from an expanded list of spells when you learn a warlock spell. The following spells are added to the warlock spell list for you. \n \n"
                        "**Fiend Expanded Spells (table)** \n \n"
                        "| Spell Level | Spells                            | \n"
                        "|-------------|-----------------------------------| \n"
                        "| 1st         | burning hands, command            | \n"
                        "| 2nd         | blindness/deafness, scorching ray | \n"
                        "| 3rd         | fireball, stinking cloud          | \n"
                        "| 4th         | fire shield, wall of fire         | \n"
                        "| 5th         | flame strike, hallow              | \n \n"
                        "##### Dark One's Blessing \n \n"
                        "Starting at 1st level, when you reduce a hostile creature to 0 hit points, you gain temporary hit points equal to your Charisma modifier + your warlock level (minimum of 1). \n \n"
                        "##### Dark One's Own Luck \n \n"
                        "Starting at 6th level, you can call on your patron to alter fate in your favor. When you make an ability check or a saving throw, you can use this feature to add a d10 to your roll. You can do so after seeing the initial roll but before any of the roll's effects occur. \n \n"
                        "Once you use this feature, you can't use it again until you finish a short or long rest. \n \n"
                        "##### Fiendish Resilience \n \n"
                        "Starting at 10th level, you can choose one damage type when you finish a short or long rest. You gain resistance to that damage type until you choose a different one with this feature. Damage from magical weapons or silver weapons ignores this resistance. \n \n"
                        "##### Hurl Through Hell \n \n"
                        "Starting at 14th level, when you hit a creature with an attack, you can use this feature to instantly transport the target through the lower planes. The creature disappears and hurtles through a nightmare landscape. \n \n"
                        "At the end of your next turn, the target returns to the space it previously occupied, or the nearest unoccupied space. If the target is not a fiend, it takes 10d10 psychic damage as it reels from its horrific experience. \n \n"
                        "Once you use this feature, you can't use it again until you finish a long rest. \n \n"
                        "> ### Your Pact Boon \n> \n"
                        "> Each Pact Boon option produces a special creature or an object that reflects your patron's nature. \n> \n"
                        "> **_Pact of the Chain._** Your familiar is more cunning than a typical familiar. Its default form can be a reflection of your patron, with sprites and pseudodragons tied to the Archfey and imps and quasits tied to the Fiend. Because the Great Old One's nature is inscrutable, any familiar form is suitable for it. \n> \n"
                        "> **_Pact of the Blade._** If your patron is the Archfey, your weapon might be a slender blade wrapped in leafy vines. If you serve the Fiend, your weapon could be an axe made of black metal and adorned with decorative flames. If your patron is the Great Old One, your weapon might be an ancient-looking spear, with a gemstone embedded in its head, carved to look like a terrible unblinking eye. \n> \n"
                        "> **_Pact of the Tome._** Your Book of Shadows might be a fine, gilt-edged tome with spells of enchantment and illusion, gifted to you by the lordly Archfey. It could be a weighty tome bound in demon hide studded with iron, holding spells of conjuration and a wealth of forbidden lore about the sinister regions of the cosmos, a gift of the Fiend. Or it could be the tattered diary of a lunatic driven mad by contact with the Great Old One, holding scraps of spells that only your own burgeoning insanity allows you to understand and cast.",
                "document__slug": "wotc-srd",
                "document__title": "Systems Reference Document",
                "document__license_url": "http://open5e.com/legal"
            }
        ],
        "document__slug": "wotc-srd",
        "document__title": "Systems Reference Document",
        "document__license_url": "http://open5e.com/legal"
    },
    "wizard": {
        "name": "Wizard",
        "slug": "wizard",
        "desc": "### Spellcasting \n \n"
                "As a student of arcane magic, you have a spellbook containing spells that show the first glimmerings of your true power. \n \n"
                "#### Cantrips \n \n"
                "At 1st level, you know three cantrips of your choice from the wizard spell list. You learn additional wizard cantrips of your choice at higher levels, as shown in the Cantrips Known column of the Wizard table. \n \n"
                "#### Spellbook \n \n"
                "At 1st level, you have a spellbook containing six 1st- level wizard spells of your choice. Your spellbook is the repository of the wizard spells you know, except your cantrips, which are fixed in your mind. \n \n"
                "#### Preparing and Casting Spells \n \n"
                "The Wizard table shows how many spell slots you have to cast your spells of 1st level and higher. To cast one of these spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest. \n \n"
                "You prepare the list of wizard spells that are available for you to cast. To do so, choose a number of wizard spells from your spellbook equal to your Intelligence modifier + your wizard level (minimum of one spell). The spells must be of a level for which you have spell slots. \n \n"
                "For example, if you're a 3rd-level wizard, you have four 1st-level and two 2nd-level spell slots. With an Intelligence of 16, your list of prepared spells can include six spells of 1st or 2nd level, in any combination, chosen from your spellbook. If you prepare the 1st-level spell *magic missile,* you can cast it using a 1st-level or a 2nd-level slot. Casting the spell doesn't remove it from your list of prepared spells. \n \n"
                "You can change your list of prepared spells when you finish a long rest. Preparing a new list of wizard spells requires time spent studying your spellbook and memorizing the incantations and gestures you must make to cast the spell: at least 1 minute per spell level for each spell on your list. \n \n"
                "#### Spellcasting Ability \n \n"
                "Intelligence is your spellcasting ability for your wizard spells, since you learn your spells through dedicated study and memorization. You use your Intelligence whenever a spell refers to your spellcasting ability. In addition, you use your Intelligence modifier when setting the saving throw DC for a wizard spell you cast and when making an attack roll with one. \n \n"
                "**Spell save DC** = 8 + your proficiency bonus + your Intelligence modifier \n \n"
                "**Spell attack modifier** = your proficiency bonus + your Intelligence modifier \n \n"
                "#### Ritual Casting \n \n"
                "You can cast a wizard spell as a ritual if that spell has the ritual tag and you have the spell in your spellbook. You don't need to have the spell prepared. \n \n"
                "#### Spellcasting Focus \n \n"
                "You can use an arcane focus as a spellcasting focus for your wizard spells. \n \n"
                "#### Learning Spells of 1st Level and Higher \n \n"
                "Each time you gain a wizard level, you can add two wizard spells of your choice to your spellbook for free. Each of these spells must be of a level for which you have spell slots, as shown on the Wizard table. On your adventures, you might find other spells that you can add to your spellbook (see the “Your Spellbook” sidebar). \n \n"
                "### Arcane Recovery \n \n"
                "You have learned to regain some of your magical energy by studying your spellbook. Once per day when you finish a short rest, you can choose expended spell slots to recover. The spell slots can have a combined level that is equal to or less than half your wizard level (rounded up), and none of the slots can be 6th level or higher. \n \n"
                "For example, if you're a 4th-level wizard, you can recover up to two levels worth of spell slots. You can recover either a 2nd-level spell slot or two 1st-level spell slots. \n \n"
                "### Arcane Tradition \n \n"
                "When you reach 2nd level, you choose an arcane tradition, shaping your practice of magic through one of eight schools: Abjuration, Conjuration, Divination, Enchantment, Evocation, Illusion, Necromancy, or Transmutation, all detailed at the end of the class description. \n \n"
                "Your choice grants you features at 2nd level and again at 6th, 10th, and 14th level. \n \n"
                "### Ability Score Improvement \n \n"
                "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature. \n \n"
                "### Spell Mastery \n \n"
                "At 18th level, you have achieved such mastery over certain spells that you can cast them at will. Choose a 1st-level wizard spell and a 2nd-level wizard spell that are in your spellbook. You can cast those spells at their lowest level without expending a spell slot when you have them prepared. If you want to cast either spell at a higher level, you must expend a spell slot as normal. \n \n"
                "By spending 8 hours in study, you can exchange one or both of the spells you chose for different spells of the same levels. \n \n"
                "### Signature Spells \n \n"
                "When you reach 20th level, you gain mastery over two powerful spells and can cast them with little effort. Choose two 3rd-level wizard spells in your spellbook as your signature spells. You always have these spells prepared, they don't count against the number of spells you have prepared, and you can cast each of them once at 3rd level without expending a spell slot. When you do so, you can't do so again until you finish a short or long rest. \n \n"
                "If you want to cast either spell at a higher level, you must expend a spell slot as normal. \n \n"
                "### Arcane Traditions \n \n"
                "The study of wizardry is ancient, stretching back to the earliest mortal discoveries of magic. It is firmly established in fantasy gaming worlds, with various traditions dedicated to its complex study. \n \n"
                "The most common arcane traditions in the multiverse revolve around the schools of magic. Wizards through the ages have cataloged thousands of spells, grouping them into eight categories called schools. In some places, these traditions are literally schools; a wizard might study at the School of Illusion while another studies across town at the School of Enchantment. In other institutions, the schools are more like academic departments, with rival faculties competing for students and funding. Even wizards who train apprentices in the solitude of their own towers use the division of magic into schools as a learning device, since the spells of each school require mastery of different techniques.",
        "hit_dice": "1d6",
        "hp_at_1st_level": "6 + your Constitution modifier",
        "hp_at_higher_levels": "1d6 (or 4) + your Constitution modifier per wizard level after 1st",
        "prof_armor": "None",
        "prof_weapons": "Daggers, darts, slings, quarterstaffs, light crossbows",
        "prof_tools": "None",
        "prof_saving_throws": "Intelligence, Wisdom",
        "prof_skills": "Choose two from Arcana, History, Insight, Investigation, Medicine, and Religion",
        "equipment": "You start with the following equipment, in addition to the equipment granted by your background: \n"
                     "* *(a)* a quarterstaff or (*b*) a dagger \n"
                     "* *(a)* a component pouch or (*b*) an arcane focus \n"
                     "* *(a)* a scholar's pack or (*b*) an explorer's pack \n"
                     "* A spellbook",
        "table": "| Level | Proficiency Bonus | Features                       | Cantrips Known | 1st | 2nd | 3rd | 4th | 5th | 6th | 7th | 8th | 9th | \n"
                 "|-------|-------------------|--------------------------------|----------------|-----|-----|-----|-----|-----|-----|-----|-----|-----| \n"
                 "| 1st   | +2                | Spellcasting, Arcane Recovery  | 3              | 2   | -   | -   | -   | -   | -   | -   | -   | -   | \n"
                 "| 2nd   | +2                | Arcane Tradition               | 3              | 3   | -   | -   | -   | -   | -   | -   | -   | -   | \n"
                 "| 3rd   | +2                | -                              | 3              | 4   | 2   | -   | -   | -   | -   | -   | -   | -   | \n"
                 "| 4th   | +2                | Ability Score Improvement      | 4              | 4   | 3   | -   | -   | -   | -   | -   | -   | -   | \n"
                 "| 5th   | +3                | -                              | 4              | 4   | 3   | 2   | -   | -   | -   | -   | -   | -   | \n"
                 "| 6th   | +3                | Arcane Tradition Feature       | 4              | 4   | 3   | 3   | -   | -   | -   | -   | -   | -   | \n"
                 "| 7th   | +3                | -                              | 4              | 4   | 3   | 3   | 1   | -   | -   | -   | -   | -   | \n"
                 "| 8th   | +3                | Ability Score Improvement      | 4              | 4   | 3   | 3   | 2   | -   | -   | -   | -   | -   | \n"
                 "| 9th   | +4                | -                              | 4              | 4   | 3   | 3   | 3   | 1   | -   | -   | -   | -   | \n"
                 "| 10th  | +4                | Arcane Tradition Feature       | 5              | 4   | 3   | 3   | 3   | 2   | -   | -   | -   | -   | \n"
                 "| 11th  | +4                | -                              | 5              | 4   | 3   | 3   | 3   | 2   | 1   | -   | -   | -   | \n"
                 "| 12th  | +4                | Ability Score Improvement      | 5              | 4   | 3   | 3   | 3   | 2   | 1   | -   | -   | -   | \n"
                 "| 13th  | +5                | -                              | 5              | 4   | 3   | 3   | 3   | 2   | 1   | 1   | -   | -   | \n"
                 "| 14th  | +5                | Arcane Tradition Feature       | 5              | 4   | 3   | 3   | 3   | 2   | 1   | 1   | -   | -   | \n"
                 "| 15th  | +5                | -                              | 5              | 4   | 3   | 3   | 3   | 2   | 1   | 1   | 1   | -   | \n"
                 "| 16th  | +5                | Ability Score Improvement      | 5              | 4   | 3   | 3   | 3   | 2   | 1   | 1   | 1   | -   | \n"
                 "| 17th  | +6                | -                              | 5              | 4   | 3   | 3   | 3   | 2   | 1   | 1   | 1   | 1   | \n"
                 "| 18th  | +6                | Spell Mastery                  | 5              | 4   | 3   | 3   | 3   | 3   | 1   | 1   | 1   | 1   | \n"
                 "| 19th  | +6                | Ability Score Improvement      | 5              | 4   | 3   | 3   | 3   | 3   | 2   | 1   | 1   | 1   | \n"
                 "| 20th  | +6                | Signature Spell                | 5              | 4   | 3   | 3   | 3   | 3   | 2   | 2   | 1   | 1   |",
        "spellcasting_ability": "Intelligence",
        "subtypes_name": "Arcane Traditions",
        "archetypes": [
            {
                "name": "School of Evocation",
                "slug": "school-of-evocation",
                "desc": "You focus your study on magic that creates powerful elemental effects such as bitter cold, searing flame, rolling thunder, crackling lightning, and burning acid. Some evokers find employment in military forces, serving as artillery to blast enemy armies from afar. Others use their spectacular power to protect the weak, while some seek their own gain as bandits, adventurers, or aspiring tyrants. \n \n"
                        "##### Evocation Savant \n \n"
                        "Beginning when you select this school at 2nd level, the gold and time you must spend to copy an evocation spell into your spellbook is halved. \n \n"
                        "##### Sculpt Spells \n \n"
                        "Beginning at 2nd level, you can create pockets of relative safety within the effects of your evocation spells. When you cast an evocation spell that affects other creatures that you can see, you can choose a number of them equal to 1 + the spell's level. The chosen creatures automatically succeed on their saving throws against the spell, and they take no damage if they would normally take half damage on a successful save. \n \n"
                        "##### Potent Cantrip \n \n"
                        "Starting at 6th level, your damaging cantrips affect even creatures that avoid the brunt of the effect. When a creature succeeds on a saving throw against your cantrip, the creature takes half the cantrip's damage (if any) but suffers no additional effect from the cantrip. \n \n"
                        "##### Empowered Evocation \n \n"
                        "Beginning at 10th level, you can add your Intelligence modifier to one damage roll of any wizard evocation spell you cast. \n \n"
                        "##### Overchannel \n \n"
                        "Starting at 14th level, you can increase the power of your simpler spells. When you cast a wizard spell of 1st through 5th level that deals damage, you can deal maximum damage with that spell. \n \n"
                        "The first time you do so, you suffer no adverse effect. If you use this feature again before you finish a long rest, you take 2d12 necrotic damage for each level of the spell, immediately after you cast it. Each time you use this feature again before finishing a long rest, the necrotic damage per spell level increases by 1d12. This damage ignores resistance and immunity. \n \n"
                        "> ### Your Spellbook \n> \n"
                        "> The spells that you add to your spellbook as you gain levels reflect the arcane research you conduct on your own, as well as intellectual breakthroughs you have had about the nature of the multiverse. You might find other spells during your adventures. You could discover a spell recorded on a scroll in an evil wizard's chest, for example, or in a dusty tome in an ancient library. \n> \n"
                        "> **_Copying a Spell into the Book._** When you find a wizard spell of 1st level or higher, you can add it to your spellbook if it is of a spell level you can prepare and if you can spare the time to decipher and copy it. \n> \n"
                        "> Copying that spell into your spellbook involves reproducing the basic form of the spell, then deciphering the unique system of notation used by the wizard who wrote it. You must practice the spell until you understand the sounds or gestures required, then transcribe it into your spellbook using your own notation. \n> \n"
                        "> For each level of the spell, the process takes 2 hours and costs 50 gp. The cost represents material components you expend as you experiment with the spell to master it, as well as the fine inks you need to record it. Once you have spent this time and money, you can prepare the spell just like your other spells. \n> \n"
                        "> **_Replacing the Book._** You can copy a spell from your own spellbook into another book-for example, if you want to make a backup copy of your spellbook. This is just like copying a new spell into your spellbook, but faster and easier, since you understand your own notation and already know how to cast the spell. You need spend only 1 hour and 10 gp for each level of the copied spell. \n> \n"
                        "> If you lose your spellbook, you can use the same procedure to transcribe the spells that you have prepared into a new spellbook. Filling out the remainder of your spellbook requires you to find new spells to do so, as normal. For this reason, many wizards keep backup spellbooks in a safe place. \n> \n"
                        "> **_The Book's Appearance._** Your spellbook is a unique compilation of spells, with its own decorative flourishes and margin notes. It might be a plain, functional leather volume that you received as a gift from your master, a finely bound gilt-edged tome you found in an ancient library, or even a loose collection of notes scrounged together after you lost your previous spellbook in a mishap.",
                "document__slug": "wotc-srd",
                "document__title": "Systems Reference Document",
                "document__license_url": "http://open5e.com/legal"
            }
        ],
        "document__slug": "wotc-srd",
        "document__title": "Systems Reference Document",
        "document__license_url": "http://open5e.com/legal"
    }
}

skill_list = {
    "athletics": {
        "name": "athletics",
        "aliases": ["Athletics"]
    },
    "acrobatics": {
        "name": "acrobatics",
        "aliases": [
            "Acrobatics"
        ]
    },
    "sleight of hand": {
        "name": "sleight of hand",
        "aliases": [
            "sleight_of_hand",
            "Sleight of hand",
            "Sleight of Hand",
            "SOH",
            "soh",
            "SoH"
        ]
    },
    "stealth": {
        "name": "stealth",
        "aliases": [
            "Stealth",
            "Sneaky",
            "Sneak",
            "sneak"
        ]
    },
    "arcana": {
        "name": "arcana",
        "aliases": [
            "Arcana"
        ]
    },
    "history": {
        "name": "history",
        "aliases": [
            "History"
        ]
    },
    "investigation": {
        "name": "investigation",
        "aliases": [
            "Investigation"
        ]
    },
    "nature": {
        "name": "nature",
        "aliases": [
            "Nature"
        ]
    },
    "religion": {
        "name": "religion",
        "aliases": [
            "Religion",
            "Jesus",
            "jesus"
        ]
    },
    "animal handling": {
        "name": "animal handling",
        "aliases": [
            "Animal handling",
            "animal Handling",
            "Animal Handling",
            "animal_handling",
            "Animal_handling",
            "animal_Handling",
            "Animal_Handling",
            "ah",
            "AH",
            "a_h",
            "A_h",
            "a_H",
            "A_H"
        ]
    },
    "insight": {
        "name": "insight",
        "aliases": [
            "Insight"
        ]
    },
    "medicine": {
        "name": "medicine",
        "aliases": [
            "Medicine"
        ]
    },
    "perception": {
        "name": "perception",
        "aliases": [
            "Perception"
        ]
    },
    "survival": {
        "name": "survival",
        "aliases": [
            "Survival"
        ]
    },
    "deception": {
        "name": "deception",
        "aliases": [
            "Deception"
        ]
    },
    "intimidation": {
        "name": "intimidation",
        "aliases": [
            "Intimidation",
            "Rawr",
            "rawr",
            "Rawr XD",
            "rawr xd"
        ]
    },
    "performance": {
        "name": "performance",
        "aliases": [
            "Performance"
        ]
    },
    "persuasion": {
        "name": "persuasion",
        "aliases": [
            "Persuasion"
        ]
    }
}

alignment_list = {
    "chaotic_evil": {
        "name": "chaotic_evil",
        "aliases": {
            "chaotic evil",
            "ce",
            "c_e"
        }
    },
    "chaotic_neutral": {
        "name": "chaotic_neutral",
        "aliases": {
            "chaotic neutral",
            "cn",
            "c_n"
        }
    },
    "chaotic_good": {
        "name": "chaotic_good",
        "aliases": {
            "chaotic good",
            "cg",
            "c_g"
        }
    },
    "neutral_evil": {
        "name": "neutral_evil",
        "aliases": {
            "neutral evil",
            "ne",
            "n_e"
        }
    },
    "neutral_neutral": {
        "name": "neutral_neutral",
        "aliases": {
            "neutral neutral",
            "nn",
            "n_n"
        }
    },
    "neutral_good": {
        "name": "neutral_good",
        "aliases": {
            "neutral good",
            "ng",
            "n_g"
        }
    },
    "lawful_evil": {
        "name": "lawful_evil",
        "aliases": {
            "lawful evil",
            "le",
            "l_e"
        }
    },
    "lawful_neutral": {
        "name": "lawful_neutral",
        "aliases": {
            "lawful neutral",
            "ln",
            "l_n"
        }
    },
    "lawful_good": {
        "name": "lawful_good",
        "aliases": {
            "lawful good",
            "lg",
            "l_g"
        }
    },
}

# https://media.wizards.com/2014/downloads/dnd/MM_MonstersCR.pdf
# https://api.open5e.com/monsters/
monster_list = {
    "0": {
        "awakened-shrub": {
            "slug": "awakened-shrub",
            "name": "Awakened Shrub",
            "size": "Small",
            "type": "plant",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 9,
            "armor_desc": "null",
            "hit_points": 10,
            "hit_dice": "3d6",
            "speed": {
                "walk": 20
            },
            "strength": 3,
            "dexterity": 8,
            "constitution": 11,
            "intelligence": 10,
            "wisdom": 10,
            "charisma": 6,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "fire",
            "damage_resistances": "piercing",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 10",
            "languages": "one language known by its creator",
            "challenge_rating": "0",
            "actions": [
                {
                    "name": "Rake",
                    "desc": "Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 1 (1d4 - 1) slashing damage.",
                    "attack_bonus": 1,
                    "damage_dice": "1d4",
                    "damage_bonus": -1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "False Appearance",
                    "desc": "While the shrub remains motionless, it is indistinguishable from a normal shrub."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "baboon": {
            "slug": "baboon",
            "name": "Baboon",
            "size": "Small",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 12,
            "armor_desc": "null",
            "hit_points": 3,
            "hit_dice": "1d6",
            "speed": {
                "walk": 30,
                "climb": 30
            },
            "strength": 8,
            "dexterity": 14,
            "constitution": 11,
            "intelligence": 4,
            "wisdom": 12,
            "charisma": 6,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 11",
            "languages": "",
            "challenge_rating": "0",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 1 (1d4 - 1) piercing damage.",
                    "attack_bonus": 1,
                    "damage_dice": "1d4",
                    "damage_bonus": -1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Pack Tactics",
                    "desc": "The baboon has advantage on an attack roll against a creature if at least one of the baboon's allies is within 5 ft. of the creature and the ally isn't incapacitated."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "badger": {
            "slug": "badger",
            "name": "Badger",
            "size": "Tiny",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 10,
            "armor_desc": "null",
            "hit_points": 3,
            "hit_dice": "1d4",
            "speed": {
                "walk": 20,
                "burrow": 5
            },
            "strength": 4,
            "dexterity": 11,
            "constitution": 12,
            "intelligence": 2,
            "wisdom": 12,
            "charisma": 5,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 30 ft., passive Perception 11",
            "languages": "",
            "challenge_rating": "0",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 1 piercing damage.",
                    "attack_bonus": 2,
                    "damage_bonus": 1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Keen Smell",
                    "desc": "The badger has advantage on Wisdom (Perception) checks that rely on smell."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "bat": {
            "slug": "bat",
            "name": "Bat",
            "size": "Tiny",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 12,
            "armor_desc": "null",
            "hit_points": 1,
            "hit_dice": "1d4",
            "speed": {
                "walk": 5,
                "fly": 30
            },
            "strength": 2,
            "dexterity": 15,
            "constitution": 8,
            "intelligence": 2,
            "wisdom": 12,
            "charisma": 4,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "blindsight 60 ft., passive Perception 11",
            "languages": "",
            "challenge_rating": "0",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +0 to hit, reach 5 ft., one creature. Hit: 1 piercing damage.",
                    "damage_bonus": 1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Echolocation",
                    "desc": "The bat can't use its blindsight while deafened."
                },
                {
                    "name": "Keen Hearing",
                    "desc": "The bat has advantage on Wisdom (Perception) checks that rely on hearing."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "cat": {
            "slug": "cat",
            "name": "Cat",
            "size": "Tiny",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 12,
            "armor_desc": "null",
            "hit_points": 2,
            "hit_dice": "1d4",
            "speed": {
                "walk": 40,
                "climb": 30
            },
            "strength": 3,
            "dexterity": 15,
            "constitution": 10,
            "intelligence": 3,
            "wisdom": 12,
            "charisma": 7,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 3,
            "skills": {
                "perception": 3,
                "stealth": 4
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 13",
            "languages": "",
            "challenge_rating": "0",
            "actions": [
                {
                    "name": "Claws",
                    "desc": "Melee Weapon Attack: +0 to hit, reach 5 ft., one target. Hit: 1 slashing damage.",
                    "damage_bonus": 1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Keen Smell",
                    "desc": "The cat has advantage on Wisdom (Perception) checks that rely on smell."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "commoner": {
            "slug": "commoner",
            "name": "Commoner",
            "size": "Medium",
            "type": "humanoid",
            "subtype": "any race",
            "group": "null",
            "alignment": "any alignment",
            "armor_class": 10,
            "armor_desc": "null",
            "hit_points": 4,
            "hit_dice": "1d8",
            "speed": {
                "walk": 30
            },
            "strength": 10,
            "dexterity": 10,
            "constitution": 10,
            "intelligence": 10,
            "wisdom": 10,
            "charisma": 10,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 10",
            "languages": "any one language (usually Common)",
            "challenge_rating": "0",
            "actions": [
                {
                    "name": "Club",
                    "desc": "Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 2 (1d4) bludgeoning damage.",
                    "attack_bonus": 2,
                    "damage_dice": "1d4"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": "",
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "crab": {
            "slug": "crab",
            "name": "Crab",
            "size": "Tiny",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 11,
            "armor_desc": "natural armor",
            "hit_points": 2,
            "hit_dice": "1d4",
            "speed": {
                "walk": 20,
                "swim": 20
            },
            "strength": 2,
            "dexterity": 11,
            "constitution": 10,
            "intelligence": 1,
            "wisdom": 8,
            "charisma": 2,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {
                "stealth": 2
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "blindsight 30 ft., passive Perception 9",
            "languages": "",
            "challenge_rating": "0",
            "actions": [
                {
                    "name": "Claw",
                    "desc": "Melee Weapon Attack: +0 to hit, reach 5 ft., one target. Hit: 1 bludgeoning damage.",
                    "damage_bonus": 1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Amphibious",
                    "desc": "The crab can breathe air and water."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "deer": {
            "slug": "deer",
            "name": "Deer",
            "size": "Medium",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 13,
            "armor_desc": "null",
            "hit_points": 4,
            "hit_dice": "1d8",
            "speed": {
                "walk": 50
            },
            "strength": 11,
            "dexterity": 16,
            "constitution": 11,
            "intelligence": 2,
            "wisdom": 14,
            "charisma": 5,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 12",
            "languages": "",
            "challenge_rating": "0",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 2 (1d4) piercing damage.",
                    "attack_bonus": 2,
                    "damage_dice": "1d4"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": "",
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "eagle": {
            "slug": "eagle",
            "name": "Eagle",
            "size": "Small",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 12,
            "armor_desc": "null",
            "hit_points": 3,
            "hit_dice": "1d6",
            "speed": {
                "walk": 10,
                "fly": 60
            },
            "strength": 6,
            "dexterity": 15,
            "constitution": 10,
            "intelligence": 2,
            "wisdom": 14,
            "charisma": 7,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 4,
            "skills": {
                "perception": 4
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 14",
            "languages": "",
            "challenge_rating": "0",
            "actions": [
                {
                    "name": "Talons",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) slashing damage.",
                    "attack_bonus": 4,
                    "damage_dice": "1d4",
                    "damage_bonus": 2
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Keen Sight",
                    "desc": "The eagle has advantage on Wisdom (Perception) checks that rely on sight."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "frog": {
            "slug": "frog",
            "name": "Frog",
            "size": "Tiny",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 11,
            "armor_desc": "null",
            "hit_points": 1,
            "hit_dice": "1d4",
            "speed": {
                "walk": 20,
                "swim": 20
            },
            "strength": 1,
            "dexterity": 13,
            "constitution": 8,
            "intelligence": 1,
            "wisdom": 8,
            "charisma": 3,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 1,
            "skills": {
                "perception": 1,
                "stealth": 3
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 30 ft., passive Perception 11",
            "languages": "",
            "challenge_rating": "0",
            "actions": "",
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Amphibious",
                    "desc": "The frog can breathe air and water"
                },
                {
                    "name": "Standing Leap",
                    "desc": "The frog's long jump is up to 10 ft. and its high jump is up to 5 ft., with or without a running start."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "giant-fire-beetle": {
            "slug": "giant-fire-beetle",
            "name": "Giant Fire Beetle",
            "size": "Small",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 13,
            "armor_desc": "natural armor",
            "hit_points": 4,
            "hit_dice": "1d6",
            "speed": {
                "walk": 30
            },
            "strength": 8,
            "dexterity": 10,
            "constitution": 12,
            "intelligence": 1,
            "wisdom": 7,
            "charisma": 3,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "blindsight 30 ft., passive Perception 8",
            "languages": "",
            "challenge_rating": "0",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 2 (1d6 - 1) slashing damage.",
                    "attack_bonus": 1,
                    "damage_dice": "1d6",
                    "damage_bonus": -1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Illumination",
                    "desc": "The beetle sheds bright light in a 10-foot radius and dim light for an additional 10 ft.."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "goat": {
            "slug": "goat",
            "name": "Goat",
            "size": "Medium",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 10,
            "armor_desc": "null",
            "hit_points": 4,
            "hit_dice": "1d8",
            "speed": {
                "walk": 40
            },
            "strength": 12,
            "dexterity": 10,
            "constitution": 11,
            "intelligence": 2,
            "wisdom": 10,
            "charisma": 5,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 10",
            "languages": "",
            "challenge_rating": "0",
            "actions": [
                {
                    "name": "Ram",
                    "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) bludgeoning damage.",
                    "attack_bonus": 3,
                    "damage_dice": "1d4",
                    "damage_bonus": 1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Charge",
                    "desc": "If the goat moves at least 20 ft. straight toward a target and then hits it with a ram attack on the same turn, the target takes an extra 2 (1d4) bludgeoning damage. If the target is a creature, it must succeed on a DC 10 Strength saving throw or be knocked prone.",
                    "attack_bonus": 0,
                    "damage_dice": "1d4"
                },
                {
                    "name": "Sure-Footed",
                    "desc": "The goat has advantage on Strength and Dexterity saving throws made against effects that would knock it prone."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "hawk": {
            "slug": "hawk",
            "name": "Hawk",
            "size": "Tiny",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 13,
            "armor_desc": "null",
            "hit_points": 1,
            "hit_dice": "1d4",
            "speed": {
                "walk": 10,
                "fly": 60
            },
            "strength": 5,
            "dexterity": 16,
            "constitution": 8,
            "intelligence": 2,
            "wisdom": 14,
            "charisma": 6,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 4,
            "skills": {
                "perception": 4
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 14",
            "languages": "",
            "challenge_rating": "0",
            "actions": [
                {
                    "name": "Talons",
                    "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 1 slashing damage.",
                    "attack_bonus": 5,
                    "damage_bonus": 1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Keen Sight",
                    "desc": "The hawk has advantage on Wisdom (Perception) checks that rely on sight."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "homunculus": {
            "slug": "homunculus",
            "name": "Homunculus",
            "size": "Tiny",
            "type": "construct",
            "subtype": "",
            "group": "null",
            "alignment": "neutral",
            "armor_class": 13,
            "armor_desc": "natural armor",
            "hit_points": 5,
            "hit_dice": "2d4",
            "speed": {
                "walk": 20,
                "fly": 40
            },
            "strength": 4,
            "dexterity": 15,
            "constitution": 11,
            "intelligence": 10,
            "wisdom": 10,
            "charisma": 7,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "poison",
            "condition_immunities": "charmed, poisoned",
            "senses": "darkvision 60 ft., passive Perception 10",
            "languages": "understands the languages of its creator but can't speak",
            "challenge_rating": "0",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 1 piercing damage, and the target must succeed on a DC 10 Constitution saving throw or be poisoned for 1 minute. If the saving throw fails by 5 or more, the target is instead poisoned for 5 (1d10) minutes and unconscious while poisoned in this way.",
                    "attack_bonus": 4,
                    "damage_bonus": 1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Telepathic Bond",
                    "desc": "While the homunculus is on the same plane of existence as its master, it can magically convey what it senses to its master, and the two can communicate telepathically."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "hyena": {
            "slug": "hyena",
            "name": "Hyena",
            "size": "Medium",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 11,
            "armor_desc": "null",
            "hit_points": 5,
            "hit_dice": "1d8",
            "speed": {
                "walk": 50
            },
            "strength": 11,
            "dexterity": 13,
            "constitution": 12,
            "intelligence": 2,
            "wisdom": 12,
            "charisma": 5,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 3,
            "skills": {
                "perception": 3
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 13",
            "languages": "",
            "challenge_rating": "0",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 3 (1d6) piercing damage.",
                    "attack_bonus": 2,
                    "damage_dice": "1d6"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Pack Tactics",
                    "desc": "The hyena has advantage on an attack roll against a creature if at least one of the hyena's allies is within 5 ft. of the creature and the ally isn't incapacitated."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "jackal": {
            "slug": "jackal",
            "name": "Jackal",
            "size": "Small",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 12,
            "armor_desc": "null",
            "hit_points": 3,
            "hit_dice": "1d6",
            "speed": {
                "walk": 40
            },
            "strength": 8,
            "dexterity": 15,
            "constitution": 11,
            "intelligence": 3,
            "wisdom": 12,
            "charisma": 6,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 3,
            "skills": {
                "perception": 3
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 13",
            "languages": "",
            "challenge_rating": "0",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 1 (1d4 - 1) piercing damage.",
                    "attack_bonus": 1,
                    "damage_dice": "1d4",
                    "damage_bonus": -1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Keen Hearing and Smell",
                    "desc": "The jackal has advantage on Wisdom (Perception) checks that rely on hearing or smell."
                },
                {
                    "name": "Pack Tactics",
                    "desc": "The jackal has advantage on an attack roll against a creature if at least one of the jackal's allies is within 5 ft. of the creature and the ally isn't incapacitated."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "lemure": {
            "slug": "lemure",
            "name": "Lemure",
            "size": "Medium",
            "type": "fiend",
            "subtype": "devil",
            "group": "Devils",
            "alignment": "lawful evil",
            "armor_class": 7,
            "armor_desc": "null",
            "hit_points": 13,
            "hit_dice": "3d8",
            "speed": {
                "walk": 15
            },
            "strength": 10,
            "dexterity": 5,
            "constitution": 11,
            "intelligence": 1,
            "wisdom": 11,
            "charisma": 3,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "cold",
            "damage_immunities": "fire, poison",
            "condition_immunities": "charmed, frightened, poisoned",
            "senses": "darkvision 120 ft., passive Perception 10",
            "languages": "understands infernal but can't speak",
            "challenge_rating": "0",
            "actions": [
                {
                    "name": "Fist",
                    "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 2 (1d4) bludgeoning damage",
                    "attack_bonus": 3,
                    "damage_dice": "1d4"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Devil's Sight",
                    "desc": "Magical darkness doesn't impede the lemure's darkvision."
                },
                {
                    "name": "Hellish Rejuvenation",
                    "desc": "A lemure that dies in the Nine Hells comes back to life with all its hit points in 1d10 days unless it is killed by a good-aligned creature with a bless spell cast on that creature or its remains are sprinkled with holy water."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "lizard": {
            "slug": "lizard",
            "name": "Lizard",
            "size": "Tiny",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 10,
            "armor_desc": "null",
            "hit_points": 2,
            "hit_dice": "1d4",
            "speed": {
                "walk": 20,
                "climb": 20
            },
            "strength": 2,
            "dexterity": 11,
            "constitution": 10,
            "intelligence": 1,
            "wisdom": 8,
            "charisma": 3,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 30 ft., passive Perception 9",
            "languages": "",
            "challenge_rating": "0",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +0 to hit, reach 5 ft., one target. Hit: 1 piercing damage.",
                    "damage_bonus": 1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": "",
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "octopus": {
            "slug": "octopus",
            "name": "Octopus",
            "size": "Small",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 12,
            "armor_desc": "null",
            "hit_points": 3,
            "hit_dice": "1d6",
            "speed": {
                "walk": 5,
                "swim": 30
            },
            "strength": 4,
            "dexterity": 15,
            "constitution": 11,
            "intelligence": 3,
            "wisdom": 10,
            "charisma": 4,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 2,
            "skills": {
                "perception": 2,
                "stealth": 4
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 30 ft., passive Perception 12",
            "languages": "",
            "challenge_rating": "0",
            "actions": [
                {
                    "name": "Tentacles",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 1 bludgeoning damage, and the target is grappled (escape DC 10). Until this grapple ends, the octopus can't use its tentacles on another target.",
                    "attack_bonus": 4,
                    "damage_bonus": 1
                },
                {
                    "name": "Ink Cloud (Recharges after a Short or Long Rest)",
                    "desc": "A 5-foot-radius cloud of ink extends all around the octopus if it is underwater. The area is heavily obscured for 1 minute, although a significant current can disperse the ink. After releasing the ink, the octopus can use the Dash action as a bonus action."
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Hold Breath",
                    "desc": "While out of water, the octopus can hold its breath for 30 minutes."
                },
                {
                    "name": "Underwater Camouflage",
                    "desc": "The octopus has advantage on Dexterity (Stealth) checks made while underwater."
                },
                {
                    "name": "Water Breathing",
                    "desc": "The octopus can breathe only underwater."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "owl": {
            "slug": "owl",
            "name": "Owl",
            "size": "Tiny",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 11,
            "armor_desc": "null",
            "hit_points": 1,
            "hit_dice": "1d4",
            "speed": {
                "walk": 5,
                "fly": 60
            },
            "strength": 3,
            "dexterity": 13,
            "constitution": 8,
            "intelligence": 2,
            "wisdom": 12,
            "charisma": 7,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 3,
            "skills": {
                "perception": 3,
                "stealth": 3
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 120 ft., passive Perception 13",
            "languages": "",
            "challenge_rating": "0",
            "actions": [
                {
                    "name": "Talons",
                    "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 1 slashing damage.",
                    "attack_bonus": 3,
                    "damage_bonus": 1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Flyby",
                    "desc": "The owl doesn't provoke opportunity attacks when it flies out of an enemy's reach."
                },
                {
                    "name": "Keen Hearing and Sight",
                    "desc": "The owl has advantage on Wisdom (Perception) checks that rely on hearing or sight."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "quipper": {
            "slug": "quipper",
            "name": "Quipper",
            "size": "Tiny",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 13,
            "armor_desc": "null",
            "hit_points": 1,
            "hit_dice": "1d4",
            "speed": {
                "swim": 40
            },
            "strength": 2,
            "dexterity": 16,
            "constitution": 9,
            "intelligence": 1,
            "wisdom": 7,
            "charisma": 2,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 60 ft., passive Perception 8",
            "languages": "",
            "challenge_rating": "0",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 1 piercing damage.",
                    "attack_bonus": 5,
                    "damage_bonus": 1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Blood Frenzy",
                    "desc": "The quipper has advantage on melee attack rolls against any creature that doesn't have all its hit points."
                },
                {
                    "name": "Water Breathing",
                    "desc": "The quipper can breathe only underwater."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "rat": {
            "slug": "rat",
            "name": "Rat",
            "size": "Tiny",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 10,
            "armor_desc": "null",
            "hit_points": 1,
            "hit_dice": "1d4",
            "speed": {
                "walk": 20
            },
            "strength": 2,
            "dexterity": 11,
            "constitution": 9,
            "intelligence": 2,
            "wisdom": 10,
            "charisma": 4,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 30 ft., passive Perception 10",
            "languages": "",
            "challenge_rating": "0",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +0 to hit, reach 5 ft., one target. Hit: 1 piercing damage.",
                    "damage_bonus": 1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Keen Smell",
                    "desc": "The rat has advantage on Wisdom (Perception) checks that rely on smell."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "raven": {
            "slug": "raven",
            "name": "Raven",
            "size": "Tiny",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 12,
            "armor_desc": "null",
            "hit_points": 1,
            "hit_dice": "1d4",
            "speed": {
                "walk": 10,
                "fly": 50
            },
            "strength": 2,
            "dexterity": 14,
            "constitution": 8,
            "intelligence": 2,
            "wisdom": 12,
            "charisma": 6,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 3,
            "skills": {
                "perception": 3
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 13",
            "languages": "",
            "challenge_rating": "0",
            "actions": [
                {
                    "name": "Beak",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 1 piercing damage."
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Mimicry",
                    "desc": "The raven can mimic simple sounds it has heard, such as a person whispering, a baby crying, or an animal chittering. A creature that hears the sounds can tell they are imitations with a successful DC 10 Wisdom (Insight) check."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "scorpion": {
            "slug": "scorpion",
            "name": "Scorpion",
            "size": "Tiny",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 11,
            "armor_desc": "natural armor",
            "hit_points": 1,
            "hit_dice": "1d4",
            "speed": {
                "walk": 10
            },
            "strength": 2,
            "dexterity": 11,
            "constitution": 8,
            "intelligence": 1,
            "wisdom": 8,
            "charisma": 2,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "blindsight 10 ft., passive Perception 9",
            "languages": "",
            "challenge_rating": "0",
            "actions": [
                {
                    "name": "Sting",
                    "desc": "Melee Weapon Attack: +2 to hit, reach 5 ft., one creature. Hit: 1 piercing damage, and the target must make a DC 9 Constitution saving throw, taking 4 (1d8) poison damage on a failed save, or half as much damage on a successful one.",
                    "attack_bonus": 2,
                    "damage_bonus": 1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": "",
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "sea-horse": {
            "slug": "sea-horse",
            "name": "Sea Horse",
            "size": "Tiny",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 11,
            "armor_desc": "null",
            "hit_points": 1,
            "hit_dice": "1d4",
            "speed": {
                "swim": 20
            },
            "strength": 1,
            "dexterity": 12,
            "constitution": 8,
            "intelligence": 1,
            "wisdom": 10,
            "charisma": 2,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 10",
            "languages": "",
            "challenge_rating": "0",
            "actions": "",
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Water Breathing",
                    "desc": "The sea horse can breathe only underwater."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "shrieker": {
            "slug": "shrieker",
            "name": "Shrieker",
            "size": "Medium",
            "type": "plant",
            "subtype": "",
            "group": "Fungi",
            "alignment": "unaligned",
            "armor_class": 5,
            "armor_desc": "null",
            "hit_points": 13,
            "hit_dice": "3d8",
            "speed": {
                "walk": 0
            },
            "strength": 1,
            "dexterity": 1,
            "constitution": 10,
            "intelligence": 1,
            "wisdom": 3,
            "charisma": 1,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "blinded, deafened, frightened",
            "senses": "blindsight 30 ft. (blind beyond this radius), passive Perception 6",
            "languages": "",
            "challenge_rating": "0",
            "actions": [
                {
                    "name": "Shriek",
                    "desc": "When bright light or a creature is within 30 feet of the shrieker, it emits a shriek audible within 300 feet of it. The shrieker continues to shriek until the disturbance moves out of range and for 1d4 of the shrieker's turns afterward"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "False Appearance",
                    "desc": "While the shrieker remains motionless, it is indistinguishable from an ordinary fungus."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "spider": {
            "slug": "spider",
            "name": "Spider",
            "size": "Tiny",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 12,
            "armor_desc": "null",
            "hit_points": 1,
            "hit_dice": "1d4",
            "speed": {
                "walk": 20,
                "climb": 20
            },
            "strength": 2,
            "dexterity": 14,
            "constitution": 8,
            "intelligence": 1,
            "wisdom": 10,
            "charisma": 2,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {
                "stealth": 4
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 30 ft., passive Perception 12",
            "languages": "",
            "challenge_rating": "0",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 1 piercing damage, and the target must succeed on a DC 9 Constitution saving throw or take 2 (1d4) poison damage.",
                    "attack_bonus": 4,
                    "damage_bonus": 1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Spider Climb",
                    "desc": "The spider can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check."
                },
                {
                    "name": "Web Sense",
                    "desc": "While in contact with a web, the spider knows the exact location of any other creature in contact with the same web."
                },
                {
                    "name": "Web Walker",
                    "desc": "The spider ignores movement restrictions caused by webbing."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "vulture": {
            "slug": "vulture",
            "name": "Vulture",
            "size": "Medium",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 10,
            "armor_desc": "null",
            "hit_points": 5,
            "hit_dice": "1d8",
            "speed": {
                "walk": 10,
                "fly": 50
            },
            "strength": 7,
            "dexterity": 10,
            "constitution": 13,
            "intelligence": 2,
            "wisdom": 12,
            "charisma": 4,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 3,
            "skills": {
                "perception": 3
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 13",
            "languages": "",
            "challenge_rating": "0",
            "actions": [
                {
                    "name": "Beak",
                    "desc": "Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 2 (1d4) piercing damage.",
                    "attack_bonus": 2,
                    "damage_dice": "1d4"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Keen Sight and Smell",
                    "desc": "The vulture has advantage on Wisdom (Perception) checks that rely on sight or smell."
                },
                {
                    "name": "Pack Tactics",
                    "desc": "The vulture has advantage on an attack roll against a creature if at least one of the vulture's allies is within 5 ft. of the creature and the ally isn't incapacitated."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "weasel": {
            "slug": "weasel",
            "name": "Weasel",
            "size": "Tiny",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 13,
            "armor_desc": "null",
            "hit_points": 1,
            "hit_dice": "1d4",
            "speed": {
                "walk": 30
            },
            "strength": 3,
            "dexterity": 16,
            "constitution": 8,
            "intelligence": 2,
            "wisdom": 12,
            "charisma": 3,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 3,
            "skills": {
                "perception": 3,
                "stealth": 5
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 13",
            "languages": "",
            "challenge_rating": "0",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 1 piercing damage.",
                    "attack_bonus": 5,
                    "damage_bonus": 1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Keen Hearing and Smell",
                    "desc": "The weasel has advantage on Wisdom (Perception) checks that rely on hearing or smell."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "zoog": {
            "slug": "zoog",
            "name": "Zoog",
            "size": "Tiny",
            "type": "aberration",
            "subtype": "",
            "group": "null",
            "alignment": "chaotic evil",
            "armor_class": 13,
            "armor_desc": "null",
            "hit_points": 3,
            "hit_dice": "1d4+1",
            "speed": {
                "climb": 30,
                "walk": 30
            },
            "strength": 3,
            "dexterity": 16,
            "constitution": 12,
            "intelligence": 11,
            "wisdom": 10,
            "charisma": 8,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 2,
            "skills": {
                "perception": 2,
                "stealth": 5
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 60 ft., passive Perception 12",
            "languages": "Deep Speech, Void Speech",
            "challenge_rating": "0",
            "actions": [
                {
                    "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 1 piercing damage.",
                    "name": "Bite"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": "",
            "spell_list": [],
            "img_main": "null",
            "document__slug": "cc",
            "document__title": "Creature Codex OGL",
            "document__license_url": "http://open5e.com/legal"
        }
    },
    "1/8": {
        "bandit": {
            "slug": "bandit",
            "name": "Bandit",
            "size": "Medium",
            "type": "humanoid",
            "subtype": "any race",
            "group": "null",
            "alignment": "any non-lawful alignment",
            "armor_class": 12,
            "armor_desc": "leather armor",
            "hit_points": 11,
            "hit_dice": "2d8",
            "speed": {
                "walk": 30
            },
            "strength": 11,
            "dexterity": 12,
            "constitution": 12,
            "intelligence": 10,
            "wisdom": 10,
            "charisma": 10,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 10",
            "languages": "any one language (usually Common)",
            "challenge_rating": "1/8",
            "actions": [
                {
                    "name": "Scimitar",
                    "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) slashing damage.",
                    "attack_bonus": 3,
                    "damage_dice": "1d6",
                    "damage_bonus": 1
                },
                {
                    "name": "Light Crossbow",
                    "desc": "Ranged Weapon Attack: +3 to hit, range 80 ft./320 ft., one target. Hit: 5 (1d8 + 1) piercing damage.",
                    "attack_bonus": 3,
                    "damage_dice": "1d8",
                    "damage_bonus": 1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": "",
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "blood-hawk": {
            "slug": "blood-hawk",
            "name": "Blood Hawk",
            "size": "Small",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 12,
            "armor_desc": "null",
            "hit_points": 7,
            "hit_dice": "2d6",
            "speed": {
                "walk": 10,
                "fly": 60
            },
            "strength": 6,
            "dexterity": 14,
            "constitution": 10,
            "intelligence": 3,
            "wisdom": 14,
            "charisma": 5,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 4,
            "skills": {
                "perception": 4
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 14",
            "languages": "",
            "challenge_rating": "1/8",
            "actions": [
                {
                    "name": "Beak",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage.",
                    "attack_bonus": 4,
                    "damage_dice": "1d4",
                    "damage_bonus": 2
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Keen Sight",
                    "desc": "The hawk has advantage on Wisdom (Perception) checks that rely on sight."
                },
                {
                    "name": "Pack Tactics",
                    "desc": "The hawk has advantage on an attack roll against a creature if at least one of the hawk's allies is within 5 ft. of the creature and the ally isn't incapacitated."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "bookkeeper": {
            "slug": "bookkeeper",
            "name": "Bookkeeper",
            "size": "Tiny",
            "type": "construct",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 12,
            "armor_desc": "null",
            "hit_points": 5,
            "hit_dice": "2d4",
            "speed": {
                "fly": 30,
                "walk": 20
            },
            "strength": 8,
            "dexterity": 14,
            "constitution": 10,
            "intelligence": 6,
            "wisdom": 8,
            "charisma": 3,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 1,
            "skills": {
                "perception": 1,
                "stealth": 4
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "bludgeoning, piercing, and slashing from nonmagical attacks",
            "damage_immunities": "either cold or fire (designated at the time of the bookkeeper's creation), poison, psychic",
            "condition_immunities": "charmed, exhaustion, frightened, paralyzed, petrified, poisoned",
            "senses": "blindsight 60 ft. (blind beyond this radius), passive Perception 11",
            "languages": "understands the languages of its creator but can't speak",
            "challenge_rating": "1/8",
            "actions": [
                {
                    "attack_bonus": 4,
                    "damage_dice": "1d6",
                    "desc": "Ranged Weapon Attack: +4 to hit, range 20 ft., one target. Hit: 3 (1d6) poison damage and the target must succeed on a DC 13 Dexterity saving throw or be blinded until the end of its next turn.",
                    "name": "Ink Splash"
                },
                {
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 1 piercing damage plus 1 poison damage.",
                    "name": "Bite"
                },
                {
                    "desc": "While inside its book, the bookkeeper magically turns its book invisible until it attacks, or until its concentration ends (as if concentrating on a spell). The bookkeeper is also invisible while inside the invisible book",
                    "name": "Elusive Pages"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "desc": "As a bonus action while within 30 feet of its book, the bookkeeper can hop inside its book. While inside its book, the bookkeeper has a flying speed of 30 feet and is indistinguishable from ink on a page.",
                    "name": "Between the Lines"
                },
                {
                    "desc": "A bookkeeper makes all attacks, saving throws, and skill checks with advantage when its creator is within 60 feet of its book. The bookkeeper's hp maximum is reduced by 1 for every minute it is further than 60 feet from its book. When its hp maximum reaches 0, it dies. If its creator dies, the bookkeeper can be convinced to pass ownership of the book to a new creature if the creature succeeds on a DC 13 Charisma check. The new owner becomes the bookkeeper's new “creator” and inherits the bookkeeper along with the book.",
                    "name": "Book Bound"
                },
                {
                    "desc": "When the bookkeeper dies, the book it is bound to is also destroyed.",
                    "name": "Disintegrate"
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "cc",
            "document__title": "Creature Codex OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "camel": {
            "slug": "camel",
            "name": "Camel",
            "size": "Large",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 9,
            "armor_desc": "null",
            "hit_points": 15,
            "hit_dice": "2d10",
            "speed": {
                "walk": 50
            },
            "strength": 16,
            "dexterity": 8,
            "constitution": 14,
            "intelligence": 2,
            "wisdom": 8,
            "charisma": 5,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 9",
            "languages": "",
            "challenge_rating": "1/8",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 2 (1d4) bludgeoning damage.",
                    "attack_bonus": 5,
                    "damage_dice": "1d4"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": "",
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "cikavak": {
            "slug": "cikavak",
            "name": "Cikavak",
            "size": "Tiny",
            "type": "fey",
            "subtype": "",
            "group": "null",
            "alignment": "neutral",
            "armor_class": 12,
            "armor_desc": "",
            "hit_points": 17,
            "hit_dice": "7d4",
            "speed": {
                "walk": 10,
                "fly": 40
            },
            "strength": 4,
            "dexterity": 15,
            "constitution": 10,
            "intelligence": 12,
            "wisdom": 12,
            "charisma": 4,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 5,
            "skills": {
                "perception": 5,
                "stealth": 9
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "acid, fire, poison",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception $1",
            "languages": "understands Common; telepathy (touch)",
            "challenge_rating": "1/8",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +4 to hit, range 5 ft., one target. Hit: 7 (1d4 + 2) piercing damage.",
                    "attack_bonus": 4,
                    "damage_dice": "1d4"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Innate Spellcasting",
                    "desc": "the cikavak's innate spellcasting ability is Wisdom (spell save DC 11). It can innately cast the following spells, requiring no material components:\n\nat will: speak with animals\n\n1/day: silence"
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "tob",
            "document__title": "Tome of Beasts OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "clockwork-servant": {
            "slug": "clockwork-servant",
            "name": "Clockwork Servant",
            "size": "Medium",
            "type": "construct",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 11,
            "armor_desc": "null",
            "hit_points": 22,
            "hit_dice": "4d8+4",
            "speed": {
                "walk": 25
            },
            "strength": 14,
            "dexterity": 12,
            "constitution": 13,
            "intelligence": 8,
            "wisdom": 12,
            "charisma": 7,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 5,
            "skills": {
                "investigation": 3,
                "perception": 5
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "poison, psychic",
            "condition_immunities": "charmed, exhaustion, frightened, paralyzed, petrified, poisoned",
            "senses": "darkvision 60 ft., passive Perception 15",
            "languages": "Common",
            "challenge_rating": "1/8",
            "actions": [
                {
                    "attack_bonus": 4,
                    "damage_dice": "1d6+2",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) bludgeoning damage.",
                    "name": "Slam"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "desc": "The servant can cast the mending and prestidigitation cantrips at will without requiring spell components.",
                    "name": "Domestic Retainer"
                },
                {
                    "desc": "The servant is immune to any spell or effect that would alter its form.",
                    "name": "Immutable Form"
                },
                {
                    "desc": "The servant has advantage on saving throws against spells and other magical effects.",
                    "name": "Magic Resistance"
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "cc",
            "document__title": "Creature Codex OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "cultist": {
            "slug": "cultist",
            "name": "Cultist",
            "size": "Medium",
            "type": "humanoid",
            "subtype": "any race",
            "group": "null",
            "alignment": "any non-good alignment",
            "armor_class": 12,
            "armor_desc": "leather armor",
            "hit_points": 9,
            "hit_dice": "2d8",
            "speed": {
                "walk": 30
            },
            "strength": 11,
            "dexterity": 12,
            "constitution": 10,
            "intelligence": 10,
            "wisdom": 11,
            "charisma": 10,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {
                "deception": 2,
                "religion": 2
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 10",
            "languages": "any one language (usually Common)",
            "challenge_rating": "1/8",
            "actions": [
                {
                    "name": "Scimitar",
                    "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one creature. Hit: 4 (1d6 + 1) slashing damage.",
                    "attack_bonus": 3,
                    "damage_dice": "1d6",
                    "damage_bonus": 1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Dark Devotion",
                    "desc": "The cultist has advantage on saving throws against being charmed or frightened."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "flying-snake": {
            "slug": "flying-snake",
            "name": "Flying Snake",
            "size": "Tiny",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 14,
            "armor_desc": "null",
            "hit_points": 5,
            "hit_dice": "2d4",
            "speed": {
                "walk": 30,
                "fly": 60,
                "swim": 30
            },
            "strength": 4,
            "dexterity": 18,
            "constitution": 11,
            "intelligence": 2,
            "wisdom": 12,
            "charisma": 5,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "blindsight 10 ft., passive Perception 11",
            "languages": "",
            "challenge_rating": "1/8",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 1 piercing damage plus 7 (3d4) poison damage.",
                    "attack_bonus": 6,
                    "damage_bonus": 1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Flyby",
                    "desc": "The snake doesn't provoke opportunity attacks when it flies out of an enemy's reach."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "giant-crab": {
            "slug": "giant-crab",
            "name": "Giant Crab",
            "size": "Medium",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 15,
            "armor_desc": "natural armor",
            "hit_points": 13,
            "hit_dice": "3d8",
            "speed": {
                "walk": 30,
                "swim": 30
            },
            "strength": 13,
            "dexterity": 15,
            "constitution": 11,
            "intelligence": 1,
            "wisdom": 9,
            "charisma": 3,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {
                "stealth": 4
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "blindsight 30 ft., passive Perception 9",
            "languages": "",
            "challenge_rating": "1/8",
            "actions": [
                {
                    "name": "Claw",
                    "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) bludgeoning damage, and the target is grappled (escape DC 11). The crab has two claws, each of which can grapple only one target.",
                    "attack_bonus": 3,
                    "damage_dice": "1d6",
                    "damage_bonus": 1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Amphibious",
                    "desc": "The crab can breathe air and water."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "giant-moth": {
            "slug": "giant-moth",
            "name": "Giant Moth",
            "size": "Small",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 11,
            "armor_desc": "null",
            "hit_points": 7,
            "hit_dice": "2d6",
            "speed": {
                "fly": 30,
                "walk": 25
            },
            "strength": 10,
            "dexterity": 12,
            "constitution": 10,
            "intelligence": 3,
            "wisdom": 10,
            "charisma": 7,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 2,
            "skills": {
                "perception": 2,
                "stealth": 3
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 60 ft., passive Perception 12",
            "languages": "-",
            "challenge_rating": "1/8",
            "actions": [
                {
                    "attack_bonus": 3,
                    "damage_dice": "1d6+1",
                    "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) piercing damage.",
                    "name": "Proboscis"
                },
                {
                    "desc": "A 10-foot radius cloud of fine powder disperses from the giant moth. Each creature in that area must succeed on a DC 10 Constitution saving throw or be blinded until the end of its next turn.",
                    "name": "Powdery Wings (1/Day)"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "desc": "The giant moth has advantage on Wisdom (Perception) checks that rely on smell.",
                    "name": "Antennae"
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "cc",
            "document__title": "Creature Codex OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "giant-rat": {
            "slug": "giant-rat",
            "name": "Giant Rat",
            "size": "Small",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 12,
            "armor_desc": "null",
            "hit_points": 7,
            "hit_dice": "2d6",
            "speed": {
                "walk": 30
            },
            "strength": 7,
            "dexterity": 15,
            "constitution": 11,
            "intelligence": 2,
            "wisdom": 10,
            "charisma": 4,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 60 ft., passive Perception 10",
            "languages": "",
            "challenge_rating": "1/8",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage.",
                    "attack_bonus": 4,
                    "damage_dice": "1d4",
                    "damage_bonus": 2
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Keen Smell",
                    "desc": "The rat has advantage on Wisdom (Perception) checks that rely on smell."
                },
                {
                    "name": "Pack Tactics",
                    "desc": "The rat has advantage on an attack roll against a creature if at least one of the rat's allies is within 5 ft. of the creature and the ally isn't incapacitated."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "giant-rat-diseased": {
            "slug": "giant-rat-diseased",
            "name": "Giant Rat (Diseased)",
            "size": "Small",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 12,
            "armor_desc": "null",
            "hit_points": 7,
            "hit_dice": "2d6",
            "speed": {
                "walk": 30
            },
            "strength": 7,
            "dexterity": 15,
            "constitution": 11,
            "intelligence": 2,
            "wisdom": 10,
            "charisma": 4,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 60 ft., passive Perception 10",
            "languages": "",
            "challenge_rating": "1/8",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 2) piercing damage. If the target is a creature, it must succeed on a DC 10 Constitution saving throw or contract a disease. Until the disease is cured, the target can't regain hit points except by magical means, and the target's hit point maximum decreases by 3 (1d6) every 24 hours. If the target's hit point maximum drops to 0 as a result of this disease, the target dies.",
                    "attack_bonus": 4,
                    "damage_dice": "1d4",
                    "damage_bonus": 2
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": "",
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "giant-weasel": {
            "slug": "giant-weasel",
            "name": "Giant Weasel",
            "size": "Medium",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 13,
            "armor_desc": "null",
            "hit_points": 9,
            "hit_dice": "2d8",
            "speed": {
                "walk": 40
            },
            "strength": 11,
            "dexterity": 16,
            "constitution": 10,
            "intelligence": 4,
            "wisdom": 12,
            "charisma": 5,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 3,
            "skills": {
                "perception": 3,
                "stealth": 5
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 60 ft., passive Perception 13",
            "languages": "",
            "challenge_rating": "1/8",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) piercing damage.",
                    "attack_bonus": 5,
                    "damage_dice": "1d4",
                    "damage_bonus": 3
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Keen Hearing and Smell",
                    "desc": "The weasel has advantage on Wisdom (Perception) checks that rely on hearing or smell."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "guard": {
            "slug": "guard",
            "name": "Guard",
            "size": "Medium",
            "type": "humanoid",
            "subtype": "any race",
            "group": "null",
            "alignment": "any alignment",
            "armor_class": 16,
            "armor_desc": "chain shirt, shield",
            "hit_points": 11,
            "hit_dice": "2d8",
            "speed": {
                "walk": 30
            },
            "strength": 13,
            "dexterity": 12,
            "constitution": 12,
            "intelligence": 10,
            "wisdom": 11,
            "charisma": 10,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 2,
            "skills": {
                "perception": 2
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 12",
            "languages": "any one language (usually Common)",
            "challenge_rating": "1/8",
            "actions": [
                {
                    "name": "Spear",
                    "desc": "Melee or Ranged Weapon Attack: +3 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d6 + 1) piercing damage or 5 (1d8 + 1) piercing damage if used with two hands to make a melee attack.",
                    "attack_bonus": 3,
                    "damage_dice": "1d6",
                    "damage_bonus": 1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": "",
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "kobold": {
            "slug": "kobold",
            "name": "Kobold",
            "size": "Small",
            "type": "humanoid",
            "subtype": "kobold",
            "group": "null",
            "alignment": "lawful evil",
            "armor_class": 12,
            "armor_desc": "null",
            "hit_points": 5,
            "hit_dice": "2d6-2",
            "speed": {
                "walk": 30
            },
            "strength": 7,
            "dexterity": 15,
            "constitution": 9,
            "intelligence": 8,
            "wisdom": 7,
            "charisma": 8,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 60 ft., passive Perception 8",
            "languages": "Common, Draconic",
            "challenge_rating": "1/8",
            "actions": [
                {
                    "name": "Dagger",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage.",
                    "attack_bonus": 4,
                    "damage_dice": "1d4",
                    "damage_bonus": 2
                },
                {
                    "name": "Sling",
                    "desc": "Ranged Weapon Attack: +4 to hit, range 30/120 ft., one target. Hit: 4 (1d4 + 2) bludgeoning damage.",
                    "attack_bonus": 4,
                    "damage_dice": "1d4",
                    "damage_bonus": 2
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Sunlight Sensitivity",
                    "desc": "While in sunlight, the kobold has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."
                },
                {
                    "name": "Pack Tactics",
                    "desc": "The kobold has advantage on an attack roll against a creature if at least one of the kobold's allies is within 5 ft. of the creature and the ally isn't incapacitated."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "leonino": {
            "slug": "leonino",
            "name": "Leonino",
            "size": "Tiny",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 13,
            "armor_desc": "null",
            "hit_points": 13,
            "hit_dice": "3d4+6",
            "speed": {
                "fly": 40,
                "walk": 30
            },
            "strength": 10,
            "dexterity": 16,
            "constitution": 14,
            "intelligence": 8,
            "wisdom": 8,
            "charisma": 12,
            "strength_save": "null",
            "dexterity_save": 5,
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": 1,
            "charisma_save": "null",
            "perception": 1,
            "skills": {
                "perception": 1,
                "persuasion": 3,
                "stealth": 5
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 30 ft., passive Perception 11",
            "languages": "Elvish",
            "challenge_rating": "1/8",
            "actions": [
                {
                    "attack_bonus": 5,
                    "damage_dice": "1d4+3",
                    "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) slashing damage. If this is the first time the leonino has hit the target within the past 24 hours, the target must succeed on a DC 10 Wisdom saving throw or be charmed by the leonino for 1 hour.",
                    "name": "Bite"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "desc": "The leonino doesn't provoke opportunity attacks when it flies out of an enemy's reach.",
                    "name": "Flyby"
                },
                {
                    "desc": "If the leonino is subjected to an effect that allows it to make a Dexterity saving throw to take only half damage, the leonino instead takes no damage if it succeeds on the saving throw, and only half damage if it fails.",
                    "name": "Evasion"
                },
                {
                    "desc": "The flight of a leonine is especially silent and difficult to notice in forests and urban settings. It has advantage on Dexterity (Stealth) checks made while flying in these areas.",
                    "name": "Silent Wings"
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "cc",
            "document__title": "Creature Codex OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "mastiff": {
            "slug": "mastiff",
            "name": "Mastiff",
            "size": "Medium",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 12,
            "armor_desc": "null",
            "hit_points": 5,
            "hit_dice": "1d8",
            "speed": {
                "walk": 40
            },
            "strength": 13,
            "dexterity": 14,
            "constitution": 12,
            "intelligence": 3,
            "wisdom": 12,
            "charisma": 7,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 3,
            "skills": {
                "perception": 3
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 13",
            "languages": "",
            "challenge_rating": "1/8",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) piercing damage. If the target is a creature, it must succeed on a DC 11 Strength saving throw or be knocked prone.",
                    "attack_bonus": 3,
                    "damage_dice": "1d6",
                    "damage_bonus": 1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Keen Hearing and Smell",
                    "desc": "The mastiff has advantage on Wisdom (Perception) checks that rely on hearing or smell."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "merfolk": {
            "slug": "merfolk",
            "name": "Merfolk",
            "size": "Medium",
            "type": "humanoid",
            "subtype": "merfolk",
            "group": "null",
            "alignment": "neutral",
            "armor_class": 11,
            "armor_desc": "null",
            "hit_points": 11,
            "hit_dice": "2d8+2",
            "speed": {
                "walk": 10,
                "swim": 40
            },
            "strength": 10,
            "dexterity": 13,
            "constitution": 12,
            "intelligence": 11,
            "wisdom": 11,
            "charisma": 12,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 2,
            "skills": {
                "perception": 2
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 12",
            "languages": "Aquan, Common",
            "challenge_rating": "1/8",
            "actions": [
                {
                    "name": "Spear",
                    "desc": "Melee or Ranged Weapon Attack: +2 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 3 (1d6) piercing damage, or 4 (1d8) piercing damage if used with two hands to make a melee attack.",
                    "attack_bonus": 2,
                    "damage_dice": "1d6"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Amphibious",
                    "desc": "The merfolk can breathe air and water."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "mule": {
            "slug": "mule",
            "name": "Mule",
            "size": "Medium",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 10,
            "armor_desc": "null",
            "hit_points": 11,
            "hit_dice": "2d8",
            "speed": {
                "walk": 40
            },
            "strength": 14,
            "dexterity": 10,
            "constitution": 13,
            "intelligence": 2,
            "wisdom": 10,
            "charisma": 5,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 10",
            "languages": "",
            "challenge_rating": "1/8",
            "actions": [
                {
                    "name": "Hooves",
                    "desc": "Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) bludgeoning damage.",
                    "attack_bonus": 4,
                    "damage_dice": "1d4",
                    "damage_bonus": 2
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Beast of Burden",
                    "desc": "The mule is considered to be a Large animal for the purpose of determining its carrying capacity."
                },
                {
                    "name": "Sure-Footed",
                    "desc": "The mule has advantage on Strength and Dexterity saving throws made against effects that would knock it prone."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "noble": {
            "slug": "noble",
            "name": "Noble",
            "size": "Medium",
            "type": "humanoid",
            "subtype": "any race",
            "group": "null",
            "alignment": "any alignment",
            "armor_class": 15,
            "armor_desc": "breastplate",
            "hit_points": 9,
            "hit_dice": "2d8",
            "speed": {
                "walk": 30
            },
            "strength": 11,
            "dexterity": 12,
            "constitution": 11,
            "intelligence": 12,
            "wisdom": 14,
            "charisma": 16,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {
                "deception": 5,
                "insight": 4,
                "persuasion": 5
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 12",
            "languages": "any two languages",
            "challenge_rating": "1/8",
            "actions": [
                {
                    "name": "Rapier",
                    "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 5 (1d8 + 1) piercing damage.",
                    "attack_bonus": 3,
                    "damage_dice": "1d8",
                    "damage_bonus": 1
                }
            ],
            "reactions": [
                {
                    "name": "Parry",
                    "desc": "The noble adds 2 to its AC against one melee attack that would hit it. To do so, the noble must see the attacker and be wielding a melee weapon."
                }
            ],
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": "",
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "poisonous-snake": {
            "slug": "poisonous-snake",
            "name": "Poisonous Snake",
            "size": "Tiny",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 13,
            "armor_desc": "null",
            "hit_points": 2,
            "hit_dice": "1d4",
            "speed": {
                "walk": 30,
                "swim": 30
            },
            "strength": 2,
            "dexterity": 16,
            "constitution": 11,
            "intelligence": 1,
            "wisdom": 10,
            "charisma": 3,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "blindsight 10 ft., passive Perception 10",
            "languages": "",
            "challenge_rating": "1/8",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 1 piercing damage, and the target must make a DC 10 Constitution saving throw, taking 5 (2d4) poison damage on a failed save, or half as much damage on a successful one.",
                    "attack_bonus": 5,
                    "damage_bonus": 1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": "",
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "pony": {
            "slug": "pony",
            "name": "Pony",
            "size": "Medium",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 10,
            "armor_desc": "null",
            "hit_points": 11,
            "hit_dice": "2d8",
            "speed": {
                "walk": 40
            },
            "strength": 15,
            "dexterity": 10,
            "constitution": 13,
            "intelligence": 2,
            "wisdom": 11,
            "charisma": 7,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 10",
            "languages": "",
            "challenge_rating": "1/8",
            "actions": [
                {
                    "name": "Hooves",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (2d4 + 2) bludgeoning damage.",
                    "attack_bonus": 4,
                    "damage_dice": "2d4",
                    "damage_bonus": 2
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": "",
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "shroud": {
            "slug": "shroud",
            "name": "Shroud",
            "size": "Medium",
            "type": "undead",
            "subtype": "",
            "group": "null",
            "alignment": "neutral evil",
            "armor_class": 13,
            "armor_desc": "natural armor",
            "hit_points": 9,
            "hit_dice": "2d8",
            "speed": {
                "hover": "true",
                "walk": 0,
                "fly": 30
            },
            "strength": 4,
            "dexterity": 13,
            "constitution": 10,
            "intelligence": 2,
            "wisdom": 10,
            "charisma": 8,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {
                "stealth": 3
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "acid, cold, fire, lightning, thunder; bludgeoning, piercing, and slashing from nonmagical weapons that aren't silvered",
            "damage_immunities": "necrotic, poison",
            "condition_immunities": "exhaustion, frightened, grappled, paralyzed, petrified, poisoned, prone, restrained",
            "senses": "darkvision 60 ft., passive Perception 10",
            "languages": "Common",
            "challenge_rating": "1/8",
            "actions": [
                {
                    "name": "Strength Drain",
                    "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one creature. Hit: 3 (1d4 + 1) necrotic damage, and the target's Strength score is reduced by one-half that amount. The target dies if this reduces its Strength to 0. Otherwise, the reduction lasts until the target finishes a short or long rest. If a non-evil humanoid dies from this attack, a new shadow rises from the corpse 1d4 hours later.",
                    "attack_bonus": 3,
                    "damage_dice": "1d4"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Amorphous",
                    "desc": "The shroud can move through a space as narrow as 1 inch wide without squeezing."
                },
                {
                    "name": "Shadow Evolution",
                    "desc": "Shrouds instantly become shadows once they cause a total of 12 damage. Any damage they've suffered is subtracted from the shadow's total hit points or abilities."
                },
                {
                    "name": "Shroud Stealth",
                    "desc": "When in dim light or darkness, the shroud can take the Hide action as a bonus action."
                },
                {
                    "name": "Sunlight Weakness",
                    "desc": "While in sunlight, the shroud has disadvantage on attack rolls, ability checks, and saving throws."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "tob",
            "document__title": "Tome of Beasts OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "stirge": {
            "slug": "stirge",
            "name": "Stirge",
            "size": "Tiny",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 14,
            "armor_desc": "natural armor",
            "hit_points": 2,
            "hit_dice": "1d4",
            "speed": {
                "walk": 10,
                "fly": 40
            },
            "strength": 4,
            "dexterity": 16,
            "constitution": 11,
            "intelligence": 2,
            "wisdom": 8,
            "charisma": 6,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 60 ft., passive Perception 9",
            "languages": "",
            "challenge_rating": "1/8",
            "actions": [
                {
                    "name": "Blood Drain",
                    "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 5 (1d4 + 3) piercing damage, and the stirge attaches to the target. While attached, the stirge doesn't attack. Instead, at the start of each of the stirge's turns, the target loses 5 (1d4 + 3) hit points due to blood loss.\nThe stirge can detach itself by spending 5 feet of its movement. It does so after it drains 10 hit points of blood from the target or the target dies. A creature, including the target, can use its action to detach the stirge.",
                    "attack_bonus": 5,
                    "damage_dice": "1d4",
                    "damage_bonus": 3
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": "",
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "stryx": {
            "slug": "stryx",
            "name": "Stryx",
            "size": "Tiny",
            "type": "monstrosity",
            "subtype": "",
            "group": "null",
            "alignment": "neutral",
            "armor_class": 13,
            "armor_desc": "",
            "hit_points": 10,
            "hit_dice": "4d4",
            "speed": {
                "walk": 10,
                "fly": 60
            },
            "strength": 3,
            "dexterity": 17,
            "constitution": 11,
            "intelligence": 8,
            "wisdom": 15,
            "charisma": 6,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 4,
            "skills": {
                "perception": 4,
                "stealth": 5
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 120 ft., passive Perception 14",
            "languages": "Common, Elvish",
            "challenge_rating": "1/8",
            "actions": [
                {
                    "name": "Talons",
                    "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 1 slashing damage.",
                    "attack_bonus": 5,
                    "damage_dice": "1"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "False Appearance",
                    "desc": "Until a stryx speaks or opens its mouth, it is indistinguishable from a normal owl."
                },
                {
                    "name": "Flyby",
                    "desc": "The stryx doesn't provoke opportunity attacks when it flies out of an enemy's reach."
                },
                {
                    "name": "Innate Spellcasting",
                    "desc": "the stryx's innate spellcasting ability is Wisdom. It can cast the following spell, requiring no components:\n\n3/day: comprehend languages"
                },
                {
                    "name": "Keen Hearing and Sight",
                    "desc": "The stryx has advantage on Wisdom (Perception) checks that rely on hearing or sight."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "tob",
            "document__title": "Tome of Beasts OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "tribal-warrior": {
            "slug": "tribal-warrior",
            "name": "Tribal Warrior",
            "size": "Medium",
            "type": "humanoid",
            "subtype": "any race",
            "group": "null",
            "alignment": "any alignment",
            "armor_class": 12,
            "armor_desc": "hide armor",
            "hit_points": 11,
            "hit_dice": "2d8",
            "speed": {
                "walk": 30
            },
            "strength": 13,
            "dexterity": 11,
            "constitution": 12,
            "intelligence": 8,
            "wisdom": 11,
            "charisma": 8,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 10",
            "languages": "any one language",
            "challenge_rating": "1/8",
            "actions": [
                {
                    "name": "Spear",
                    "desc": "Melee or Ranged Weapon Attack: +3 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d6 + 1) piercing damage, or 5 (1d8 + 1) piercing damage if used with two hands to make a melee attack.",
                    "attack_bonus": 3,
                    "damage_dice": "1d6",
                    "damage_bonus": 1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Pack Tactics",
                    "desc": "The warrior has advantage on an attack roll against a creature if at least one of the warrior's allies is within 5 ft. of the creature and the ally isn't incapacitated."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "wharfling": {
            "slug": "wharfling",
            "name": "Wharfling",
            "size": "Tiny",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 13,
            "armor_desc": "",
            "hit_points": 6,
            "hit_dice": "4d4 . 4",
            "speed": {
                "walk": 30,
                "climb": 30,
                "swim": 20
            },
            "strength": 4,
            "dexterity": 16,
            "constitution": 8,
            "intelligence": 2,
            "wisdom": 12,
            "charisma": 8,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 3,
            "skills": {
                "perception": 3
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 60 ft., passive Perception 13",
            "languages": "-",
            "challenge_rating": "1/8",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) piercing damage, and the target is grappled (escape DC 10). Until this grapple ends, the wharfling can't use its bite on another target. While the target is grappled, the wharfling's bite attack hits it automatically.",
                    "attack_bonus": 5,
                    "damage_dice": "1d4+3"
                },
                {
                    "name": "Pilfer",
                    "desc": "A wharfling that has an opponent grappled at the start of its turn can make a Dexterity (Sleight of Hand) check as a bonus action. The DC for this check equals 10 plus the grappled target's Dexterity modifier. If the check is successful, the wharfling steals some small metallic object from the target, and the theft is unnoticed if the same result equals or exceeds the target's passive Perception. A wharfling flees with its treasure."
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": "",
            "spell_list": [],
            "img_main": "null",
            "document__slug": "tob",
            "document__title": "Tome of Beasts OGL",
            "document__license_url": "http://open5e.com/legal"
        }
    },
    "1/4": {
        "acid-ant": {
            "slug": "acid-ant",
            "name": "Acid Ant",
            "size": "Small",
            "type": "monstrosity",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 13,
            "armor_desc": "natural armor",
            "hit_points": 13,
            "hit_dice": "3d6+3",
            "speed": {
                "walk": 30
            },
            "strength": 8,
            "dexterity": 13,
            "constitution": 12,
            "intelligence": 1,
            "wisdom": 7,
            "charisma": 3,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "acid",
            "condition_immunities": "",
            "senses": "blindsight 60 ft., passive Perception 8",
            "languages": "-",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "attack_bonus": 3,
                    "damage_dice": "2d4",
                    "desc": "Ranged Weapon Attack: +3 to hit, range 20/60 ft., one target. Hit: 5 (2d4) acid damage and the target takes 1 acid damage at the start of its next turn unless the target immediately uses its reaction to wipe off the spit.",
                    "name": "Acid Spit"
                },
                {
                    "attack_bonus": 3,
                    "damage_dice": "1d4+1",
                    "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) piercing damage plus 2 (1d4) acid damage.",
                    "name": "Bite"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "desc": "When the ant is reduced to 0 hp, it explodes in a burst of acid. Each creature within 5 feet of the ant must succeed on a DC 11 Dexterity saving throw or take 5 (2d4) acid damage.",
                    "name": "Explosive Death"
                },
                {
                    "desc": "The ant has advantage on Wisdom (Perception) checks that rely on smell.",
                    "name": "Keen Smell"
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "cc",
            "document__title": "Creature Codex OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "acolyte": {
            "slug": "acolyte",
            "name": "Acolyte",
            "size": "Medium",
            "type": "humanoid",
            "subtype": "any race",
            "group": "null",
            "alignment": "any alignment",
            "armor_class": 10,
            "armor_desc": "null",
            "hit_points": 9,
            "hit_dice": "2d8",
            "speed": {
                "walk": 30
            },
            "strength": 10,
            "dexterity": 10,
            "constitution": 10,
            "intelligence": 10,
            "wisdom": 14,
            "charisma": 11,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {
                "medicine": 4,
                "religion": 2
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 12",
            "languages": "any one language (usually Common)",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Club",
                    "desc": "Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 2 (1d4) bludgeoning damage.",
                    "attack_bonus": 2,
                    "damage_dice": "1d4"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Spellcasting",
                    "desc": "The acolyte is a 1st-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 12, +4 to hit with spell attacks). The acolyte has following cleric spells prepared:\n\n• Cantrips (at will): light, sacred flame, thaumaturgy\n• 1st level (3 slots): bless, cure wounds, sanctuary"
                }
            ],
            "spell_list": [
                "https://api.open5e.com/spells/light/",
                "https://api.open5e.com/spells/sacred-flame/",
                "https://api.open5e.com/spells/thaumaturgy/",
                "https://api.open5e.com/spells/bless/",
                "https://api.open5e.com/spells/cure-wounds/",
                "https://api.open5e.com/spells/sanctuary/"
            ],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "alliumite": {
            "slug": "alliumite",
            "name": "Alliumite",
            "size": "Small",
            "type": "plant",
            "subtype": "",
            "group": "null",
            "alignment": "chaotic neutral",
            "armor_class": 14,
            "armor_desc": "null",
            "hit_points": 18,
            "hit_dice": "4d6+4",
            "speed": {
                "burrow": 20,
                "walk": 30
            },
            "strength": 6,
            "dexterity": 18,
            "constitution": 12,
            "intelligence": 7,
            "wisdom": 12,
            "charisma": 9,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 3,
            "skills": {
                "perception": 3,
                "stealth": 6,
                "survival": 3
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 60 ft., passive Perception 13",
            "languages": "Sylvan",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "attack_bonus": 6,
                    "damage_dice": "1d4+4",
                    "desc": "Ranged Weapon Attack: +6 to hit, range 20/60 ft., one target. Hit: 6 (1d4 + 4) piercing damage.",
                    "name": "Thorn Dart"
                },
                {
                    "attack_bonus": 6,
                    "damage_dice": "1d6+4",
                    "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) slashing damage.",
                    "name": "Grass Blade"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "desc": "The alliumite has advantage on Dexterity (Stealth) checks it makes in any terrain with ample obscuring plant life.",
                    "name": "Plant Camouflage"
                },
                {
                    "desc": "Each creature other than an alliumite within 5 feet of the alliumite when it takes damage must succeed on a DC 13 Constitution saving throw or be blinded until the start of the creature's next turn. On a successful saving throw, the creature is immune to the Tearful Stench of all alliumites for 1 minute.",
                    "name": "Tearful Stench"
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "cc",
            "document__title": "Creature Codex OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "archaeopteryx": {
            "slug": "archaeopteryx",
            "name": "Archaeopteryx",
            "size": "Tiny",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 12,
            "armor_desc": "natural armor",
            "hit_points": 7,
            "hit_dice": "3d4",
            "speed": {
                "fly": 50,
                "walk": 5
            },
            "strength": 6,
            "dexterity": 13,
            "constitution": 10,
            "intelligence": 2,
            "wisdom": 14,
            "charisma": 6,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 12",
            "languages": "-",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "desc": "The archaeopteryx makes two attacks: one with its beak and one with its talons.",
                    "name": "Multiattack"
                },
                {
                    "attack_bonus": 3,
                    "damage_dice": "1d4+1",
                    "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) piercing damage.",
                    "name": "Beak"
                },
                {
                    "attack_bonus": 3,
                    "damage_dice": "1d4+1",
                    "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) slashing damage.",
                    "name": "Talons"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "desc": "The archaeopteryx doesn't provoke opportunity attacks when it flies out of an enemy's reach.",
                    "name": "Flyby"
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "cc",
            "document__title": "Creature Codex OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "axe-beak": {
            "slug": "axe-beak",
            "name": "Axe Beak",
            "size": "Large",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 11,
            "armor_desc": "null",
            "hit_points": 19,
            "hit_dice": "3d10",
            "speed": {
                "walk": 50
            },
            "strength": 14,
            "dexterity": 12,
            "constitution": 12,
            "intelligence": 2,
            "wisdom": 10,
            "charisma": 5,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 10",
            "languages": "",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Beak",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) slashing damage.",
                    "attack_bonus": 4,
                    "damage_dice": "1d8",
                    "damage_bonus": 2
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": "",
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "azza-gremlin": {
            "slug": "azza-gremlin",
            "name": "Azza Gremlin",
            "size": "Small",
            "type": "fey",
            "subtype": "",
            "group": "null",
            "alignment": "neutral",
            "armor_class": 14,
            "armor_desc": "",
            "hit_points": 7,
            "hit_dice": "2d6",
            "speed": {
                "walk": 10,
                "fly": 40,
                "hover": "true"
            },
            "strength": 5,
            "dexterity": 18,
            "constitution": 10,
            "intelligence": 12,
            "wisdom": 13,
            "charisma": 10,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "lightning, thunder",
            "condition_immunities": "",
            "senses": "darkvision 120 ft., passive Perception 11",
            "languages": "Common, Primordial",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Lightning Jolt",
                    "desc": "Melee or Ranged Spell Attack: +6 to hit, reach 5 ft. or range 30 ft., one creature. Hit: 3 (1d6) lightning damage, and the target is affected by Contagious Lightning.",
                    "attack_bonus": 6,
                    "damage_dice": "1d6"
                }
            ],
            "reactions": [
                {
                    "name": "Ride the Bolt",
                    "desc": "The azza gremlin can travel instantly along any bolt of lightning. When it is within 5 feet of a lightning effect, the azza can teleport to any unoccupied space inside or within 5 feet of that lightning effect."
                }
            ],
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Contagious Lightning",
                    "desc": "A creature that touches the azza gremlin or hits it with a melee attack using a metal weapon receives a discharge of lightning. The creature must succeed on a DC 10 Constitution saving throw or attract lightning for 1 minute. For the duration, attacks that cause lightning damage have advantage against this creature, the creature has disadvantage on saving throws against lightning damage and lightning effects, and if the creature takes lightning damage, it is paralyzed until the end of its next turn. An affected creature repeats the saving throw at the end of each of its turns, ending the effect on itself on a success."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "tob",
            "document__title": "Tome of Beasts OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "blink-dog": {
            "slug": "blink-dog",
            "name": "Blink Dog",
            "size": "Medium",
            "type": "fey",
            "subtype": "",
            "group": "null",
            "alignment": "lawful good",
            "armor_class": 13,
            "armor_desc": "null",
            "hit_points": 22,
            "hit_dice": "4d8",
            "speed": {
                "walk": 40
            },
            "strength": 12,
            "dexterity": 17,
            "constitution": 12,
            "intelligence": 10,
            "wisdom": 13,
            "charisma": 11,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 3,
            "skills": {
                "perception": 3,
                "stealth": 5
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 10",
            "languages": "Blink Dog, understands Sylvan but can't speak it",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) piercing damage.",
                    "attack_bonus": 3,
                    "damage_dice": "1d6",
                    "damage_bonus": 1
                },
                {
                    "name": "Teleport (Recharge 4-6)",
                    "desc": "The dog magically teleports, along with any equipment it is wearing or carrying, up to 40 ft. to an unoccupied space it can see. Before or after teleporting, the dog can make one bite attack."
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Keen Hearing and Smell",
                    "desc": "The dog has advantage on Wisdom (Perception) checks that rely on hearing or smell."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "boar": {
            "slug": "boar",
            "name": "Boar",
            "size": "Medium",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 11,
            "armor_desc": "natural armor",
            "hit_points": 11,
            "hit_dice": "2d8",
            "speed": {
                "walk": 40
            },
            "strength": 13,
            "dexterity": 11,
            "constitution": 12,
            "intelligence": 2,
            "wisdom": 9,
            "charisma": 5,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 9",
            "languages": "",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Tusk",
                    "desc": "Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) slashing damage.",
                    "attack_bonus": 3,
                    "damage_dice": "1d6",
                    "damage_bonus": 1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Charge",
                    "desc": "If the boar moves at least 20 ft. straight toward a target and then hits it with a tusk attack on the same turn, the target takes an extra 3 (1d6) slashing damage. If the target is a creature, it must succeed on a DC 11 Strength saving throw or be knocked prone.",
                    "attack_bonus": 0,
                    "damage_dice": "1d6"
                },
                {
                    "name": "Relentless (Recharges after a Short or Long Rest)",
                    "desc": "If the boar takes 7 damage or less that would reduce it to 0 hit points, it is reduced to 1 hit point instead."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "clurichaun": {
            "slug": "clurichaun",
            "name": "Clurichaun",
            "size": "Tiny",
            "type": "fey",
            "subtype": "",
            "group": "null",
            "alignment": "chaotic neutral",
            "armor_class": 14,
            "armor_desc": "",
            "hit_points": 22,
            "hit_dice": "4d4+12",
            "speed": {
                "walk": 30
            },
            "strength": 13,
            "dexterity": 12,
            "constitution": 16,
            "intelligence": 10,
            "wisdom": 8,
            "charisma": 16,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": 5,
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 1,
            "skills": {
                "perception": 1,
                "stealth": 3
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "frightened, poisoned",
            "senses": "darkvision 60ft., passive Perception 11",
            "languages": "Common, Elvish, Sylvan",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Unarmed Strike",
                    "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one creature. Hit: 2 (1 + 1) bludgeoning damage.",
                    "attack_bonus": 3,
                    "damage_dice": "1"
                },
                {
                    "name": "Improvised Weapon",
                    "desc": "Melee or Ranged Weapon Attack: +3 to hit, reach 5 ft. or range 20/60 ft., one creature. Hit: 3 (1d4 + 1) bludgeoning, piercing, or slashing damage, depending on weapon.",
                    "attack_bonus": 3,
                    "damage_dice": "1d4"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Clurichaun's Luck",
                    "desc": "Clurichauns add both their Dexterity and Charisma modifiers to their Armor Class."
                },
                {
                    "name": "Innate Spellcasting",
                    "desc": "the clurichaun's innate spellcasting ability is Charisma (spell save DC 13). The clurichaun can cast the following spells, requiring only alcohol as a component.\n\nat will: friends, mending, minor illusion, purify food and drink, vicious mockery\n\n1/day each: blur, calm emotions, heroism, sleep, suggestion"
                },
                {
                    "name": "Magic Resistance",
                    "desc": "The clurichaun has advantage on saving throws against spells and other magical effects."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "tob",
            "document__title": "Tome of Beasts OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "constrictor-snake": {
            "slug": "constrictor-snake",
            "name": "Constrictor Snake",
            "size": "Large",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 12,
            "armor_desc": "null",
            "hit_points": 13,
            "hit_dice": "2d10",
            "speed": {
                "walk": 30,
                "swim": 30
            },
            "strength": 15,
            "dexterity": 14,
            "constitution": 12,
            "intelligence": 1,
            "wisdom": 10,
            "charisma": 3,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "blindsight 10 ft., passive Perception 10",
            "languages": "",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 5 (1d6 + 2) piercing damage.",
                    "attack_bonus": 4,
                    "damage_dice": "1d6",
                    "damage_bonus": 2
                },
                {
                    "name": "Constrict",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 6 (1d8 + 2) bludgeoning damage, and the target is grappled (escape DC 14). Until this grapple ends, the creature is restrained, and the snake can't constrict another target.",
                    "attack_bonus": 4,
                    "damage_dice": "1d8",
                    "damage_bonus": 2
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": "",
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "dipsa": {
            "slug": "dipsa",
            "name": "Dipsa",
            "size": "Tiny",
            "type": "ooze",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 15,
            "armor_desc": "",
            "hit_points": 27,
            "hit_dice": "6d4+12",
            "speed": {
                "walk": 20,
                "climb": 20,
                "swim": 20
            },
            "strength": 3,
            "dexterity": 17,
            "constitution": 14,
            "intelligence": 1,
            "wisdom": 6,
            "charisma": 1,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {
                "stealth": 7
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "acid",
            "damage_immunities": "",
            "condition_immunities": "blinded, charmed, deafened, exhaustion, frightened, prone",
            "senses": "blindsight 60 ft. (blind beyond this radius), passive Perception 8",
            "languages": "-",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +7 to hit, reach 0 ft., one creature in the dipsa's space. Hit: 1 piercing damage, and the dipsa attaches to the target. A creature with a dipsa attached takes 3 (1d6) acid damage per round per dipsa, and it must make a successful DC 12 Constitution saving throw or have its hit point maximum reduced by an amount equal to the damage taken. If a creature's hit point maximum is reduced to 0 by this effect, the creature dies. This reduction to a creature's hit point maximum lasts until it is affected by a lesser restoration spell or comparable magic.",
                    "attack_bonus": 7,
                    "damage_dice": "1d6"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Swamp Stealth",
                    "desc": "The dipsa gains an additional +2 (+9 in total) to Stealth in swamp terrain."
                },
                {
                    "name": "Amorphous",
                    "desc": "The dipsa can move through a space as narrow as 1 inch wide without squeezing."
                },
                {
                    "name": "Discreet Bite",
                    "desc": "The bite of a dipsa is barely perceptible and the wound is quickly anesthetized. A creature bitten must succeed on a DC 15 Wisdom (Perception) check to notice the attack or any damage taken from it."
                },
                {
                    "name": "Translucent",
                    "desc": "The dipsa can take the Hide action as a bonus action on each of its turns."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "tob",
            "document__title": "Tome of Beasts OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "draft-horse": {
            "slug": "draft-horse",
            "name": "Draft Horse",
            "size": "Large",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 10,
            "armor_desc": "null",
            "hit_points": 19,
            "hit_dice": "3d10",
            "speed": {
                "walk": 40
            },
            "strength": 18,
            "dexterity": 10,
            "constitution": 12,
            "intelligence": 2,
            "wisdom": 11,
            "charisma": 7,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 10",
            "languages": "",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Hooves",
                    "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (2d4 + 4) bludgeoning damage.",
                    "attack_bonus": 6,
                    "damage_dice": "2d4",
                    "damage_bonus": 4
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": "",
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "dretch": {
            "slug": "dretch",
            "name": "Dretch",
            "size": "Small",
            "type": "fiend",
            "subtype": "demon",
            "group": "Demons",
            "alignment": "chaotic evil",
            "armor_class": 11,
            "armor_desc": "natural armor",
            "hit_points": 18,
            "hit_dice": "4d6+4",
            "speed": {
                "walk": 20
            },
            "strength": 11,
            "dexterity": 11,
            "constitution": 12,
            "intelligence": 5,
            "wisdom": 8,
            "charisma": 3,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "cold, fire, lightning",
            "damage_immunities": "poison",
            "condition_immunities": "poisoned",
            "senses": "darkvision 60 ft., passive Perception 9",
            "languages": "Abyssal, telepathy 60 ft. (works only with creatures that understand Abyssal)",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Multiattack",
                    "desc": "The dretch makes two attacks: one with its bite and one with its claws."
                },
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 3 (1d6) piercing damage.",
                    "attack_bonus": 2,
                    "damage_dice": "1d6"
                },
                {
                    "name": "Claws",
                    "desc": "Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 5 (2d4) slashing damage.",
                    "attack_bonus": 2,
                    "damage_dice": "2d4"
                },
                {
                    "name": "Fetid Cloud (1/Day)",
                    "desc": "A 10-foot radius of disgusting green gas extends out from the dretch. The gas spreads around corners, and its area is lightly obscured. It lasts for 1 minute or until a strong wind disperses it. Any creature that starts its turn in that area must succeed on a DC 11 Constitution saving throw or be poisoned until the start of its next turn. While poisoned in this way, the target can take either an action or a bonus action on its turn, not both, and can't take reactions."
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": "",
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "drow": {
            "slug": "drow",
            "name": "Drow",
            "size": "Medium",
            "type": "humanoid",
            "subtype": "elf",
            "group": "null",
            "alignment": "neutral evil",
            "armor_class": 15,
            "armor_desc": "chain shirt",
            "hit_points": 13,
            "hit_dice": "3d8",
            "speed": {
                "walk": 30
            },
            "strength": 10,
            "dexterity": 14,
            "constitution": 10,
            "intelligence": 11,
            "wisdom": 11,
            "charisma": 12,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 2,
            "skills": {
                "perception": 2,
                "stealth": 4
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 120 ft., passive Perception 12",
            "languages": "Elvish, Undercommon",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Shortsword",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage.",
                    "attack_bonus": 4,
                    "damage_dice": "1d6",
                    "damage_bonus": 2
                },
                {
                    "name": "Hand Crossbow",
                    "desc": "Ranged Weapon Attack: +4 to hit, range 30/120 ft., one target. Hit: 5 (1d6 + 2) piercing damage, and the target must succeed on a DC 13 Constitution saving throw or be poisoned for 1 hour. If the saving throw fails by 5 or more, the target is also unconscious while poisoned in this way. The target wakes up if it takes damage or if another creature takes an action to shake it awake.",
                    "attack_bonus": 4,
                    "damage_dice": "1d6",
                    "damage_bonus": 2
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Fey Ancestry",
                    "desc": "The drow has advantage on saving throws against being charmed, and magic can't put the drow to sleep."
                },
                {
                    "name": "Innate Spellcasting",
                    "desc": "The drow's spellcasting ability is Charisma (spell save DC 11). It can innately cast the following spells, requiring no material components:\nAt will: dancing lights\n1/day each: darkness, faerie fire"
                },
                {
                    "name": "Sunlight Sensitivity",
                    "desc": "While in sunlight, the drow has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."
                }
            ],
            "spell_list": [
                "https://api.open5e.com/spells/dancing-lights/",
                "https://api.open5e.com/spells/darkness/",
                "https://api.open5e.com/spells/faerie-fire/"
            ],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "dust-goblin": {
            "slug": "dust-goblin",
            "name": "Dust Goblin",
            "size": "Small",
            "type": "humanoid",
            "subtype": "goblinoid",
            "group": "null",
            "alignment": "neutral evil",
            "armor_class": 14,
            "armor_desc": "leather armor",
            "hit_points": 5,
            "hit_dice": "1d6+2",
            "speed": {
                "walk": 40
            },
            "strength": 8,
            "dexterity": 16,
            "constitution": 14,
            "intelligence": 10,
            "wisdom": 8,
            "charisma": 8,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {
                "stealth": 7
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "charmed, frightened",
            "senses": "darkvision 60 ft., passive Perception 9",
            "languages": "Common, Goblin",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Shortsword",
                    "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) piercing damage.",
                    "attack_bonus": 5,
                    "damage_dice": "1d6"
                },
                {
                    "name": "Light Crossbow",
                    "desc": "Ranged Weapon Attack: +5 to hit, range 80/320 ft., one target. Hit: 6 (1d6 + 3) piercing damage.",
                    "attack_bonus": 5,
                    "damage_dice": "1d6"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Twisted",
                    "desc": "When the dust goblin attacks a creature from hiding, its target must make a successful DC 10 Wisdom saving throw or be frightened until the end of its next turn."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "tob",
            "document__title": "Tome of Beasts OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "elk": {
            "slug": "elk",
            "name": "Elk",
            "size": "Large",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 10,
            "armor_desc": "null",
            "hit_points": 13,
            "hit_dice": "2d10",
            "speed": {
                "walk": 50
            },
            "strength": 16,
            "dexterity": 10,
            "constitution": 12,
            "intelligence": 2,
            "wisdom": 10,
            "charisma": 6,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 10",
            "languages": "",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Ram",
                    "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) bludgeoning damage."
                },
                {
                    "name": "Hooves",
                    "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one prone creature. Hit: 8 (2d4 + 3) bludgeoning damage."
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Charge",
                    "desc": "If the elk moves at least 20 ft. straight toward a target and then hits it with a ram attack on the same turn, the target takes an extra 7 (2d6) damage. If the target is a creature, it must succeed on a DC 13 Strength saving throw or be knocked prone.",
                    "attack_bonus": 0,
                    "damage_dice": "2d6"
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "erina-scrounger": {
            "slug": "erina-scrounger",
            "name": "Erina Scrounger",
            "size": "Small",
            "type": "humanoid",
            "subtype": "erina",
            "group": "null",
            "alignment": "neutral",
            "armor_class": 12,
            "armor_desc": "leather armor",
            "hit_points": 22,
            "hit_dice": "4d6+8",
            "speed": {
                "walk": 20,
                "burrow": 20
            },
            "strength": 9,
            "dexterity": 12,
            "constitution": 14,
            "intelligence": 13,
            "wisdom": 10,
            "charisma": 11,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "poison",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 60 ft., passive Perception 10",
            "languages": "Common, Erina",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Dagger",
                    "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) slashing damage.",
                    "attack_bonus": 3,
                    "damage_dice": "1d4"
                },
                {
                    "name": "Sling",
                    "desc": "Ranged Weapon Attack: +3 to hit, range 30/120 ft., one target. Hit: 4 (1d4 + 2) bludgeoning damage.",
                    "attack_bonus": 3,
                    "damage_dice": "1d4"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Keen Smell",
                    "desc": "The erina has advantage on Wisdom (Perception) checks that rely on smell."
                },
                {
                    "name": "Hardy",
                    "desc": "The erina has advantage on saving throws against poison."
                },
                {
                    "name": "Spines",
                    "desc": "An enemy who hits the erina with a melee attack while within 5 feet of it takes 2 (1d4) piercing damage."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "tob",
            "document__title": "Tome of Beasts OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "exploding-toad": {
            "slug": "exploding-toad",
            "name": "Exploding Toad",
            "size": "Tiny",
            "type": "monstrosity",
            "subtype": "",
            "group": "null",
            "alignment": "chaotic evil",
            "armor_class": 12,
            "armor_desc": "natural armor",
            "hit_points": 2,
            "hit_dice": "1d4",
            "speed": {
                "swim": 20,
                "walk": 20
            },
            "strength": 1,
            "dexterity": 13,
            "constitution": 11,
            "intelligence": 4,
            "wisdom": 8,
            "charisma": 3,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {
                "stealth": 5
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "fire",
            "condition_immunities": "",
            "senses": "darkvision 30 ft., passive Perception 9",
            "languages": "understands Goblin but can't speak",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "attack_bonus": 3,
                    "damage_dice": "1d4+1",
                    "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) piercing damage.",
                    "name": "Bite"
                }
            ],
            "reactions": [
                {
                    "desc": "The exploding toad can turn an attack that missed it into a hit or turn a successful saving throw into a failure.",
                    "name": "Death Leap"
                }
            ],
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "desc": "The toad can breathe air and water.",
                    "name": "Amphibious"
                },
                {
                    "desc": "When the toad is reduced to 0 hp, it explodes in a 10-foot-radius sphere. Each creature in the area must make a DC 11 Dexterity saving throw, taking 10 (3d6) fire damage on a failed save, or half as much damage on a successful one.",
                    "name": "Final Croak"
                },
                {
                    "desc": "Ranged attacks against the toad have disadvantage.",
                    "name": "Mad Hopping"
                },
                {
                    "desc": "When an attack or effect deals fire damage to the toad, the toad can choose to take the fire damage as if it were not immune.",
                    "name": "Selective Immunity"
                },
                {
                    "desc": "The toad's long jump is up to 10 feet and its high jump is up to 5 feet, with or without a running start.",
                    "name": "Standing Leap"
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "cc",
            "document__title": "Creature Codex OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "flying-sword": {
            "slug": "flying-sword",
            "name": "Flying Sword",
            "size": "Small",
            "type": "construct",
            "subtype": "",
            "group": "Animated Objects",
            "alignment": "unaligned",
            "armor_class": 17,
            "armor_desc": "natural armor",
            "hit_points": 17,
            "hit_dice": "5d6",
            "speed": {
                "hover": "true",
                "walk": 0,
                "fly": 50
            },
            "strength": 12,
            "dexterity": 15,
            "constitution": 11,
            "intelligence": 1,
            "wisdom": 5,
            "charisma": 1,
            "strength_save": "null",
            "dexterity_save": 4,
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "poison, psychic",
            "condition_immunities": "blinded, charmed, deafened, frightened, paralyzed, petrified, poisoned",
            "senses": "blindsight 60 ft. (blind beyond this radius), passive Perception 7",
            "languages": "",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Longsword",
                    "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 5 (1d8 + 1) slashing damage.",
                    "attack_bonus": 3,
                    "damage_dice": "1d8",
                    "damage_bonus": 1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Antimagic Susceptibility",
                    "desc": "The sword is incapacitated while in the area of an antimagic field. If targeted by dispel magic, the sword must succeed on a Constitution saving throw against the caster's spell save DC or fall unconscious for 1 minute."
                },
                {
                    "name": "False Appearance",
                    "desc": "While the sword remains motionless and isn't flying, it is indistinguishable from a normal sword."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "garroter-crab": {
            "slug": "garroter-crab",
            "name": "Garroter Crab",
            "size": "Tiny",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 13,
            "armor_desc": "natural armor",
            "hit_points": 18,
            "hit_dice": "4d4+8",
            "speed": {
                "walk": 30,
                "swim": 20
            },
            "strength": 7,
            "dexterity": 14,
            "constitution": 14,
            "intelligence": 1,
            "wisdom": 10,
            "charisma": 2,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "psychic",
            "condition_immunities": "charmed, frightened",
            "senses": "darkvision 60 ft., passive Perception 10",
            "languages": "-",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Whip-claw",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) slashing damage, and the target is grappled (escape DC 8). While grappled, the target cannot speak or cast spells with verbal components.",
                    "attack_bonus": 4,
                    "damage_dice": "1d6"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Amphibious",
                    "desc": "The crab can breathe air and water."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "tob",
            "document__title": "Tome of Beasts OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "giant-badger": {
            "slug": "giant-badger",
            "name": "Giant Badger",
            "size": "Medium",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 10,
            "armor_desc": "null",
            "hit_points": 13,
            "hit_dice": "2d8",
            "speed": {
                "walk": 30,
                "burrow": 10
            },
            "strength": 13,
            "dexterity": 10,
            "constitution": 15,
            "intelligence": 2,
            "wisdom": 12,
            "charisma": 5,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 30 ft., passive Perception 11",
            "languages": "",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Multiattack",
                    "desc": "The badger makes two attacks: one with its bite and one with its claws."
                },
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) piercing damage.",
                    "attack_bonus": 3,
                    "damage_dice": "1d6",
                    "damage_bonus": 1
                },
                {
                    "name": "Claws",
                    "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (2d4 + 1) slashing damage.",
                    "attack_bonus": 3,
                    "damage_dice": "2d4",
                    "damage_bonus": 1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Keen Smell",
                    "desc": "The badger has advantage on Wisdom (Perception) checks that rely on smell."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "giant-bat": {
            "slug": "giant-bat",
            "name": "Giant Bat",
            "size": "Large",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 13,
            "armor_desc": "null",
            "hit_points": 22,
            "hit_dice": "4d10",
            "speed": {
                "walk": 10,
                "fly": 60
            },
            "strength": 15,
            "dexterity": 16,
            "constitution": 11,
            "intelligence": 2,
            "wisdom": 12,
            "charisma": 6,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "blindsight 60 ft., passive Perception 11",
            "languages": "",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 5 (1d6 + 2) piercing damage.",
                    "attack_bonus": 4,
                    "damage_dice": "1d6",
                    "damage_bonus": 2
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Echolocation",
                    "desc": "The bat can't use its blindsight while deafened."
                },
                {
                    "name": "Keen Hearing",
                    "desc": "The bat has advantage on Wisdom (Perception) checks that rely on hearing."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "giant-centipede": {
            "slug": "giant-centipede",
            "name": "Giant Centipede",
            "size": "Small",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 13,
            "armor_desc": "natural armor",
            "hit_points": 4,
            "hit_dice": "1d6",
            "speed": {
                "walk": 30,
                "climb": 30
            },
            "strength": 5,
            "dexterity": 14,
            "constitution": 12,
            "intelligence": 1,
            "wisdom": 7,
            "charisma": 3,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "blindsight 30 ft., passive Perception 8",
            "languages": "",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Bite. Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 4 (1d4 + 2) piercing damage, and the target must succeed on a DC 11 Constitution saving throw or take 10 (3d6) poison damage. If the poison damage reduces the target to 0 hit points, the target is stable but poisoned for 1 hour, even after regaining hit points, and is paralyzed while poisoned in this way.",
                    "attack_bonus": 4,
                    "damage_dice": "1d4",
                    "damage_bonus": 2
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": "",
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "giant-frog": {
            "slug": "giant-frog",
            "name": "Giant Frog",
            "size": "Medium",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 11,
            "armor_desc": "null",
            "hit_points": 18,
            "hit_dice": "4d8",
            "speed": {
                "walk": 30,
                "swim": 30
            },
            "strength": 12,
            "dexterity": 13,
            "constitution": 11,
            "intelligence": 2,
            "wisdom": 10,
            "charisma": 3,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 2,
            "skills": {
                "perception": 2,
                "stealth": 3
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 30 ft., passive Perception 12",
            "languages": "",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) piercing damage, and the target is grappled (escape DC 11). Until this grapple ends, the target is restrained, and the frog can't bite another target.",
                    "attack_bonus": 3,
                    "damage_dice": "1d6",
                    "damage_bonus": 1
                },
                {
                    "name": "Swallow",
                    "desc": "The frog makes one bite attack against a Small or smaller target it is grappling. If the attack hits, the target is swallowed, and the grapple ends. The swallowed target is blinded and restrained, it has total cover against attacks and other effects outside the frog, and it takes 5 (2d4) acid damage at the start of each of the frog's turns. The frog can have only one target swallowed at a time. If the frog dies, a swallowed creature is no longer restrained by it and can escape from the corpse using 5 ft. of movement, exiting prone."
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Amphibious",
                    "desc": "The frog can breathe air and water"
                },
                {
                    "name": "Standing Leap",
                    "desc": "The frog's long jump is up to 20 ft. and its high jump is up to 10 ft., with or without a running start."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "giant-lizard": {
            "slug": "giant-lizard",
            "name": "Giant Lizard",
            "size": "Large",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 12,
            "armor_desc": "natural armor",
            "hit_points": 19,
            "hit_dice": "3d10",
            "speed": {
                "walk": 30,
                "climb": 30
            },
            "strength": 15,
            "dexterity": 12,
            "constitution": 13,
            "intelligence": 2,
            "wisdom": 10,
            "charisma": 5,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 30 ft., passive Perception 10",
            "languages": "",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) piercing damage.",
                    "attack_bonus": 4,
                    "damage_dice": "1d8",
                    "damage_bonus": 2
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Variant: Hold Breath",
                    "desc": "The lizard can hold its breath for 15 minutes. (A lizard that has this trait also has a swimming speed of 30 feet.)"
                },
                {
                    "name": "Variant: Spider Climb",
                    "desc": "The lizard can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "giant-owl": {
            "slug": "giant-owl",
            "name": "Giant Owl",
            "size": "Large",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "neutral",
            "armor_class": 12,
            "armor_desc": "null",
            "hit_points": 19,
            "hit_dice": "3d10",
            "speed": {
                "walk": 5,
                "fly": 60
            },
            "strength": 13,
            "dexterity": 15,
            "constitution": 12,
            "intelligence": 8,
            "wisdom": 13,
            "charisma": 10,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 5,
            "skills": {
                "perception": 5,
                "stealth": 4
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 120 ft., passive Perception 15",
            "languages": "Giant Owl, understands Common, Elvish, and Sylvan but can't speak",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Talons",
                    "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 8 (2d6 + 1) slashing damage.",
                    "attack_bonus": 3,
                    "damage_dice": "2d6",
                    "damage_bonus": 1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Flyby",
                    "desc": "The owl doesn't provoke opportunity attacks when it flies out of an enemy's reach."
                },
                {
                    "name": "Keen Hearing and Sight",
                    "desc": "The owl has advantage on Wisdom (Perception) checks that rely on hearing or sight."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "giant-poisonous-snake": {
            "slug": "giant-poisonous-snake",
            "name": "Giant Poisonous Snake",
            "size": "Medium",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 14,
            "armor_desc": "null",
            "hit_points": 11,
            "hit_dice": "2d8",
            "speed": {
                "walk": 30,
                "swim": 30
            },
            "strength": 10,
            "dexterity": 18,
            "constitution": 13,
            "intelligence": 2,
            "wisdom": 10,
            "charisma": 3,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 2,
            "skills": {
                "perception": 2
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "blindsight 10 ft., passive Perception 12",
            "languages": "",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 6 (1d4 + 4) piercing damage, and the target must make a DC 11 Constitution saving throw, taking 10 (3d6) poison damage on a failed save, or half as much damage on a successful one.",
                    "attack_bonus": 6,
                    "damage_dice": "1d4",
                    "damage_bonus": 4
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": "",
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "giant-wolf-spider": {
            "slug": "giant-wolf-spider",
            "name": "Giant Wolf Spider",
            "size": "Medium",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 13,
            "armor_desc": "null",
            "hit_points": 11,
            "hit_dice": "2d8",
            "speed": {
                "walk": 40,
                "climb": 40
            },
            "strength": 12,
            "dexterity": 16,
            "constitution": 13,
            "intelligence": 3,
            "wisdom": 12,
            "charisma": 4,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 3,
            "skills": {
                "perception": 3,
                "stealth": 7
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "blindsight 10 ft., darkvision 60 ft., passive Perception 13",
            "languages": "",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Weapon Attack: +3 to hit, reach 5 ft., one creature. Hit: 4 (1d6 + 1) piercing damage, and the target must make a DC 11 Constitution saving throw, taking 7 (2d6) poison damage on a failed save, or half as much damage on a successful one. If the poison damage reduces the target to 0 hit points, the target is stable but poisoned for 1 hour, even after regaining hit points, and is paralyzed while poisoned in this way.",
                    "attack_bonus": 3,
                    "damage_dice": "1d6",
                    "damage_bonus": 1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Spider Climb",
                    "desc": "The spider can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check."
                },
                {
                    "name": "Web Sense",
                    "desc": "While in contact with a web, the spider knows the exact location of any other creature in contact with the same web."
                },
                {
                    "name": "Web Walker",
                    "desc": "The spider ignores movement restrictions caused by webbing."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "goblin": {
            "slug": "goblin",
            "name": "Goblin",
            "size": "Small",
            "type": "humanoid",
            "subtype": "goblinoid",
            "group": "null",
            "alignment": "neutral evil",
            "armor_class": 15,
            "armor_desc": "leather armor, shield",
            "hit_points": 7,
            "hit_dice": "2d6",
            "speed": {
                "walk": 30
            },
            "strength": 8,
            "dexterity": 14,
            "constitution": 10,
            "intelligence": 10,
            "wisdom": 8,
            "charisma": 8,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {
                "stealth": 6
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 60 ft., passive Perception 9",
            "languages": "Common, Goblin",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Scimitar",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) slashing damage.",
                    "attack_bonus": 4,
                    "damage_dice": "1d6",
                    "damage_bonus": 2
                },
                {
                    "name": "Shortbow",
                    "desc": "Ranged Weapon Attack: +4 to hit, range 80/320 ft., one target. Hit: 5 (1d6 + 2) piercing damage.",
                    "attack_bonus": 4,
                    "damage_dice": "1d6",
                    "damage_bonus": 2
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Nimble Escape",
                    "desc": "The goblin can take the Disengage or Hide action as a bonus action on each of its turns."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "goreling": {
            "slug": "goreling",
            "name": "Goreling",
            "size": "Small",
            "type": "undead",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 12,
            "armor_desc": "null",
            "hit_points": 11,
            "hit_dice": "2d6+4",
            "speed": {
                "walk": 20
            },
            "strength": 12,
            "dexterity": 14,
            "constitution": 14,
            "intelligence": 1,
            "wisdom": 5,
            "charisma": 1,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "necrotic, poison",
            "condition_immunities": "poisoned",
            "senses": "blindsight 60 ft. (blind beyond this radius), passive Perception 7",
            "languages": "-",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "attack_bonus": 4,
                    "damage_dice": "1d4+2",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) bludgeoning damage plus 2 (1d4) necrotic damage. ++ Reactions",
                    "name": "Slam"
                },
                {
                    "desc": "When a goreling is hit but not reduced to 0 hp, it splits into two new gorelings. Each new goreling has 1 hp, doesn't have this reaction, and is one size smaller than the original goreling.",
                    "name": "Multiplying"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "desc": "If 6 or more gorelings are within 30 feet of one another, they become frenzied and their attacks deal an extra 2 (1d4) necrotic damage.",
                    "name": "Bloodthirsty"
                },
                {
                    "desc": "Up to five gorelings can occupy the same space.",
                    "name": "Swarming"
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "cc",
            "document__title": "Creature Codex OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "grimlock": {
            "slug": "grimlock",
            "name": "Grimlock",
            "size": "Medium",
            "type": "humanoid",
            "subtype": "grimlock",
            "group": "null",
            "alignment": "neutral evil",
            "armor_class": 11,
            "armor_desc": "null",
            "hit_points": 11,
            "hit_dice": "2d8+2",
            "speed": {
                "walk": 30
            },
            "strength": 16,
            "dexterity": 12,
            "constitution": 12,
            "intelligence": 9,
            "wisdom": 8,
            "charisma": 6,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 3,
            "skills": {
                "athletics": 5,
                "perception": 3,
                "stealth": 3
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "blinded",
            "senses": "blindsight 30 ft. or 10 ft. while deafened (blind beyond this radius), passive Perception 13",
            "languages": "Undercommon",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Spiked Bone Club",
                    "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) bludgeoning damage plus 2 (1d4) piercing damage.",
                    "attack_bonus": 5,
                    "damage_dice": "1d4+1d4",
                    "damage_bonus": 5
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Blind Senses",
                    "desc": "The grimlock can't use its blindsight while deafened and unable to smell."
                },
                {
                    "name": "Keen Hearing and Smell",
                    "desc": "The grimlock has advantage on Wisdom (Perception) checks that rely on hearing or smell."
                },
                {
                    "name": "Stone Camouflage",
                    "desc": "The grimlock has advantage on Dexterity (Stealth) checks made to hide in rocky terrain."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "hair-golem": {
            "slug": "hair-golem",
            "name": "Hair Golem",
            "size": "Small",
            "type": "construct",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 13,
            "armor_desc": "null",
            "hit_points": 13,
            "hit_dice": "3d6+3",
            "speed": {
                "walk": 30
            },
            "strength": 10,
            "dexterity": 17,
            "constitution": 13,
            "intelligence": 3,
            "wisdom": 8,
            "charisma": 1,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "slashing",
            "damage_resistances": "bludgeoning and piercing from nonmagical attacks not made with adamantine",
            "damage_immunities": "poison, psychic",
            "condition_immunities": "charmed, exhaustion, frightened, paralyzed, petrified, poisoned",
            "senses": "darkvision 60 ft., passive Perception 9",
            "languages": "understands the languages of its creator but can't speak",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "attack_bonus": 5,
                    "damage_dice": "1d4+3",
                    "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) slashing damage. The target must succeed on a DC 11 Dexterity saving throw or be knocked prone.",
                    "name": "Lash"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "desc": "The golem is immune to any spell or effect that would alter its form.",
                    "name": "Immutable Form"
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "cc",
            "document__title": "Creature Codex OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "inkling": {
            "slug": "inkling",
            "name": "Inkling",
            "size": "Tiny",
            "type": "construct",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 12,
            "armor_desc": "null",
            "hit_points": 10,
            "hit_dice": "4d4",
            "speed": {
                "walk": 20
            },
            "strength": 4,
            "dexterity": 14,
            "constitution": 10,
            "intelligence": 14,
            "wisdom": 12,
            "charisma": 10,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {
                "arcana": 4,
                "stealth": 4
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "blindsight 60 ft. (blind beyond this radius), passive Perception 11",
            "languages": "understands the languages of its creator but can't speak",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "attack_bonus": 4,
                    "damage_dice": "1d4+2",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) slashing damage.",
                    "name": "Lash"
                }
            ],
            "reactions": [
                {
                    "desc": "If a spell attack hits the inkling, it can force the attacker to make a DC 12 Intelligence saving throw. If the attacker fails the saving throw, the spell is redirected to hit another creature of the inkling's choice within 30 feet.",
                    "name": "Redirect Spell"
                }
            ],
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "desc": "The inkling can move through a space as narrow as 1 inch wide without squeezing.",
                    "name": "Amorphous"
                },
                {
                    "desc": "If an inkling spends 24 hours with a spellbook or a spell scroll, it can learn the magic of one 2nd level or lower spell, erasing and absorbing all the ink and magic used to inscribe the spell. The inkling can then cast the spell once per day.",
                    "name": "A Thirst for Knowledge"
                },
                {
                    "desc": "The inkling has advantage on saving throws against spells and other magical effects.",
                    "name": "Magic Resistance"
                },
                {
                    "desc": "The inkling's innate spellcasting ability is Intelligence (spell save DC 12, +4 to hit with spell attacks). It can innately cast the following spells, requiring only somatic components:\nAt will: fire bolt, mending, minor illusion, prestidigitation\n1/day each: color spray, detect magic, magic missile",
                    "name": "Innate Spellcasting"
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "cc",
            "document__title": "Creature Codex OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "kalke": {
            "slug": "kalke",
            "name": "Kalke",
            "size": "Small",
            "type": "fiend",
            "subtype": "",
            "group": "null",
            "alignment": "neutral evil",
            "armor_class": 14,
            "armor_desc": "natural armor",
            "hit_points": 9,
            "hit_dice": "2d6+2",
            "speed": {
                "walk": 30,
                "climb": 30
            },
            "strength": 8,
            "dexterity": 17,
            "constitution": 12,
            "intelligence": 13,
            "wisdom": 7,
            "charisma": 13,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 0,
            "skills": {
                "perception": 0,
                "stealth": 5
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 120 ft., passive Perception 10",
            "languages": "Abyssal, Common, Infernal",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Dagger",
                    "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) piercing damage.",
                    "attack_bonus": 5,
                    "damage_dice": "1d4"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Extinguish Flames",
                    "desc": "Kalkes can extinguish candles, lamps, lanterns and low-burning campfires within 120 feet as a bonus action."
                },
                {
                    "name": "Detect Spellcasting",
                    "desc": "Kalkes can sense spellcasting in a 5-mile radius, as long as the effect is not innate."
                },
                {
                    "name": "Magic Resistance",
                    "desc": "Kalkes have advantage on saving throws against spells and magical effects."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "tob",
            "document__title": "Tome of Beasts OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "lemurfolk": {
            "slug": "lemurfolk",
            "name": "Lemurfolk",
            "size": "Small",
            "type": "humanoid",
            "subtype": "lemurfolk",
            "group": "null",
            "alignment": "neutral",
            "armor_class": 13,
            "armor_desc": "",
            "hit_points": 14,
            "hit_dice": "4d6",
            "speed": {
                "walk": 20,
                "climb": 10,
                "fly": 40
            },
            "strength": 10,
            "dexterity": 15,
            "constitution": 11,
            "intelligence": 12,
            "wisdom": 10,
            "charisma": 8,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {
                "acrobatics": 4,
                "stealth": 4
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 60 ft., passive Perception 10",
            "languages": "Common, Lemurfolk",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Kukri Dagger",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., 20/60 range, one target. Hit: 4 (1d4 + 2) piercing damage.",
                    "attack_bonus": 4,
                    "damage_dice": "1d4"
                },
                {
                    "name": "Blowgun",
                    "desc": "Ranged Weapon Attack: +4 to hit, range 25/100 ft., one creature. Hit: 4 (1d4 + 2) piercing damage, and the target must succeed on a DC 13 Constitution saving throw or be poisoned and unconscious for 1d4 hours. Another creature can use an action to shake the target awake and end its unconsciousness but not the poisoning.",
                    "attack_bonus": 4,
                    "damage_dice": "1d4"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Silent Glide",
                    "desc": "The lemurfolk can glide for 1 minute, making almost no sound. It gains a fly speed of 40 feet, and it must move at least 20 feet on its turn to keep flying. A gliding lemurfolk has advantage on Dexterity (Stealth) checks."
                },
                {
                    "name": "Sneak Attack (1/Turn)",
                    "desc": "The lemurfolk deals an extra 3 (1d6) damage when it hits with a weapon attack and it has advantage, or when the target is within 5 feet of an ally of the lemurfolk that isn't incapacitated and the lemurfolk doesn't have disadvantage on the attack roll."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "tob",
            "document__title": "Tome of Beasts OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "living-shade": {
            "slug": "living-shade",
            "name": "Living Shade",
            "size": "Medium",
            "type": "fey",
            "subtype": "",
            "group": "null",
            "alignment": "neutral",
            "armor_class": 12,
            "armor_desc": "null",
            "hit_points": 18,
            "hit_dice": "4d8",
            "speed": {
                "walk": 40
            },
            "strength": 6,
            "dexterity": 14,
            "constitution": 10,
            "intelligence": 9,
            "wisdom": 10,
            "charisma": 12,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {
                "stealth": 6
            },
            "damage_vulnerabilities": "radiant",
            "damage_resistances": "acid, cold, fire, lightning, thunder; bludgeoning, piercing, and slashing from nonmagical attacks",
            "damage_immunities": "necrotic, poison",
            "condition_immunities": "exhaustion, frightened, grappled, paralyzed, petrified, poisoned, prone, restrained",
            "senses": "darkvision 60 ft., passive Perception 10",
            "languages": "understands Common but can't speak",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "attack_bonus": 4,
                    "damage_dice": "1d4",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 2 (1d4) cold damage.",
                    "name": "Shadow Touch"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "desc": "The living shade can move through a space as narrow as 1 inch wide without squeezing.",
                    "name": "Amorphous"
                },
                {
                    "desc": "While in dim light or darkness, the living shade can take the Hide action as a bonus action.",
                    "name": "Shadow Stealth"
                },
                {
                    "desc": "While in sunlight, the living shade has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight.",
                    "name": "Sunlight Sensitivity"
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "cc",
            "document__title": "Creature Codex OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "living-wick": {
            "slug": "living-wick",
            "name": "Living Wick",
            "size": "Small",
            "type": "construct",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 13,
            "armor_desc": "natural armor",
            "hit_points": 28,
            "hit_dice": "8d6",
            "speed": {
                "walk": 20
            },
            "strength": 10,
            "dexterity": 10,
            "constitution": 10,
            "intelligence": 5,
            "wisdom": 5,
            "charisma": 5,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "poison, psychic",
            "condition_immunities": "blinded, charmed, deafened, exhaustion, frightened, paralyzed, petrified, poisoned, unconscious",
            "senses": "sight 20 ft. (blind beyond the radius of its own light), passive Perception 10",
            "languages": "shares a telepathic link with the individual that lit its wick",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Slam",
                    "desc": "Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 3 (1d6) bludgeoning damage.",
                    "attack_bonus": 2,
                    "damage_dice": "1d6"
                },
                {
                    "name": "Consume Self",
                    "desc": "A living wick can be commanded to rapidly burn through the remains of its wick, creating a devastating fireball. All creatures within 20 feet of the living wick take 7 (2d6) fire damage, or half damage with a successful DC 13 Dexterity saving throw. The fire spreads around corners and ignites flammable objects in the area that aren't being worn or carried. The wick is reduced to a lifeless puddle of wax."
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Controlled",
                    "desc": "Living wicks cannot move, attack, or perform actions when they are not lit. Living wicks only respond to the telepathic commands of the individual that lit them."
                },
                {
                    "name": "Light",
                    "desc": "Activated living wicks produce light as a torch."
                },
                {
                    "name": "Melting",
                    "desc": "A living wick loses one hit point for every 24 hours it remains lit."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "tob",
            "document__title": "Tome of Beasts OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "map-mimic": {
            "slug": "map-mimic",
            "name": "Map Mimic",
            "size": "Tiny",
            "type": "aberration",
            "subtype": "shapechanger",
            "group": "null",
            "alignment": "neutral",
            "armor_class": 14,
            "armor_desc": "natural armor",
            "hit_points": 32,
            "hit_dice": "5d8+10",
            "speed": {
                "walk": 30,
                "fly": 15
            },
            "strength": 10,
            "dexterity": 15,
            "constitution": 14,
            "intelligence": 13,
            "wisdom": 15,
            "charisma": 16,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "acid",
            "condition_immunities": "prone",
            "senses": "darkvision 60 ft., passive Perception 14",
            "languages": "-",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Pseudopod",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) bludgeoning damage. If the mimic is in object form, the target is subjected to its Constrict Face trait.",
                    "attack_bonus": 4,
                    "damage_dice": "1d6"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Shapechanger",
                    "desc": "The mimic can use its action to polymorph into an object or back into its true, amorphous form. Its statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies."
                },
                {
                    "name": "Constrict Face",
                    "desc": "When a map mimic touches a Medium or smaller creature or vice versa, it adheres to the creature, enveloping the creature's face and covering its eyes and ears and airways (escape DC 13). The target creature is immediately blinded and deafened, and it begins suffocating at the beginning of the mimic's next turn."
                },
                {
                    "name": "False Appearance (Object Form Only)",
                    "desc": "While the mimic remains motionless, it is indistinguishable from an ordinary object."
                },
                {
                    "name": "Mimic Page",
                    "desc": "The mimic can disguise itself as any tiny, flat object-a piece of leather, a plate-not only a map. In any form, a map mimic can make a map on its skin leading to its mother mimic."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "tob",
            "document__title": "Tome of Beasts OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "morko": {
            "slug": "morko",
            "name": "Morko",
            "size": "Small",
            "type": "fey",
            "subtype": "",
            "group": "null",
            "alignment": "chaotic evil",
            "armor_class": 12,
            "armor_desc": "null",
            "hit_points": 17,
            "hit_dice": "5d6",
            "speed": {
                "walk": 30
            },
            "strength": 12,
            "dexterity": 15,
            "constitution": 11,
            "intelligence": 12,
            "wisdom": 10,
            "charisma": 8,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 2,
            "skills": {
                "perception": 2,
                "stealth": 6
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "fire, poison",
            "condition_immunities": "",
            "senses": "passive Perception 12",
            "languages": "Elvish, Sylvan",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "attack_bonus": 3,
                    "damage_dice": "1d6+1",
                    "desc": "Melee or Ranged Weapon Attack: +3 to hit, reach 5 ft. and range 20/60 ft., one target. Hit: 4 (1d6 + 1) piercing damage, or 5 (1d8 + 1) piercing damage if used with two hands to make a melee attack.",
                    "name": "Spear"
                },
                {
                    "desc": "The morko fixes its gaze on a creature it can see within 30 feet. The target must make a DC 13 Wisdom saving throw or become cursed with ill manners, taking disadvantage on all ability checks and saving throws based on",
                    "name": "Disdainful Eye (Recharge 6)"
                },
                {
                    "desc": "The curse lasts until removed by the remove curse spell or other magic, or until the creature drinks a pitcher of curdled milk.",
                    "name": "Charisma"
                },
                {
                    "desc": "For 1 minute, the morko magically decreases in size, along with anything it is wearing or carrying. While shrunken, the morko is Tiny, halves its damage dice on Strength-based weapon attacks, and makes Strength checks and Strength saving throws with disadvantage. If the morko lacks the room to grow back to its regular size, it attains the maximum size possible in the space available.",
                    "name": "Shrink (Recharges after a Short or Long Rest)"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "desc": "The morko has advantage on saving throws against spells and other magical effects.",
                    "name": "Magic Resistance"
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "cc",
            "document__title": "Creature Codex OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "necrotic-tick": {
            "slug": "necrotic-tick",
            "name": "Necrotic Tick",
            "size": "Tiny",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 15,
            "armor_desc": "natural armor",
            "hit_points": 3,
            "hit_dice": "1d4+1",
            "speed": {
                "climb": 10,
                "walk": 10
            },
            "strength": 2,
            "dexterity": 14,
            "constitution": 12,
            "intelligence": 1,
            "wisdom": 12,
            "charisma": 8,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": 3,
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 60 ft., passive Perception 11",
            "languages": "-",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 1 piercing damage, and the tick attaches to the target. While attached, the necrotic tick doesn't attack. Instead, at the start of each of the tick's turns, the target loses 5 (1d4 + 3) hp due to blood loss. The target must make a DC 13 Wisdom saving throw. If it fails, it is affected by the tick's toxins and doesn't attempt to remove the tick. The host will even replace a dislodged tick unless prevented from doing so for 1 minute, after which the tick's influence fades. \n\nThe tick can detach itself by spending 5 feet of its movement. It does so when seeking a new host or if the target dies. A creature, including the target, can use its action to detach the tick. When a necrotic tick detaches, voluntarily or otherwise, its host takes 1 necrotic damage.",
                    "name": "Blood Drain"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "desc": "While attached to a living host, a necrotic tick leaks negative energy into the host's bloodstream, quickly closing over the creature's wounds with scabrous, necrotic flesh. If the host doesn't already have regeneration, it regains 2 hp at the start of its turn if it has at least 1 hit point. Track how many “necrotic hp” a host recovers via Necrotic Regeneration. Magical healing reverses the necrosis and subtracts an equal number of necrotic hp from those accumulated. When the necrotic hp equal the host's hit point maximum, the host becomes a zombie.",
                    "name": "Necrotic Regeneration"
                },
                {
                    "desc": "When a necrotic tick's living host has lost three-quarters of its maximum hp from Blood Drain, the tick's toxins fill the host with an unnatural desire to approach other living beings. When a suitable creature is within 5 feet, the tick incites a sudden rage in the host, riding the current host to a new host. The current host must succeed on a DC 13 Wisdom saving throw or it attempts to grapple a living creature within 5 feet of it as a reaction. The host can re-attempt this saving throw at the end of each turn that it suffers damage from the necrotic tick's Blood Drain.",
                    "name": "Ride Host"
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "cc",
            "document__title": "Creature Codex OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "panther": {
            "slug": "panther",
            "name": "Panther",
            "size": "Medium",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 12,
            "armor_desc": "null",
            "hit_points": 13,
            "hit_dice": "3d8",
            "speed": {
                "walk": 50,
                "climb": 40
            },
            "strength": 14,
            "dexterity": 15,
            "constitution": 10,
            "intelligence": 3,
            "wisdom": 14,
            "charisma": 7,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 4,
            "skills": {
                "perception": 4,
                "stealth": 6
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 14",
            "languages": "",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage.",
                    "attack_bonus": 4,
                    "damage_dice": "1d6",
                    "damage_bonus": 2
                },
                {
                    "name": "Claw",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) slashing damage.",
                    "attack_bonus": 4,
                    "damage_dice": "1d4",
                    "damage_bonus": 2
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Keen Smell",
                    "desc": "The panther has advantage on Wisdom (Perception) checks that rely on smell."
                },
                {
                    "name": "Pounce",
                    "desc": "If the panther moves at least 20 ft. straight toward a creature and then hits it with a claw attack on the same turn, that target must succeed on a DC 12 Strength saving throw or be knocked prone. If the target is prone, the panther can make one bite attack against it as a bonus action."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "paper-golem": {
            "slug": "paper-golem",
            "name": "Paper Golem",
            "size": "Tiny",
            "type": "construct",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 13,
            "armor_desc": "null",
            "hit_points": 7,
            "hit_dice": "2d4+2",
            "speed": {
                "fly": 30,
                "walk": 20
            },
            "strength": 8,
            "dexterity": 16,
            "constitution": 12,
            "intelligence": 3,
            "wisdom": 7,
            "charisma": 3,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "fire",
            "damage_resistances": "bludgeoning, piercing, and slashing from nonmagical attacks not made with adamantine",
            "damage_immunities": "poison, psychic",
            "condition_immunities": "charmed, exhaustion, frightened, paralyzed, petrified, poisoned",
            "senses": "darkvision 30 ft., passive perception 8",
            "languages": "understands the languages of its creator but can't speak",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "attack_bonus": 5,
                    "damage_dice": "1d6+3",
                    "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage.",
                    "name": "Paper Cut"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "desc": "While the paper golem remains motionless, it is indistinguishable from an ordinary sheet of paper.",
                    "name": "False Appearance"
                },
                {
                    "desc": "The paper golem is immune to any spell or effect that would alter its form.",
                    "name": "Immutable Form"
                },
                {
                    "desc": "As a bonus action, the paper golem applies ink to itself. The next time it hits a creature with a paper cut attack, the creature must make a DC 13 Constitution saving throw, taking 5 (2d4) poison damage on a failed save, or half as much damage on a successful one.",
                    "name": "Ink Blot (Recharge 4-6)"
                },
                {
                    "desc": "The paper golem's weapon attacks are magical.",
                    "name": "Magic Weapons"
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "cc",
            "document__title": "Creature Codex OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "pseudodragon": {
            "slug": "pseudodragon",
            "name": "Pseudodragon",
            "size": "Tiny",
            "type": "dragon",
            "subtype": "",
            "group": "null",
            "alignment": "neutral good",
            "armor_class": 13,
            "armor_desc": "natural armor",
            "hit_points": 7,
            "hit_dice": "2d4+2",
            "speed": {
                "walk": 15,
                "fly": 60
            },
            "strength": 6,
            "dexterity": 15,
            "constitution": 13,
            "intelligence": 10,
            "wisdom": 12,
            "charisma": 10,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 3,
            "skills": {
                "perception": 3,
                "stealth": 4
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "blindsight 10 ft., darkvision 60 ft., passive Perception 13",
            "languages": "understands Common and Draconic but can't speak",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage.",
                    "attack_bonus": 4,
                    "damage_dice": "1d4",
                    "damage_bonus": 2
                },
                {
                    "name": "Sting",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 4 (1d4 + 2) piercing damage, and the target must succeed on a DC 11 Constitution saving throw or become poisoned for 1 hour. If the saving throw fails by 5 or more, the target falls unconscious for the same duration, or until it takes damage or another creature uses an action to shake it awake.",
                    "attack_bonus": 4,
                    "damage_dice": "1d4",
                    "damage_bonus": 2
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Keen Senses",
                    "desc": "The pseudodragon has advantage on Wisdom (Perception) checks that rely on sight, hearing, or smell."
                },
                {
                    "name": "Magic Resistance",
                    "desc": "The pseudodragon has advantage on saving throws against spells and other magical effects."
                },
                {
                    "name": "Limited Telepathy",
                    "desc": "The pseudodragon can magically communicate simple ideas, emotions, and images telepathically with any creature within 100 ft. of it that can understand a language."
                },
                {
                    "name": "Variant: Familiar",
                    "desc": "The pseudodragon can serve another creature as a familiar, forming a magic, telepathic bond with that willing companion. While the two are bonded, the companion can sense what the pseudodragon senses as long as they are within 1 mile of each other. While the pseudodragon is within 10 feet of its companion, the companion shares the pseudodragon's Magic Resistance trait. At any time and for any reason, the pseudodragon can end its service as a familiar, ending the telepathic bond."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "ramag": {
            "slug": "ramag",
            "name": "Ramag",
            "size": "Medium",
            "type": "humanoid",
            "subtype": "ramag",
            "group": "null",
            "alignment": "neutral",
            "armor_class": 13,
            "armor_desc": "leather armor",
            "hit_points": 27,
            "hit_dice": "6d8",
            "speed": {
                "walk": 30
            },
            "strength": 9,
            "dexterity": 14,
            "constitution": 10,
            "intelligence": 16,
            "wisdom": 12,
            "charisma": 11,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {
                "arcana": 5,
                "investigation": 5
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception $1",
            "languages": "Common",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Scimitar",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) slashing damage.",
                    "attack_bonus": 4,
                    "damage_dice": "1d6"
                },
                {
                    "name": "Shortbow",
                    "desc": "Ranged Weapon Attack: +4 to hit, range 80/320 ft., one target. Hit: 5 (1d6 + 2) piercing damage.",
                    "attack_bonus": 4,
                    "damage_dice": "1d6"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Magic Resistance",
                    "desc": "The ramag has advantage on saving throws against spells or other magical effects."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "tob",
            "document__title": "Tome of Beasts OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "ratfolk": {
            "slug": "ratfolk",
            "name": "Ratfolk",
            "size": "Small",
            "type": "humanoid",
            "subtype": "ratfolk",
            "group": "null",
            "alignment": "neutral",
            "armor_class": 14,
            "armor_desc": "studded leather armor",
            "hit_points": 7,
            "hit_dice": "2d6",
            "speed": {
                "walk": 25,
                "swim": 10
            },
            "strength": 7,
            "dexterity": 15,
            "constitution": 11,
            "intelligence": 14,
            "wisdom": 10,
            "charisma": 10,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 2,
            "skills": {
                "perception": 2
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 60 ft., passive Perception 12",
            "languages": "Common",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Dagger",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage.",
                    "attack_bonus": 4,
                    "damage_dice": "1d4"
                },
                {
                    "name": "Light crossbow",
                    "desc": "Ranged Weapon Attack: +4 to hit, range 80/320 ft., one target. Hit: 6 (1d8 + 2) piercing damage.",
                    "attack_bonus": 4,
                    "damage_dice": "1d8"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Nimbleness",
                    "desc": "The ratfolk can move through the space of any creature size Medium or larger."
                },
                {
                    "name": "Pack Tactics",
                    "desc": "The ratfolk has advantage on its attack roll against a creature if at least one of the ratfolk's allies is within 5 feet of the creature and the ally is capable of attacking."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "tob",
            "document__title": "Tome of Beasts OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "red-banded-line-spider": {
            "slug": "red-banded-line-spider",
            "name": "Red-Banded Line Spider",
            "size": "Tiny",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 13,
            "armor_desc": "",
            "hit_points": 2,
            "hit_dice": "1d4",
            "speed": {
                "walk": 30,
                "climb": 30
            },
            "strength": 4,
            "dexterity": 16,
            "constitution": 10,
            "intelligence": 1,
            "wisdom": 10,
            "charisma": 2,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 2,
            "skills": {
                "perception": 2,
                "stealth": 5
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "psychic",
            "condition_immunities": "charmed, frightened",
            "senses": "darkvision 60 ft., passive Perception 12",
            "languages": "-",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 1 piercing damage, and the target must succeed on a DC 10 Constitution saving throw or take 3 (1d6) poison damage and be poisoned until the start of the spider's next turn. The target fails the saving throw automatically and takes an extra 1d6 poison damage if it is bitten by another red-banded line spider while poisoned this way.",
                    "attack_bonus": 5,
                    "damage_dice": "1d6"
                },
                {
                    "name": "Swingline",
                    "desc": "Ranged Weapon Attack: +5 to hit, range 60 ft., one target. Hit: the spider immediately moves the full length of the webbing (up to 60 feet) to the target and delivers a bite with advantage. This attack can be used only if the spider is higher than its target and at least 10 feet away.",
                    "attack_bonus": 5,
                    "damage_dice": "0"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Spider Climb",
                    "desc": "The spider can climb difficult surfaces, including upside down and on ceilings, without needing to make an ability check."
                },
                {
                    "name": "Web Walker",
                    "desc": "The spider ignores movement restrictions caused by webbing."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "tob",
            "document__title": "Tome of Beasts OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "riding-horse": {
            "slug": "riding-horse",
            "name": "Riding Horse",
            "size": "Large",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 10,
            "armor_desc": "null",
            "hit_points": 13,
            "hit_dice": "2d10",
            "speed": {
                "walk": 60
            },
            "strength": 16,
            "dexterity": 10,
            "constitution": 12,
            "intelligence": 2,
            "wisdom": 11,
            "charisma": 7,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 10",
            "languages": "",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Hooves",
                    "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (2d4 + 3) bludgeoning damage.",
                    "attack_bonus": 5,
                    "damage_dice": "2d4",
                    "damage_bonus": 3
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": "",
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "rimewing": {
            "slug": "rimewing",
            "name": "Rimewing",
            "size": "Small",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 12,
            "armor_desc": "null",
            "hit_points": 22,
            "hit_dice": "5d6+5",
            "speed": {
                "fly": 30,
                "walk": 25
            },
            "strength": 11,
            "dexterity": 14,
            "constitution": 12,
            "intelligence": 3,
            "wisdom": 10,
            "charisma": 7,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 2,
            "skills": {
                "perception": 2,
                "stealth": 4
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "cold",
            "condition_immunities": "",
            "senses": "darkvision 60 ft., passive Perception 12",
            "languages": "-",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "attack_bonus": 4,
                    "damage_dice": "1d6+2",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage.",
                    "name": "Proboscis"
                },
                {
                    "desc": "A 20-foot radius cloud of colorful ice crystals extends from the rimewing. Each creature in that area must succeed on a DC 10 Wisdom saving throw or be charmed by the rimewing for 1 minute. While charmed by the rimewing, a creature is incapacitated and must move up to its speed toward the rimewing at the start of its turn, stopping when it is 5 feet away. A charmed creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.",
                    "name": "Frosted Wings (1/Day)"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "desc": "The giant moth has advantage on Wisdom (Perception) checks that rely on smell.",
                    "name": "Antennae"
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "cc",
            "document__title": "Creature Codex OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "roachling-skirmisher": {
            "slug": "roachling-skirmisher",
            "name": "Roachling Skirmisher",
            "size": "Small",
            "type": "humanoid",
            "subtype": "roachling",
            "group": "null",
            "alignment": "chaotic neutral",
            "armor_class": 13,
            "armor_desc": "natural armor",
            "hit_points": 7,
            "hit_dice": "2d6",
            "speed": {
                "walk": 25
            },
            "strength": 10,
            "dexterity": 14,
            "constitution": 11,
            "intelligence": 10,
            "wisdom": 9,
            "charisma": 8,
            "strength_save": "null",
            "dexterity_save": 4,
            "constitution_save": 2,
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {
                "acrobatics": 4,
                "stealth": 6
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 60 ft., tremorsense 10 ft., passive Perception 9",
            "languages": "Common",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Shortsword",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage.",
                    "attack_bonus": 4,
                    "damage_dice": "1d6"
                },
                {
                    "name": "Dart",
                    "desc": "Ranged Weapon Attack: +4 to hit, range 20/60 ft., one target. Hit: 4 (1d4 + 2) piercing damage.",
                    "attack_bonus": 4,
                    "damage_dice": "1d4"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Resistant",
                    "desc": "The roachling skirmisher has advantage on Constitution saving throws."
                },
                {
                    "name": "Unlovely",
                    "desc": "The skirmisher has disadvantage on Performance and Persuasion checks in interactions with nonroachlings."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "tob",
            "document__title": "Tome of Beasts OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "shadow-fey": {
            "slug": "shadow-fey",
            "name": "Shadow Fey",
            "size": "Medium",
            "type": "humanoid",
            "subtype": "elf",
            "group": "null",
            "alignment": "lawful evil",
            "armor_class": 15,
            "armor_desc": "chain shirt",
            "hit_points": 31,
            "hit_dice": "7d8",
            "speed": {
                "walk": 30
            },
            "strength": 10,
            "dexterity": 14,
            "constitution": 10,
            "intelligence": 11,
            "wisdom": 11,
            "charisma": 13,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 2,
            "skills": {
                "arcana": 2,
                "perception": 2
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 60 ft., passive Perception 12",
            "languages": "Common, Elvish, Umbral",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Shortsword",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage.",
                    "attack_bonus": 4,
                    "damage_dice": "1d6"
                },
                {
                    "name": "Shortbow",
                    "desc": "Ranged Weapon Attack: +4 to hit, range 80/320 ft., one target. Hit: 5 (1d6 + 2) piercing damage.",
                    "attack_bonus": 4,
                    "damage_dice": "1d6"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Fey Ancestry",
                    "desc": "The shadow fey has advantage on saving throws against being charmed, and magic can't put it to sleep."
                },
                {
                    "name": "Innate Spellcasting",
                    "desc": "the shadow fey's innate spellcasting ability is Charisma. It can cast the following spells innately, requiring no material components.\n\n1/day: misty step (when in shadows, dim light, or darkness only)"
                },
                {
                    "name": "Sunlight Sensitivity",
                    "desc": "While in sunlight, the shadow fey has disadvantage on attack rolls and on Wisdom (Perception) checks that rely on sight."
                },
                {
                    "name": "Traveler in Darkness",
                    "desc": "The shadow fey has advantage on Intelligence (Arcana) checks made to know about shadow roads and shadow magic spells or items."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "tob",
            "document__title": "Tome of Beasts OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "skeleton": {
            "slug": "skeleton",
            "name": "Skeleton",
            "size": "Medium",
            "type": "undead",
            "subtype": "",
            "group": "Skeletons",
            "alignment": "lawful evil",
            "armor_class": 13,
            "armor_desc": "armor scraps",
            "hit_points": 13,
            "hit_dice": "2d8+4",
            "speed": {
                "walk": 30
            },
            "strength": 10,
            "dexterity": 14,
            "constitution": 15,
            "intelligence": 6,
            "wisdom": 8,
            "charisma": 5,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "bludgeoning",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "poisoned",
            "senses": "darkvision 60 ft., passive Perception 9",
            "languages": "understands all languages it spoke in life but can't speak",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Shortsword",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage.",
                    "attack_bonus": 4,
                    "damage_dice": "1d6",
                    "damage_bonus": 2
                },
                {
                    "name": "Shortbow",
                    "desc": "Ranged Weapon Attack: +4 to hit, range 80/320 ft., one target. Hit: 5 (1d6 + 2) piercing damage.",
                    "attack_bonus": 4,
                    "damage_dice": "1d6",
                    "damage_bonus": 2
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": "",
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "skull-lantern": {
            "slug": "skull-lantern",
            "name": "Skull Lantern",
            "size": "Tiny",
            "type": "undead",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 13,
            "armor_desc": "null",
            "hit_points": 14,
            "hit_dice": "4d4+4",
            "speed": {
                "fly": 30,
                "hover": "true",
                "walk": 0
            },
            "strength": 1,
            "dexterity": 16,
            "constitution": 12,
            "intelligence": 3,
            "wisdom": 6,
            "charisma": 5,
            "strength_save": "null",
            "dexterity_save": 5,
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "poison",
            "condition_immunities": "charmed, exhaustion, frightened, paralyzed, poisoned, prone, unconscious",
            "senses": "passive Perception 8",
            "languages": "-",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "attack_bonus": 5,
                    "damage_dice": "1d4+3",
                    "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) piercing damage.",
                    "name": "Bite"
                },
                {
                    "desc": "The skull lantern opens its mouth, releasing a searing beam of light in a 15-foot line that is 5 feet wide. Each creature in that line must make a DC 13 Dexterity saving throw, taking 7 (2d6) fire damage on a failed save, or half as much damage on a successful one.",
                    "name": "Fire Beam (Recharge 6)"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "desc": "When immersed in magical darkness, a skull lantern emits a brilliant flash of light powerful enough to dispel magical darkness in a 30-foot-radius sphere centered on itself, illuminating the area with bright light for 1d4 rounds. Afterwards, the light winks out and the skull falls to the ground, inert. In one week, the skull lantern has a 50% chance of becoming active again, though failure to do so means it will never reanimate.",
                    "name": "Flare"
                },
                {
                    "desc": "The skull lantern sheds bright light in a 20-foot-radius and dim light for an additional 20 feet.",
                    "name": "Illumination"
                },
                {
                    "desc": "If damage reduces the skull to 0 hp, it must make a Constitution saving throw with a DC of 5 + the damage taken, unless the damage is radiant or from a critical hit. On a success, the skull drops to 1 hp instead.",
                    "name": "Undead Fortitude"
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "cc",
            "document__title": "Creature Codex OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "snow-cat": {
            "slug": "snow-cat",
            "name": "Snow Cat",
            "size": "Medium",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 12,
            "armor_desc": "null",
            "hit_points": 13,
            "hit_dice": "3d8",
            "speed": {
                "climb": 40,
                "walk": 50
            },
            "strength": 14,
            "dexterity": 14,
            "constitution": 10,
            "intelligence": 3,
            "wisdom": 14,
            "charisma": 7,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 4,
            "skills": {
                "perception": 4,
                "stealth": 6
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 14",
            "languages": "-",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "attack_bonus": 4,
                    "damage_dice": "1d6+2",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 5 (1d6 + 2) piercing damage.",
                    "name": "Bite"
                },
                {
                    "attack_bonus": 4,
                    "damage_dice": "1d4+2",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 4 (1d4 + 2) slashing damage.",
                    "name": "Claw"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "desc": "The snow cat has advantage on Wisdom (Perception) checks that rely on sight, hearing, or smell.",
                    "name": "Keen Senses"
                },
                {
                    "desc": "If the snow cat surprises a creature and hits it with a bite attack, the target is grappled (escape DC 12) if it is a Medium or smaller creature.",
                    "name": "Stalker"
                },
                {
                    "desc": "The snow cat has advantage on Dexterity (Stealth) checks made to hide in snowy terrain.",
                    "name": "Snow Camouflage"
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "cc",
            "document__title": "Creature Codex OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "sootwing": {
            "slug": "sootwing",
            "name": "Sootwing",
            "size": "Small",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 11,
            "armor_desc": "null",
            "hit_points": 13,
            "hit_dice": "3d6+3",
            "speed": {
                "fly": 30,
                "walk": 25
            },
            "strength": 11,
            "dexterity": 12,
            "constitution": 12,
            "intelligence": 3,
            "wisdom": 10,
            "charisma": 7,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 2,
            "skills": {
                "perception": 2,
                "stealth": 3
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "fire",
            "condition_immunities": "",
            "senses": "darkvision 60 ft., passive Perception 12",
            "languages": "-",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "attack_bonus": 3,
                    "damage_dice": "1d6+1",
                    "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) piercing damage.",
                    "name": "Proboscis"
                },
                {
                    "desc": "A 20-foot radius cloud of smoldering ash disperses from the sootwing. Each creature in that area must make a DC 11 Constitution saving throw. On a failure, a creature takes 4 (1d8) fire damage and is blinded until the end of its next turn. On a success, a creature takes half the damage and isn't blinded.",
                    "name": "Sooty Wings (1/Day)"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "desc": "The giant moth has advantage on Wisdom (Perception) checks that rely on smell.",
                    "name": "Antennae"
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "cc",
            "document__title": "Creature Codex OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "sprite": {
            "slug": "sprite",
            "name": "Sprite",
            "size": "Tiny",
            "type": "fey",
            "subtype": "",
            "group": "null",
            "alignment": "neutral good",
            "armor_class": 15,
            "armor_desc": "leather armor",
            "hit_points": 2,
            "hit_dice": "1d4",
            "speed": {
                "walk": 10,
                "fly": 40
            },
            "strength": 3,
            "dexterity": 18,
            "constitution": 10,
            "intelligence": 14,
            "wisdom": 13,
            "charisma": 11,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 3,
            "skills": {
                "perception": 3,
                "stealth": 8
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 13",
            "languages": "Common, Elvish, Sylvan",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Longsword",
                    "desc": "Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 1 slashing damage.",
                    "attack_bonus": 2,
                    "damage_bonus": 1
                },
                {
                    "name": "Shortbow",
                    "desc": "Ranged Weapon Attack: +6 to hit, range 40/160 ft., one target. Hit: 1 piercing damage, and the target must succeed on a DC 10 Constitution saving throw or become poisoned for 1 minute. If its saving throw result is 5 or lower, the poisoned target falls unconscious for the same duration, or until it takes damage or another creature takes an action to shake it awake.",
                    "attack_bonus": 6,
                    "damage_bonus": 1
                },
                {
                    "name": "Heart Sight",
                    "desc": "The sprite touches a creature and magically knows the creature's current emotional state. If the target fails a DC 10 Charisma saving throw, the sprite also knows the creature's alignment. Celestials, fiends, and undead automatically fail the saving throw."
                },
                {
                    "name": "Invisibility",
                    "desc": "The sprite magically turns invisible until it attacks or casts a spell, or until its concentration ends (as if concentrating on a spell). Any equipment the sprite wears or carries is invisible with it."
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": "",
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "steam-mephit": {
            "slug": "steam-mephit",
            "name": "Steam Mephit",
            "size": "Small",
            "type": "elemental",
            "subtype": "",
            "group": "Mephits",
            "alignment": "neutral evil",
            "armor_class": 10,
            "armor_desc": "null",
            "hit_points": 21,
            "hit_dice": "6d6",
            "speed": {
                "walk": 30,
                "fly": 30
            },
            "strength": 5,
            "dexterity": 11,
            "constitution": 10,
            "intelligence": 11,
            "wisdom": 10,
            "charisma": 12,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "fire, poison",
            "condition_immunities": "poisoned",
            "senses": "darkvision 60 ft., passive Perception 10",
            "languages": "Aquan, Ignan",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Claws",
                    "desc": "Melee Weapon Attack: +2 to hit, reach 5 ft., one creature. Hit: 2 (1d4) slashing damage plus 2 (1d4) fire damage.",
                    "attack_bonus": 2,
                    "damage_dice": "2d4"
                },
                {
                    "name": "Steam Breath (Recharge 6)",
                    "desc": "The mephit exhales a 15-foot cone of scalding steam. Each creature in that area must succeed on a DC 10 Dexterity saving throw, taking 4 (1d8) fire damage on a failed save, or half as much damage on a successful one."
                },
                {
                    "name": "Variant: Summon Mephits (1/Day)",
                    "desc": "The mephit has a 25 percent chance of summoning 1d4 mephits of its kind. A summoned mephit appears in an unoccupied space within 60 feet of its summoner, acts as an ally of its summoner, and can't summon other mephits. It remains for 1 minute, until it or its summoner dies, or until its summoner dismisses it as an action."
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Death Burst",
                    "desc": "When the mephit dies, it explodes in a cloud of steam. Each creature within 5 ft. of the mephit must succeed on a DC 10 Dexterity saving throw or take 4 (1d8) fire damage.",
                    "attack_bonus": 0,
                    "damage_dice": "1d8"
                },
                {
                    "name": "Innate Spellcasting (1/Day)",
                    "desc": "The mephit can innately cast _blur_, requiring no material components. Its innate spellcasting ability is Charisma."
                }
            ],
            "spell_list": [
                "https://api.open5e.com/spells/blur/"
            ],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "suturefly": {
            "slug": "suturefly",
            "name": "Suturefly",
            "size": "Tiny",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 14,
            "armor_desc": "",
            "hit_points": 7,
            "hit_dice": "3d4",
            "speed": {
                "hover": "true",
                "walk": 10,
                "fly": 40
            },
            "strength": 1,
            "dexterity": 19,
            "constitution": 10,
            "intelligence": 1,
            "wisdom": 12,
            "charisma": 4,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {
                "stealth": 6
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 60 ft., passive Perception 11",
            "languages": "-",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Sew",
                    "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 1 piercing damage, and the suturefly sews the target's mouth, nose, or eye closed. With supernatural speed, the suturefly repeatedly pierces the target's face, each time threading a loop of the target's own skin through the previous hole. These skin loops rapidly blacken, shrink, and draw the orifice tightly closed. It takes two actions and a sharp blade to sever the loops and reopen the orifice, and the process causes intense pain and 2 slashing damage. A victim whose mouth and nose have been sewn shut begins suffocating at the start of his or her next turn.",
                    "attack_bonus": 6,
                    "damage_dice": "1"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Camouflage",
                    "desc": "A suturefly in forest surroundings has advantage on Dexterity (Stealth) checks."
                },
                {
                    "name": "Detect Blasphemy",
                    "desc": "The most common variety of suturefly attacks any creature that blasphemes aloud, which it can detect at a range of 100 feet unless the blasphemer makes a successful DC 13 Charisma saving throw."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "tob",
            "document__title": "Tome of Beasts OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "swamp-adder": {
            "slug": "swamp-adder",
            "name": "Swamp Adder",
            "size": "Small",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 13,
            "armor_desc": "",
            "hit_points": 18,
            "hit_dice": "4d6+4",
            "speed": {
                "walk": 30
            },
            "strength": 4,
            "dexterity": 16,
            "constitution": 12,
            "intelligence": 1,
            "wisdom": 10,
            "charisma": 4,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "blindsight 10 ft., passive Perception 10",
            "languages": "-",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 1 piercing damage, and the target must make a successful DC 11 saving throw or become poisoned. While poisoned this way, the target is paralyzed and takes 3(1d6) poison damage at the start of each of its turns. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself with a success.",
                    "attack_bonus": 5,
                    "damage_dice": "1d6"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Swamp Camouflage",
                    "desc": "The swamp adder has advantage on Dexterity (Stealth) checks while in swamp terrain."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "tob",
            "document__title": "Tome of Beasts OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "swarm-of-bats": {
            "slug": "swarm-of-bats",
            "name": "Swarm of Bats",
            "size": "Medium",
            "type": "swarm of Tiny beasts",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 12,
            "armor_desc": "null",
            "hit_points": 22,
            "hit_dice": "5d8",
            "speed": {
                "walk": 0,
                "fly": 30
            },
            "strength": 5,
            "dexterity": 15,
            "constitution": 10,
            "intelligence": 2,
            "wisdom": 12,
            "charisma": 4,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "bludgeoning, piercing, slashing",
            "damage_immunities": "",
            "condition_immunities": "charmed, frightened, grappled, paralyzed, petrified, prone, restrained, stunned",
            "senses": "blindsight 60 ft., passive Perception 11",
            "languages": "",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Bites",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 0 ft., one creature in the swarm's space. Hit: 5 (2d4) piercing damage, or 2 (1d4) piercing damage if the swarm has half of its hit points or fewer.",
                    "attack_bonus": 4,
                    "damage_dice": "2d4"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Echolocation",
                    "desc": "The swarm can't use its blindsight while deafened."
                },
                {
                    "name": "Keen Hearing",
                    "desc": "The swarm has advantage on Wisdom (Perception) checks that rely on hearing."
                },
                {
                    "name": "Swarm",
                    "desc": "The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening large enough for a Tiny bat. The swarm can't regain hit points or gain temporary hit points."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "swarm-of-rats": {
            "slug": "swarm-of-rats",
            "name": "Swarm of Rats",
            "size": "Medium",
            "type": "swarm of Tiny beasts",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 10,
            "armor_desc": "null",
            "hit_points": 24,
            "hit_dice": "7d8",
            "speed": {
                "walk": 30
            },
            "strength": 9,
            "dexterity": 11,
            "constitution": 9,
            "intelligence": 2,
            "wisdom": 10,
            "charisma": 3,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "bludgeoning, piercing, slashing",
            "damage_immunities": "",
            "condition_immunities": "charmed, frightened, grappled, paralyzed, petrified, prone, restrained, stunned",
            "senses": "darkvision 30 ft., passive Perception 10",
            "languages": "",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Bites",
                    "desc": "Melee Weapon Attack: +2 to hit, reach 0 ft., one target in the swarm's space. Hit: 7 (2d6) piercing damage, or 3 (1d6) piercing damage if the swarm has half of its hit points or fewer.",
                    "attack_bonus": 2,
                    "damage_dice": "2d6"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Keen Smell",
                    "desc": "The swarm has advantage on Wisdom (Perception) checks that rely on smell."
                },
                {
                    "name": "Swarm",
                    "desc": "The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening large enough for a Tiny rat. The swarm can't regain hit points or gain temporary hit points."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "swarm-of-ravens": {
            "slug": "swarm-of-ravens",
            "name": "Swarm of Ravens",
            "size": "Medium",
            "type": "swarm of Tiny beasts",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 12,
            "armor_desc": "null",
            "hit_points": 24,
            "hit_dice": "7d8",
            "speed": {
                "walk": 10,
                "fly": 50
            },
            "strength": 6,
            "dexterity": 14,
            "constitution": 8,
            "intelligence": 3,
            "wisdom": 12,
            "charisma": 6,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "bludgeoning, piercing, slashing",
            "damage_immunities": "",
            "condition_immunities": "charmed, frightened, grappled, paralyzed, petrified, prone, restrained, stunned",
            "senses": "passive Perception 15",
            "languages": "",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Beaks",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target in the swarm's space. Hit: 7 (2d6) piercing damage, or 3 (1d6) piercing damage if the swarm has half of its hit points or fewer.",
                    "attack_bonus": 4,
                    "damage_dice": "2d6"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Swarm",
                    "desc": "The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening large enough for a Tiny raven. The swarm can't regain hit points or gain temporary hit points."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "treacle": {
            "slug": "treacle",
            "name": "Treacle",
            "size": "Tiny",
            "type": "ooze",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 13,
            "armor_desc": "natural armor",
            "hit_points": 22,
            "hit_dice": "4d4+12",
            "speed": {
                "walk": 15,
                "climb": 10
            },
            "strength": 4,
            "dexterity": 6,
            "constitution": 17,
            "intelligence": 1,
            "wisdom": 1,
            "charisma": 10,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {
                "deception": 4
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "blindsight 60 ft., passive Perception 10",
            "languages": "-",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Reshape",
                    "desc": "The treacle assumes the shape of any tiny creature or object. A reshaped treacle gains the movement of its new form but no other special qualities."
                },
                {
                    "name": "Blood Drain (1/hour)",
                    "desc": "A treacle touching the skin of a warm-blooded creature inflicts 4 (1d8) necrotic damage per hour of contact, and the victim's maximum hit points are reduced by the same number. Blood is drained so slowly that the victim doesn't notice the damage unless he or she breaks contact with the treacle (sets it down or hands it to someone else, for example). When contact is broken, the victim notices blood on his or her skin or clothes with a successful DC 13 Wisdom (Perception) check."
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Amorphous",
                    "desc": "The treacle can move through a space as narrow as 1 inch wide without squeezing."
                },
                {
                    "name": "Charming Presence",
                    "desc": "The treacle has an uncanny ability to sense and to play off of another creature's emotions. It uses Charisma (Deception) to oppose Wisdom (Insight or Perception) skill checks made to see through its ruse, and it has advantage on its check."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "tob",
            "document__title": "Tome of Beasts OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "violet-fungus": {
            "slug": "violet-fungus",
            "name": "Violet Fungus",
            "size": "Medium",
            "type": "plant",
            "subtype": "",
            "group": "Fungi",
            "alignment": "unaligned",
            "armor_class": 5,
            "armor_desc": "null",
            "hit_points": 18,
            "hit_dice": "4d8",
            "speed": {
                "walk": 5
            },
            "strength": 3,
            "dexterity": 1,
            "constitution": 10,
            "intelligence": 1,
            "wisdom": 3,
            "charisma": 1,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "blinded, deafened, frightened",
            "senses": "blindsight 30 ft. (blind beyond this radius), passive Perception 6",
            "languages": "",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Multiattack",
                    "desc": "The fungus makes 1d4 Rotting Touch attacks."
                },
                {
                    "name": "Rotting Touch",
                    "desc": "Melee Weapon Attack: +2 to hit, reach 10 ft., one creature. Hit: 4 (1d8) necrotic damage.",
                    "attack_bonus": 2,
                    "damage_dice": "1d8"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "False Appearance",
                    "desc": "While the violet fungus remains motionless, it is indistinguishable from an ordinary fungus."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "witchlight": {
            "slug": "witchlight",
            "name": "Witchlight",
            "size": "Tiny",
            "type": "construct",
            "subtype": "",
            "group": "null",
            "alignment": "neutral",
            "armor_class": 14,
            "armor_desc": "",
            "hit_points": 10,
            "hit_dice": "4d4",
            "speed": {
                "fly": 50
            },
            "strength": 1,
            "dexterity": 18,
            "constitution": 10,
            "intelligence": 10,
            "wisdom": 13,
            "charisma": 7,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 3,
            "skills": {
                "perception": 3
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "poison, radiant",
            "condition_immunities": "charmed, exhaustion, frightened, paralyzed, petrified, poisoned",
            "senses": "darkvision 60 ft., passive Perception 13",
            "languages": "understands the language of its creator but can't speak",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Light Ray",
                    "desc": "Ranged Weapon Attack: +6 to hit, range 30 ft., one target. Hit: 6 (1d4 + 4) radiant damage.",
                    "attack_bonus": 6,
                    "damage_dice": "1d4"
                },
                {
                    "name": "Flash (Recharge 5-6)",
                    "desc": "The witchlight emits a bright burst of light that blinds all sighted creatures within 30 feet for 1d4 rounds unless they succeed on a DC 10 Constitution saving throw."
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Dispel Magic Weakness",
                    "desc": "Casting dispel magic on a witchlight paralyzes it for 1d10 rounds."
                },
                {
                    "name": "Luminance",
                    "desc": "A witchlight normally glows as brightly as a torch. The creature can dim itself to the luminosity of a candle, but it cannot extinguish its light. Because of its glow, the witchlight has disadvantage on Dexterity (Stealth) checks."
                },
                {
                    "name": "Thin As Light",
                    "desc": "While a witchlight is not incorporeal, it can pass through any opening that light can."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "tob",
            "document__title": "Tome of Beasts OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "wolf": {
            "slug": "wolf",
            "name": "Wolf",
            "size": "Medium",
            "type": "beast",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 13,
            "armor_desc": "natural armor",
            "hit_points": 11,
            "hit_dice": "2d8",
            "speed": {
                "walk": 40
            },
            "strength": 12,
            "dexterity": 15,
            "constitution": 12,
            "intelligence": 3,
            "wisdom": 12,
            "charisma": 6,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": 3,
            "skills": {
                "perception": 3,
                "stealth": 4
            },
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "passive Perception 13",
            "languages": "",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Bite",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (2d4 + 2) piercing damage. If the target is a creature, it must succeed on a DC 11 Strength saving throw or be knocked prone.",
                    "attack_bonus": 4,
                    "damage_dice": "2d4",
                    "damage_bonus": 2
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Keen Hearing and Smell",
                    "desc": "The wolf has advantage on Wisdom (Perception) checks that rely on hearing or smell."
                },
                {
                    "name": "Pack Tactics",
                    "desc": "The wolf has advantage on an attack roll against a creature if at least one of the wolf's allies is within 5 ft. of the creature and the ally isn't incapacitated."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        },
        "wolpertinger": {
            "slug": "wolpertinger",
            "name": "Wolpertinger",
            "size": "Tiny",
            "type": "monstrosity",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 13,
            "armor_desc": "null",
            "hit_points": 9,
            "hit_dice": "2d4+4",
            "speed": {
                "burrow": 10,
                "fly": 30,
                "walk": 30
            },
            "strength": 6,
            "dexterity": 16,
            "constitution": 14,
            "intelligence": 5,
            "wisdom": 12,
            "charisma": 6,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "",
            "senses": "darkvision 60 ft., passive Perception 11",
            "languages": "-",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "attack_bonus": 5,
                    "damage_dice": "1d4+3",
                    "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) piercing damage.",
                    "name": "Bite"
                },
                {
                    "attack_bonus": 5,
                    "damage_dice": "1d4+3",
                    "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) piercing damage.",
                    "name": "Gore"
                },
                {
                    "desc": "The wolpertinger emits a piercing shriek. Each creature within 30 feet that can hear the wolpertinger must succeed on a DC 13 Constitution saving throw or be deafened for 1 minute. A beast with an Intelligence of 4 or lower that is in the area must also succeed on a DC 13 Wisdom saving throw or be frightened until the beginning of its next turn.",
                    "name": "Keening (Recharge 6)"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "desc": "If the wolpertinger moves at least 10 feet straight toward a target and then hits it with a gore attack on the same turn, the target takes an extra 2 (1d4) piercing damage.",
                    "name": "Charge"
                },
                {
                    "desc": "The wolpertinger doesn't provoke an opportunity attack when it flies out of an enemy's reach.",
                    "name": "Flyby"
                },
                {
                    "desc": "The wolpertinger's long jump is up to 20 feet and its high jump is up to 10 feet, with or without a running start.",
                    "name": "Standing Leap"
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "cc",
            "document__title": "Creature Codex OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "xanka": {
            "slug": "xanka",
            "name": "Xanka",
            "size": "Small",
            "type": "construct",
            "subtype": "",
            "group": "null",
            "alignment": "unaligned",
            "armor_class": 15,
            "armor_desc": "natural armor",
            "hit_points": 18,
            "hit_dice": "4d6+4",
            "speed": {
                "walk": 25,
                "climb": 15
            },
            "strength": 10,
            "dexterity": 15,
            "constitution": 12,
            "intelligence": 4,
            "wisdom": 10,
            "charisma": 7,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": "null",
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "charmed, exhaustion, frightened,",
            "senses": "blindsight 120 ft., passive Perception 10",
            "languages": "Understands the languages of its creator but can't",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Absorb",
                    "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) force damage, and the xanka regains hit points equal to the damage caused by its attack. In addition, a living creature hit by this attack must make a successful DC 12 Dexterity saving throw or suffer a gaping wound that causes 2 (1d4) necrotic damage at the end of each of the creature's turns until the wound is treated with magical healing or with a successful DC 10 Intelligence (Medicine) check. If a creature who fails this saving throw is wearing armor or using a shield, the creature can choose to prevent the necrotic damage by permanently reducing the AC of its armor or shield by 1 instead.",
                    "attack_bonus": 4,
                    "damage_dice": "1d8+2"
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Ingest Weapons",
                    "desc": "When the xanka is hit by a melee weapon and the final, adjusted attack roll is 19 or less, the weapon gains a permanent -1 penalty to damage rolls, after inflicting damage for this attack. If the penalty reaches -5, the weapon is destroyed. Even magic weapons are subject to this effect."
                },
                {
                    "name": "Magic Weapons",
                    "desc": "The xanka's weapon attacks are magical."
                },
                {
                    "name": "Constructed Nature",
                    "desc": "A xanka doesn't require air, food, drink, or sleep."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "tob",
            "document__title": "Tome of Beasts OGL",
            "document__license_url": "http://open5e.com/legal"
        },
        "zombie": {
            "slug": "zombie",
            "name": "Zombie",
            "size": "Medium",
            "type": "undead",
            "subtype": "",
            "group": "Zombies",
            "alignment": "neutral evil",
            "armor_class": 8,
            "armor_desc": "null",
            "hit_points": 22,
            "hit_dice": "3d8+9",
            "speed": {
                "walk": 20
            },
            "strength": 13,
            "dexterity": 6,
            "constitution": 16,
            "intelligence": 3,
            "wisdom": 6,
            "charisma": 5,
            "strength_save": "null",
            "dexterity_save": "null",
            "constitution_save": "null",
            "intelligence_save": "null",
            "wisdom_save": 0,
            "charisma_save": "null",
            "perception": "null",
            "skills": {},
            "damage_vulnerabilities": "",
            "damage_resistances": "",
            "damage_immunities": "",
            "condition_immunities": "poisoned",
            "senses": "darkvision 60 ft., passive Perception 8",
            "languages": "understands all languages it spoke in life but can't speak",
            "challenge_rating": "1/4",
            "actions": [
                {
                    "name": "Slam",
                    "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) bludgeoning damage.",
                    "attack_bonus": 3,
                    "damage_dice": "1d6",
                    "damage_bonus": 1
                }
            ],
            "reactions": "",
            "legendary_desc": "",
            "legendary_actions": "",
            "special_abilities": [
                {
                    "name": "Undead Fortitude",
                    "desc": "If damage reduces the zombie to 0 hit points, it must make a Constitution saving throw with a DC of 5+the damage taken, unless the damage is radiant or from a critical hit. On a success, the zombie drops to 1 hit point instead."
                }
            ],
            "spell_list": [],
            "img_main": "null",
            "document__slug": "wotc-srd",
            "document__title": "Systems Reference Document",
            "document__license_url": "http://open5e.com/legal"
        }
    },
    "1/2": {
        "ape",
        "black bear",
        "cockatrice",
        "crocodile",
        "darkmantle",
        "deep gnome",
        "dust mephit",
        "gas spore",
        "giant goat",
        "giant sea horse",
        "giant wasp",
        "gnoll",
        "gray ooze",
        "hobgoblin",
        "ice mephit",
        "jackalwere",
        "lizardfolk",
        "magma mephit",
        "magmin",
        "myconid adult",
        "orc",
        "piercer",
        "reef shark",
        "rust monster",
        "sahuagin",
        "satyr",
        "scout",
        "shadow",
        "swarm of insects",
        "thug",
        "tridrone",
        "vine blight",
        "warhorse",
        "warhorse skeleton",
        "worg"
    },
    "1": {
        "animated armor",
        "brass dragon wyrmling",
        "brown bear",
        "bugbear",
        "copper dragon wyrmling",
        "death dog",
        "dire wolf",
        "dryad",
        "duergar",
        "faerie dragon (young)",
        "fire snake",
        "ghoul",
        "giant eagle",
        "giant hyena",
        "giant octopus",
        "giant spider",
        "giant toad",
        "giant vulture",
        "goblin boss",
        "half-ogre",
        "harpy",
        "hippogriff",
        "imp",
        "kuo-toa whip",
        "lion",
        "quadrone",
        "quaggoth spore servant",
        "quasit",
        "scarecrow",
        "specter",
        "spy",
        "swarm of quippers",
        "thri-kreen",
        "tiger",
        "yuan-ti pureblood"
    },
    "2": {
        "allosaurus",
        "ankheg",
        "awakened tree",
        "azer",
        "bandit captain",
        "berserker",
        "black dragon wyrmling",
        "bronze dragon wyrmling",
        "carrion crawler",
        "centaur",
        "cult fanatic",
        "druid",
        "ettercap",
        "faerie dragon (old)",
        "gargoyle",
        "gelatinous cube",
        "ghast",
        "giant boar",
        "giant constrictor snake",
        "giant elk",
        "gibbering mouther",
        "githzerai monk",
        "gnoll pack lord",
        "green dragon wyrmling",
        "grick",
        "griffon",
        "hunter shark",
        "intellect devourer",
        "lizardfolk shaman",
        "merrow",
        "mimic",
        "minotaur skeleton",
        "myconid sovereign",
        "nothic",
        "ochre jelly",
        "ogre",
        "ogre zombie",
        "orc eye of gruumsh",
        "orog",
        "pegasus",
        "pentadrone",
        "peryton",
        "plesiosaurus",
        "polar bear",
        "poltergeist (specter)",
        "priest",
        "quaggoth",
        "rhinoceros",
        "rug of smothering",
        "saber-toothed tiger",
        "sahuagin priestess",
        "sea hag",
        "silver dragon wyrmling",
        "spined devil",
        "swarm of poisonous snakes",
        "wererat",
        "white dragon wyrmling",
        "will-o’-wisp"
    },
    "3": {
        "ankylosaurus",
        "basilisk",
        "bearded devil",
        "blue dragon wyrmling",
        "bugbear chief",
        "displacer beast",
        "doppelganger",
        "giant scorpion",
        "githyanki warrior",
        "gold dragon wyrmling",
        "green hag",
        "grell",
        "hell hound",
        "hobgoblin captain",
        "hook horror",
        "killer whale",
        "knight",
        "kuo-toa monitor",
        "manticore",
        "minotaur",
        "mummy",
        "nightmare",
        "owlbear",
        "phase spider",
        "quaggoth thonot",
        "spectator",
        "veteran",
        "water weird",
        "werewolf",
        "wight",
        "winter wolf",
        "yeti",
        "yuan-ti malison"
    },
    "4": {
        "banshee",
        "black pudding",
        "bone naga",
        "chuul",
        "couatl",
        "elephant",
        "ettin",
        "flameskull",
        "ghost",
        "gnoll fang of yeenoghu",
        "helmed horror",
        "incubus",
        "lamia",
        "lizard king/queen",
        "orc war chief",
        "red dragon wyrmling",
        "sea hag (in coven)",
        "shadow demon",
        "succubus",
        "wereboar",
        "weretiger"
    },
    "5": {
        "air elemental",
        "barbed devil",
        "barlgura",
        "beholder zombie",
        "bulette",
        "cambion",
        "drow elite warrior",
        "earth elemental",
        "fire elemental",
        "flesh golem",
        "giant crocodile",
        "giant shark",
        "gladiator",
        "gorgon",
        "green hag (in coven)",
        "half-red dragon veteran",
        "hill giant",
        "mezzoloth",
        "night hag",
        "otyugh",
        "red slaad",
        "revenant",
        "roper",
        "sahuagin baron",
        "salamander",
        "shambling mound",
        "triceratops",
        "troll",
        "umber hulk",
        "unicorn",
        "vampire spawn",
        "water elemental",
        "werebear",
        "wraith",
        "xorn",
        "young remorhaz"
    },
    "6": {
        "chasme",
        "chimera",
        "cyclops",
        "drider",
        "galeb duhr",
        "githzerai zerth",
        "hobgoblin warlord",
        "invisible stalker",
        "kuo-toa archpriest",
        "mage",
        "mammoth",
        "medusa",
        "vrock",
        "wyvern",
        "young brass dragon",
        "young white dragon"
    },
    "7": {
        "blue slaad",
        "drow mage",
        "giant ape",
        "grick alpha",
        "mind flayer",
        "night hag (in coven)",
        "oni",
        "shield guardian",
        "stone giant",
        "young black dragon",
        "young copper dragon",
        "yuan-ti abomination"
    },
    "8": {
        "assassin",
        "chain devil",
        "cloaker",
        "drow priestess of lolth",
        "fomorian",
        "frost giant",
        "githyanki knight",
        "green slaad",
        "hezrou",
        "hydra",
        "mind flayer arcanist",
        "spirit naga",
        "tyrannosaurus rex",
        "young bronze dragon",
        "young green dragon"
    },
    "9": {
        "abominable yeti",
        "bone devil",
        "clay golem",
        "cloud giant",
        "fire giant",
        "glabrezu",
        "gray slaad",
        "nycaloth",
        "treant",
        "young blue dragon",
        "young silver dragon"
    },
    "10": {
        "aboleth",
        "death slaad",
        "deva",
        "guardian naga",
        "stone golem",
        "yochlol",
        "young gold dragon",
        "young red dragon"
    },
    "11": {
        "behir",
        "dao",
        "djinni",
        "efreeti",
        "gynosphinx",
        "horned devil",
        "marid",
        "remorhaz",
        "roc"
    },
    "12": {
        "arcanaloth",
        "archmage",
        "erinyes"
    },
    "13": {
        "adult brass dragon",
        "adult white dragon",
        "beholder (not in lair)",
        "nalfeshnee",
        "rakshasa",
        "storm giant",
        "ultroloth",
        "vampire",
        "young red shadow dragon"
    },
    "14": {
        "adult black dragon",
        "adult copper dragon",
        "beholder (in lair)",
        "death tyrant (not in lair)",
        "ice devil"
    },
    "15": {
        "adult bronze dragon",
        "adult green dragon",
        "death tyrant (in lair)",
        "mummy lord (not in lair)",
        "purple worm",
        "vampire (spellcaster)",
        "vampire (warrior)"
    },
    "16": {
        "adult blue dragon",
        "adult silver dragon",
        "iron golem",
        "marilith",
        "mummy lord (in lair)",
        "planetar"
    },
    "17": {
        "adult blue dracolich",
        "adult gold dragon",
        "adult red dragon",
        "androsphinx",
        "death knight",
        "dragon turtle",
        "goristro"
    },
    "18": {
        "demilich (not in lair)",
    },
    "19": {
        "balor"
    },
    "20": {
        "ancient brass dragon",
        "ancient white dragon",
        "demilich (in lair)",
        "pit fiend"
    },
    "21": {
        "ancient black dragon",
        "ancient copper dragon",
        "lich (not in lair)",
        "solar"
    },
    "22": {
        "ancient bronze dragon",
        "ancient green dragon",
        "lich (in lair)"
    },
    "23": {
        "ancient blue dragon",
        "ancient silver dragon",
        "empyrean",
        "kraken"
    },
    "24": {
        "ancient gold dragon",
        "ancient red dragon"
    },
    "30": {
        "tarrasque"
    }
}
