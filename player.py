class Player:

    def __init__(self, balance):
        self.balance = balance

    def get_starting_hand(self, deck, hand, num_cards):
        self._get_draw(deck, hand, num_cards)
        print(f"You are dealt: {hand}")

    def get_hit(self, deck, hand, num_cards):
        self._get_draw(deck, hand, num_cards)
        print(
            f"You are dealt: {hand.last_card}\nYou now have: {hand}")

    def _get_draw(self, deck, hand, num_cards):
        player_draw_card = deck.deal(num_cards)
        hand.add_to_hand(player_draw_card)

    def update_balance_lose(self, bet):
        self.balance -= bet

    def update_balance_win(self, bet):
        self.balance += bet
