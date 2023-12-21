from player import Player
from dealer import Dealer
from game import Game


def main():
    STARTING_BALANCE = 500

    player = Player(STARTING_BALANCE)
    dealer = Dealer()
    game = Game(player, dealer)

    print("\nWelcome to Blackjack!")
    game.start_game()


if __name__ == '__main__':
    main()
