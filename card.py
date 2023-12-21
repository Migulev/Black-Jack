class Card:
    SUIT_SYMBOLS = [
        u"\u2666",  # diamonds
        u"\u2665",  # hearts
        u"\u2663",  # clubs
        u"\u2660"  # spades
    ]

    VALUE_NAMES = [
        "A",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "T",
        "J",
        "Q",
        "K"
    ]


    def __init__(self, value_name, suit):
        self.value_name = value_name
        self.suit = suit


    def __str__(self):
        return str(f"{self.value_name}{self.suit}")
