from classes import SlotMachine, Emoji

slot_machines = {
    "classic": SlotMachine(
        name="classic",
        cost=3,
        rows=3,
        reels=3,
        machine_type="slot",
        play_count=63,
        winnings=321,
        profit=-132, 
        emojis=[
            Emoji(emoji=u'<:bar:740308928398622822>', rank=0, weights=[4.347826086, 4.347826086, 4.347826086]),
            Emoji(emoji=u'<:SlotmachineSeven:743190741920251994>', rank=1, weights=[13.04347826, 4.347826086, 4.347826086]),
            Emoji(emoji=u'\U0001f352', rank=2, weights=[17.39130435, 13.04347826, 13.04347826]),
            Emoji(emoji=u'\U0001f34a', rank=3, weights=[21.73913044, 26.08695652, 26.08695652]),
            Emoji(emoji=u'\U0001f34c', rank=4, weights=[21.73913044, 26.08695652, 26.08695652]),
            Emoji(emoji=u'\U0001f349', rank=5, weights=[21.73913044, 26.08695652, 26.08695652])
        ]
    ),
    "c": SlotMachine(
        name="c",
        cost=3,
        rows=1,
        reels=3,
        machine_type="slot",
        play_count=0,
        winnings=0,
        profit=0, 
        emojis=[
            Emoji(emoji=u'<:bar:740998677979725864>', rank=0, weights=[4.347826086, 4.347826086, 4.347826086]),
            Emoji(emoji=u':seven:', rank=1, weights=[13.04347826, 4.347826086, 4.347826086]),
            Emoji(emoji=u'\U0001f352', rank=2, weights=[17.39130435, 13.04347826, 13.04347826]),
            Emoji(emoji=u'\U0001f34a', rank=3, weights=[21.73913044, 26.08695652, 26.08695652]),
            Emoji(emoji=u'\U0001f34c', rank=4, weights=[21.73913044, 26.08695652, 26.08695652]),
            Emoji(emoji=u'\U0001f34b', rank=5, weights=[21.73913044, 26.08695652, 26.08695652])
        ]
    ),
    "fruits": SlotMachine(
        name="fruits",
        cost=3,
        rows=3,
        reels=3,
        machine_type="slot",
        play_count=0,
        winnings=0,
        profit=0, 
        emojis=[
            Emoji(emoji=u'\U0001f34e', rank=0, weights=[2.22]),
            Emoji(emoji=u'\U0001f34a', rank=1, weights=[5.31]),
            Emoji(emoji=u'\U0001f350', rank=2, weights=[7.94]),
            Emoji(emoji=u'\U0001f34b', rank=3, weights=[17.1]),
            Emoji(emoji=u'\U0001f349', rank=4, weights=[41.21]),
            Emoji(emoji=u'[B]', rank=5, weights=[26.215])
        ]
    ),
    "animals": SlotMachine(
        name="animals",
        cost=3,
        rows=3,
        reels=3,
        machine_type="slot",
        play_count=0,
        winnings=0,
        profit=0, 
        emojis=[
            Emoji(emoji=u'\U0001f42b', rank=0, weights=[2.22]),
            Emoji(emoji=u'\U0001f427', rank=1, weights=[5.31]),
            Emoji(emoji=u'\U0001f420', rank=2, weights=[7.94]),
            Emoji(emoji=u'\U0001f40d', rank=3, weights=[17.1]),
            Emoji(emoji=u'\U0001f422', rank=4, weights=[41.21]),
            Emoji(emoji=u'[B]', rank=5, weights=[26.215])
        ]
    ),
    "cats": SlotMachine(
        name="cats",
        cost=3,
        rows=3,
        reels=3,
        machine_type="slot",
        play_count=0,
        winnings=0,
        profit=0, 
        emojis=[
            Emoji(emoji=u'\U0001f63a', rank=0, weights=[2.22]),
            Emoji(emoji=u'\U0001f638', rank=1, weights=[5.31]),
            Emoji(emoji=u'\U0001f639', rank=2, weights=[7.94]),
            Emoji(emoji=u'\U0001f63b', rank=3, weights=[17.1]),
            Emoji(emoji=u'\U0001f63c', rank=4, weights=[41.21]),
            Emoji(emoji=u'[B]', rank=5, weights=[26.215])
        ]
    ),
    "moons": SlotMachine(
        name="moons",
        cost=3,
        rows=3,
        reels=3,
        machine_type="slot",
        play_count=0,
        winnings=0,
        profit=0, 
        emojis=[
            Emoji(emoji=u'\U0001f317', rank=0, weights=[2.22]),
            Emoji(emoji=u'\U0001f318', rank=1, weights=[5.31]),
            Emoji(emoji=u'\U0001f311', rank=2, weights=[7.94]),
            Emoji(emoji=u'\U0001f312', rank=3, weights=[17.1]),
            Emoji(emoji=u'\U0001f314', rank=4, weights=[41.21]),
            Emoji(emoji=u'[B]', rank=5, weights=[26.215])
        ]
    ),
    "hearts": SlotMachine(
        name="hearts",
        cost=3,
        rows=3,
        reels=5,
        machine_type="slot",
        play_count=0,
        winnings=0,
        profit=0, 
        emojis=[
            Emoji(emoji=u'\u2764', rank=0, weights=[4.347826086, 4.347826086, 4.347826086, 4.347826086, 4.347826086]),
            Emoji(emoji=u'\U0001f49b', rank=1, weights=[13.04347826, 4.347826086, 4.347826086, 4.347826086, 4.347826086]),
            Emoji(emoji=u'\U0001f49a', rank=2, weights=[17.39130435, 13.04347826, 13.04347826, 13.04347826, 13.04347826]),
            Emoji(emoji=u'\U0001f499', rank=3, weights=[21.73913044, 26.08695652, 26.08695652, 26.08695652, 26.08695652]),
            Emoji(emoji=u'\U0001f49c', rank=4, weights=[21.73913044, 26.08695652, 26.08695652, 26.08695652, 26.08695652]),
            Emoji(emoji=u'<:bar:740998677979725864>', rank=5, weights=[21.73913044, 26.08695652, 26.08695652, 26.08695652, 26.08695652])
        ]
    ),
    "osrs": SlotMachine(
        name="osrs",
        cost=3,
        rows=3,
        reels=3,
        machine_type="slot",
        play_count=0,
        winnings=0,
        profit=0, 
        emojis=[
            Emoji(emoji=u'\u200d', rank=0, weights=[2.22]),
            Emoji(emoji=u'\U0001f9b9', rank=1, weights=[5.31]),
            Emoji(emoji=u'\U0001f9b8', rank=2, weights=[7.94]),
            Emoji(emoji=u'\U0001f9db', rank=3, weights=[17.1]),
            Emoji(emoji=u'\U0001f9dc', rank=4, weights=[41.21]),
            Emoji(emoji=u'[B]', rank=5, weights=[26.215])
        ]
    )
}