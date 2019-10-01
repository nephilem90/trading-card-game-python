import unittest
from app.game import Game
from unittest.mock import MagicMock


class GameTest(unittest.TestCase):
    def test_game_has_two_player(self):
        player_one = MagicMock(name='p1')
        player_two = MagicMock(name='p2')
        game = Game(player_one, player_two)
        self.assertEqual([player_one, player_two], game.get_players())

    def test_players_start_with_twenty_life_point(self):
        player_one = MagicMock(name='p1')
        player_two = MagicMock(name='p2')
        game = Game(player_one, player_two)
        self.assertEqual(game.get_players(), [player_one, player_two])

    def test_player_add_one_mana_in_tourn(self):
        player_one = MagicMock(name='p1')
        player_two = MagicMock(name='p2')
        game = Game(player_one, player_two)
        game.play_turn()
        game.get_players()[0].add_mana.assert_called_once_with(1)

    def test_player_get_damage_if_can_not_pick_card(self):
        player_one = MagicMock(name='p1')
        player_two = MagicMock(name='p2')
        player_one.draw_card.return_value = False
        game = Game(player_one, player_two)
        game.play_turn()
        game.get_players()[0].receive_damage.assert_called_once_with(1)

    def test_player_play_card(self):
        player_one = MagicMock(name='p1')
        player_two = MagicMock(name='p2')
        player_one.draw_card.return_value = True
        game = Game(player_one, player_two)
        game.play_turn()
        game.get_players()[0].play_cards.assert_called_once_with()


if __name__ == '__main__':
    unittest.main()
