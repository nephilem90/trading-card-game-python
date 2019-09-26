import unittest
from app.game import Game
from unittest.mock import MagicMock


class GameTest(unittest.TestCase):
    def test_game_has_two_player(self):
        player_one = MagicMock(name='p1')
        player_two = MagicMock(name='p2')
        game = Game(player_one, player_two)
        self.assertEqual([player_one, player_two], game.get_players())


if __name__ == '__main__':
    unittest.main()
