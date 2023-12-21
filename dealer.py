class Dealer:

    def get_starting_hand(self, deck, hand, num_cards):
        self._get_draw(deck, hand, num_cards)
        print(
            f"The dealer is dealt: {hand.first_card}, Unknown")

    def get_hit(self, deck, hand, num_cards):
        self._get_draw(deck, hand, num_cards)
        print(
            f"The dealer hits and is dealt: {hand.last_card}\nThe dealer has: {hand}")

    def _get_draw(self, deck, hand, num_cards):
        dealer_starting_hand = deck.deal(num_cards)
        hand.add_to_hand(dealer_starting_hand)
