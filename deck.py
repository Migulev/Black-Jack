from random import shuffle
from card import Card


class Deck:
    def __init__(self):
        self.cards = []
        self._create_deck()
        self._shuffle()

    def _create_deck(self):
        for value_name in Card.VALUE_NAMES:
            for suit_symbol in Card.SUIT_SYMBOLS:
                card = Card(value_name, suit_symbol)
                self.cards.append(card)
        return self.cards

    def _shuffle(self):
        shuffle(self.cards)

    def deal(self, num_cards):
        cards_to_deal = []
        for _ in range(num_cards):
            cards_to_deal.append(self.cards.pop())
        return cards_to_deal
