from app.game import Game
from app.object.player import Player
from app.object.deck import Deck


deck_one = Deck.generate([0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 8])
deck_two = Deck.generate([0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 8])
player_one = Player(20)
player_one.add_deck(deck_one)
player_one.shuffle_deck()
player_two = Player(20)
player_two.add_deck(deck_two)
player_two.shuffle_deck()
game = Game(player_one, player_two)
winner = game.play_game() + 1
print(winner)
