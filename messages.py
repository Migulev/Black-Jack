class Messages:

    def __init__(self, player, dealer, bonus):
        self.player = player
        self.dealer = dealer
        self.bet = None
        self.bonus = bonus

    def update_bet_info(self, bet):
        self.bet = bet

    def print_both_players_hit_blackjack(self, dealer_hand):
        print(
            f"The dealer has dealt: {dealer_hand}\nTou tie. Both players have Blackjack! WOW! \nYour bet has been returned.")

    def print_player_hits_blackjack(self, dealer_hand):
        print(
            f"The dealer has dealt: {dealer_hand}\nBlackjack! You win ${self.bet * self.bonus} :)")

    def print_dealer_hits_blackjack(self):
        print(
            f"The dealer has Blackjack! You lose {self.bet} :(")

    def print_dealer_busts(self):
        print(f"The dealer busts, you win ${self.bet} :)")

    def print_dealer_stays(self):
        print("The dealer stays.")

    def print_both_tie(self):
        print("You tie. Your bet has been returned.")

    def print_dealer_wins(self):
        print(f"The dealer wins, you lose ${self.bet} :(")

    def print_player_wins(self):
        print(f"You win ${self.bet}!")

    def print_player_has_no_money(self):
        print(
            "You've ran out of money. Please restart this program to try again. Goodbye.\n")

    def print_bye(self):
        print(
            f"So pity that you are leaving the game.\nYour balance is ${self.player.balance}.\nBYE BYE!\n")

    def print_minimum_bet(self):
        print(f"The minimum bet is ${self.bet}.")

    def print_not_valid(self):
        print("This is not a valid option.")

    def print_dealer_hand(self, dealer_hand):
        print(f"The dealer has: {dealer_hand}")

    def print_player_hand_is_over_21(self):
        print(
            f"Your hand value is over 21 and you lose ${self.bet} :(")

    def print_not_enough_funds(self):
        print("You do not have sufficient funds.")
