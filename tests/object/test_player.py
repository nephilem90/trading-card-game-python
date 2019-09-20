import unittest
from app.object.player import Player
from unittest.mock import MagicMock


class TestPlayer(unittest.TestCase):
    def test_damage(self):
        player = Player(20, None)
        self.assertFalse(player.receive_damage(5).is_defeat())

    def test_damage_with_not_life_point(self):
        player = Player(None, None)
        self.assertTrue(player.receive_damage(1).is_defeat())

    def test_draw_card_from_deck(self):
        deck = MagicMock(name='Deck')
        deck.pick = MagicMock(name='pick')
        player = Player(None, deck)
        player.draw_card()
        deck.pick.assert_called_once_with()
    # todo test 1 damage if when call draw deck have no card
    # todo test play card
    # todo


if __name__ == '__main__':
    unittest.main()
