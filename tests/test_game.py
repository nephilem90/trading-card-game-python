import unittest
from app.game import Game
from unittest.mock import MagicMock
import random


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
        player_one.play_cards.assert_called_once_with()

    def test_if_player_has_no_lv_is_defeat(self):
        player_one = MagicMock(name='p1')
        player_two = MagicMock(name='p2')
        player_one.get_life_point.return_value = 0
        game = Game(player_one, player_two)
        self.assertFalse(game.play_turn())

    def test_player_defeat_if_has_one_lv_but_no_card(self):
        player_one = MagicMock(name='p1')
        player_two = MagicMock(name='p2')
        player_one.get_life_point.side_effect = [1, 0]
        player_one.draw_card.return_value = False
        game = Game(player_one, player_two)
        is_defeat = game.play_turn()
        player_one.get_life_point.assert_called_with()
        player_one.draw_card.assert_called_once_with()
        player_one.add_mana.assert_called_once_with(1)
        self.assertFalse(is_defeat)

    def test_second_player_get_damage(self):
        player_one = MagicMock(name='p1')
        player_two = MagicMock(name='p2')
        player_one.get_life_point.side_effect = [2, 1]
        player_one.draw_card.return_value = True
        damage = random.randint(1111, 9999)
        player_one.play_cards.return_value = damage
        game = Game(player_one, player_two)
        is_defeat = game.play_turn()
        player_two.receive_damage.assert_called_once_with(damage)
        self.assertTrue(is_defeat)

    def test_play_game(self):
        player_one = MagicMock(name='p1')
        player_two = MagicMock(name='p2')
        game = Game(player_one, player_two)
        player_one.get_life_point.return_value = 0
        self.assertEqual(0, game.play_game())

if __name__ == '__main__':
    unittest.main()
