from classes import SlotMachine, Emoji

slot_machines = {
    "classic": SlotMachine(name="classic", cost=3, rows=3, reels=3, emojis=[
            Emoji(emoji="<:bar:740998677979725864>", rank=0, weights=[4.347826086, 4.347826086, 4.347826086]),
            Emoji(emoji=":seven:", rank=1, weights=[13.04347826, 4.347826086, 4.347826086]),
            Emoji(emoji="🍒", rank=2, weights=[17.39130435, 13.04347826, 13.04347826]),
            Emoji(emoji="🍊", rank=3, weights=[21.73913044, 26.08695652, 26.08695652]),
            Emoji(emoji="🍌", rank=4, weights=[21.73913044, 26.08695652, 26.08695652]),
            Emoji(emoji="🍋", rank=5, weights=[21.73913044, 26.08695652, 26.08695652])
        ]
    ),
    "c": SlotMachine(name="c", cost=3, rows=1, reels=3, emojis=[
            Emoji(emoji="<:bar:740998677979725864>", rank=0, weights=[4.347826086, 4.347826086, 4.347826086]),
            Emoji(emoji=":seven:", rank=1, weights=[13.04347826, 4.347826086, 4.347826086]),
            Emoji(emoji="🍒", rank=2, weights=[17.39130435, 13.04347826, 13.04347826]),
            Emoji(emoji="🍊", rank=3, weights=[21.73913044, 26.08695652, 26.08695652]),
            Emoji(emoji="🍌", rank=4, weights=[21.73913044, 26.08695652, 26.08695652]),
            Emoji(emoji="🍋", rank=5, weights=[21.73913044, 26.08695652, 26.08695652])
        ]
    ),
    "fruits": SlotMachine(name="fruits", cost=3, rows=3, reels=3, emojis=[
            Emoji(emoji="🍎", rank=0, weights=2.22),
            Emoji(emoji="🍊", rank=1, weights=5.31),
            Emoji(emoji="🍐", rank=2, weights=7.94),
            Emoji(emoji="🍋", rank=3, weights=17.1),
            Emoji(emoji="🍉", rank=4, weights=41.21),
            Emoji(emoji="[B]", rank=5, weights=26.215)
        ]
    ),
    "animals": SlotMachine(name="animals", cost=3, rows=3, reels=3, emojis=[
            Emoji(emoji="🐫", rank=0, weights=2.22),
            Emoji(emoji="🐧", rank=1, weights=5.31),
            Emoji(emoji="🐠", rank=2, weights=7.94),
            Emoji(emoji="🐍", rank=3, weights=17.1),
            Emoji(emoji="🐢", rank=4, weights=41.21),
            Emoji(emoji="[B]", rank=5, weights=26.215)
        ]
    ),
    "cats": SlotMachine(name="cats", cost=3, rows=3, reels=3, emojis=[
            Emoji(emoji="😺", rank=0, weights=2.22),
            Emoji(emoji="😸", rank=1, weights=5.31),
            Emoji(emoji="😹", rank=2, weights=7.94),
            Emoji(emoji="😻", rank=3, weights=17.1),
            Emoji(emoji="😼", rank=4, weights=41.21),
            Emoji(emoji="[B]", rank=5, weights=26.215)
        ]
    ),
    "moons": SlotMachine(name="moons", cost=3, rows=3, reels=3, emojis=[
            Emoji(emoji="🌗", rank=0, weights=2.22),
            Emoji(emoji="🌘", rank=1, weights=5.31),
            Emoji(emoji="🌑", rank=2, weights=7.94),
            Emoji(emoji="🌒", rank=3, weights=17.1),
            Emoji(emoji="🌔", rank=4, weights=41.21),
            Emoji(emoji="[B]", rank=5, weights=26.215)
        ]
    ),
    "hearts": SlotMachine(name="hearts", cost=3, rows=3, reels=5, emojis=[
            Emoji(emoji="❤", rank=0, weights=[4.347826086, 4.347826086, 4.347826086, 4.347826086, 4.347826086]),
            Emoji(emoji="💛", rank=1, weights=[13.04347826, 4.347826086, 4.347826086, 4.347826086, 4.347826086]),
            Emoji(emoji="💚", rank=2, weights=[17.39130435, 13.04347826, 13.04347826, 13.04347826, 13.04347826]),
            Emoji(emoji="💙", rank=3, weights=[21.73913044, 26.08695652, 26.08695652, 26.08695652, 26.08695652]),
            Emoji(emoji="💜", rank=4, weights=[21.73913044, 26.08695652, 26.08695652, 26.08695652, 26.08695652]),
            Emoji(emoji="<:bar:740998677979725864>", rank=5,
                  weights=[21.73913044, 26.08695652, 26.08695652, 26.08695652, 26.08695652])
        ]
    ),
    "osrs": SlotMachine(name="osrs", cost=3, rows=3, reels=3, emojis=[
            Emoji(emoji="🧙‍", rank=0, weights=2.22),
            Emoji(emoji="🦹", rank=1, weights=5.31),
            Emoji(emoji="🦸", rank=2, weights=7.94),
            Emoji(emoji="🧛", rank=3, weights=17.1),
            Emoji(emoji="🧜", rank=4, weights=41.21),
            Emoji(emoji="[B]", rank=5, weights=26.215)
        ]
    )
}
