class Hand:

    BLACKJACK = 21

    CARD_VALUE = {
        "A": 11,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 10,
        "Q": 10,
        "K": 10
    }

    def __init__(self):
        self.cards = []
        self.cards_value = 0
        self.ace_count = 0
        self.last_card = None
        self.first_card = None

    def _update_cards_value(self, num_cards):
        for card in self.cards[-num_cards:]:
            if str(card)[0] == "A":
                self.ace_count += 1

            self.cards_value += Hand.CARD_VALUE[str(card)[0]]

            if self.cards_value > self.BLACKJACK and self.ace_count > 0:
                self.cards_value -= 10
                self.ace_count -= 1

        return self.cards_value

    def add_to_hand(self, cards):
        self.cards.extend(cards)
        self.last_card = self.cards[-1]
        self.first_card = self.cards[0]
        self._update_cards_value(len(cards))

    def __str__(self):
        result = ''
        for card in self.cards:
            result += str(card) + ', '
        return result[:-2]
