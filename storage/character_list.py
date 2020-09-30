from classes import Character, Attributes, Class

character_list = {
    228716653318373376:
        Character(
            user_id=228716653318373376,
            char_name="Vol",
            class_type=Class(
                name="fighter",
                desc="### Fighting Style \n \nYou adopt a particular style of fighting as your specialty. Choose one of the "
                     "following options. You can't take a Fighting Style option more than once, even if you later get to choose "
                     "again. \n \n "
                     "#### Archery \n \n"
                     "You gain a +2 bonus to attack rolls you make with ranged weapons. \n \n"
                     "#### Defense \n \n"
                     "While you are wearing armor, you gain a +1 bonus to AC. \n \n"
                     "#### Dueling \n \n"
                     "When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with "
                     "that weapon. \n \n "
                     "#### Great Weapon Fighting \n \n"
                     "When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon that you are wielding with two "
                     "hands, you can reroll the die and must use the new roll, even if the new roll is a 1 or a 2. The weapon must "
                     "have the two-handed or versatile property for you to gain this benefit. \n \n "
                     "#### Protection \n \n"
                     "When a creature you can see attacks a target other than you that is within 5 feet of you, you can use your "
                     "reaction to impose disadvantage on the attack roll. You must be wielding a shield. \n \n "
                     "#### Two-Weapon Fighting \n \n"
                     "When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack. \n "
                     "\n "
                     "### Second Wind \n \n"
                     "You have a limited well of stamina that you can draw on to protect yourself from harm. On your turn, you can use "
                     "a bonus action to regain hit points equal to 1d10 + your fighter level. Once you use this feature, "
                     "you must finish a short or long rest before you can use it again. \n \n "
                     "### Action Surge \n \n"
                     "Starting at 2nd level, you can push yourself beyond your normal limits for a moment. On your turn, you can take "
                     "one additional action on top of your regular action and a possible bonus action. \n \n "
                     "Once you use this feature, you must finish a short or long rest before you can use it again. Starting at 17th "
                     "level, you can use it twice before a rest, but only once on the same turn. \n \n "
                     "### Martial Archetype \n \n"
                     "At 3rd level, you choose an archetype that you strive to emulate in your combat styles and techniques. Choose "
                     "Champion, Battle Master, or Eldritch Knight, all detailed at the end of the class description. The archetype you "
                     "choose grants you features at 3rd level and again at 7th, 10th, 15th, and 18th level. \n \n "
                     "### Ability Score Improvement \n \n"
                     "When you reach 4th level, and again at 6th, 8th, 12th, 14th, 16th, and 19th level, you can increase one ability "
                     "score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, "
                     "you can't increase an ability score above 20 using this feature. \n \n "
                     "### Extra Attack \n \n"
                     "Beginning at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn. "
                     "\n \n "
                     "The number of attacks increases to three when you reach 11th level in this class and to four when you reach 20th "
                     "level in this class. \n \n "
                     "### Indomitable \n \n"
                     "Beginning at 9th level, you can reroll a saving throw that you fail. If you do so, you must use the new roll, "
                     "and you can't use this feature again until you finish a long rest. \n \n "
                     "You can use this feature twice between long rests starting at 13th level and three times between long rests "
                     "starting at 17th level.\n \n "
                     "### Martial Archetypes \n \n"
                     "Different fighters choose different approaches to perfecting their fighting prowess. The martial archetype you "
                     "choose to emulate reflects your approach.",
                hit_dice="1d10",
                prof_armor="All armor, shields",
                prof_weapons="Simple weapons, martial weapons",
                prof_tools="None",
                prof_saving_throws="Strength, Constitution",
                prof_skills="Choose two skills from Acrobatics, Animal, Handling, Athletics, History, Insight, Intimidation, "
                            "Perception, and Survival",
                equipment="You start with the following equipment, in addition to the equipment granted by your background: \n \n"
                          "* (*a*) chain mail or (*b*) leather armor, longbow, and 20 arrows \n"
                          "* (*a*) a martial weapon and a shield or (*b*) two martial weapons \n"
                          "* (*a*) a light crossbow and 20 bolts or (*b*) two handaxes \n"
                          "* (*a*) a dungeoneer's pack or (*b*) an explorer's pack",
                table="| Level | Proficiency Bonus | Features                                          | \n"
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
                spellcasting_ability="",
                subtypes_name="Martial Archetypes",
                archetypes={
                    "champion": {
                        "name": "Champion",
                        "slug": "champion",
                        "desc": "The archetypal Champion focuses on the development of raw physical power honed to deadly "
                                "perfection. Those who model themselves on this archetype combine rigorous training with physical "
                                "excellence to deal devastating blows. \n \n "
                                "##### Improved Critical \n \n"
                                "Beginning when you choose this archetype at 3rd level, your weapon attacks score a critical hit "
                                "on a roll of 19 or 20. \n \n "
                                "##### Remarkable Athlete \n \n"
                                "Starting at 7th level, you can add half your proficiency bonus (round up) to any Strength, "
                                "Dexterity, or Constitution check you make that doesn't already use your proficiency bonus. \n \n "
                                "In addition, when you make a running long jump, the distance you can cover increases by a number "
                                "of feet equal to your Strength modifier. \n \n "
                                "##### Additional Fighting Style \n \n"
                                "At 10th level, you can choose a second option from the Fighting Style class feature. \n \n"
                                "##### Superior Critical \n \n"
                                "Starting at 15th level, your weapon attacks score a critical hit on a roll of 18-20. \n \n"
                                "##### Survivor \n \n"
                                "At 18th level, you attain the pinnacle of resilience in battle. At the start of each of your "
                                "turns, you regain hit points equal to 5 + your Constitution modifier if you have no more than "
                                "half of your hit points left. You don't gain this benefit if you have 0 hit points."
                    }
                }
            ),
            level=1,
            background="soldier",
            alignment="chaotic good",
            race="human",
            exp=0,
            proficiencies=["athletics", "acrobatics", "animal handling"],
            attributes=Attributes(
                strength=10,
                dexterity=12,
                constitution=14,
                intelligence=16,
                wisdom=18,
                charisma=8
            )
        )
}
