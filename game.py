from deck import Deck
from hand import Hand
from messages import Messages


class Game:
    MINIMUM_BET = 1
    STARTING_CARDS = 2
    HIT = 1
    BLACKJACK = 21
    BONUS_MULT = 1.5
    MINIMUM_DEALER_CARD_VALUE = 17

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.messages = Messages(player, dealer, self.BONUS_MULT)

    def starting_settings(self):
        self.deck = Deck()
        self.end_game = False
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.bet = None

    def ask_player_to_bet(self):
        while True:
            self.bet = input("Place your bet: ")
            try:
                self.bet = float(self.bet)
                if self.bet < self.MINIMUM_BET:
                    self.messages.print_minimum_bet(self.MINIMUM_BET)
                    continue
                if self.bet > self.player.balance:
                    self.messages.print_not_enough_funds()
                    continue
                break
            except:
                self.messages.print_not_valid()
                print()
                continue

    def hit_or_stay_stage(self, player_hand, dealer_hand):
        while True:
            stay_hit = input("Would you like to hit or stay? ")

            if stay_hit.lower() in ['hit', 'h']:
                self.player.get_hit(self.deck, player_hand, self.HIT)

                if player_hand.cards_value > self.BLACKJACK:
                    self.messages.print_player_hand_is_over_21()
                    self.player.update_balance_lose(self.bet)
                    self.end_game = True
                    break

                continue

            if stay_hit.lower() in ['stay', 's']:
                self.messages.print_dealer_hand(dealer_hand)

                if dealer_hand.cards_value == self.BLACKJACK:
                    self.messages.print_dealer_hits_blackjack()
                    self.player.update_balance_lose(self.bet)
                    self.end_game = True
                    break

                while dealer_hand.cards_value < self.MINIMUM_DEALER_CARD_VALUE and dealer_hand.cards_value < self.BLACKJACK:
                    self.dealer.get_hit(self.deck, dealer_hand, self.HIT)

                break

            else:
                self.messages.print_not_valid()

    def determine_winner(self, player_hand, dealer_hand):
        if dealer_hand.cards_value > self.BLACKJACK:
            self.messages.print_dealer_busts()
            self.player.update_balance_win(self.bet)

        elif self.end_game == False:
            if dealer_hand.cards_value <= self.BLACKJACK:
                self.messages.print_dealer_stays()

                if player_hand.cards_value == dealer_hand.cards_value:
                    self.messages.print_both_tie()
                elif player_hand.cards_value < dealer_hand.cards_value:
                    self.messages.print_dealer_wins()
                    self.player.update_balance_lose(self.bet)
                else:
                    self.messages.print_player_wins()
                    self.player.update_balance_win(self.bet)

    def start_game(self):
        while True:

            starting_question = input(
                f"\nYou are starting with ${self.player.balance}. Would you like to play a hand? (yes/no): ")

            if starting_question.lower() in ['yes', 'y']:

                self.starting_settings()
                self.ask_player_to_bet()
                self.messages.update_bet_info(self.bet)

                self.player.get_starting_hand(
                    self.deck, self.player_hand, self.STARTING_CARDS)

                self.dealer.get_starting_hand(
                    self.deck, self.dealer_hand, self.STARTING_CARDS)

                if self.player_hand.cards_value == self.BLACKJACK:
                    if self.dealer_hand.cards_value == self.BLACKJACK:
                        self.messages.print_both_players_hit_blackjack(
                            self.dealer_hand)
                        continue

                    else:
                        self.messages.print_player_hits_blackjack(
                            self.dealer_hand)
                        self.player.update_balance_win(
                            self.bet * self.BONUS_MULT)
                        continue

                self.hit_or_stay_stage(self.player_hand, self.dealer_hand)
                self.determine_winner(self.player_hand, self.dealer_hand)

                if self.player.balance == 0:
                    self.messages.print_player_has_no_money()
                    quit()

            elif starting_question.lower() in ['no', 'n']:
                self.messages.print_bye()
                quit()

            else:
                self.messages.print_not_valid()
