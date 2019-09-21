import unittest
from app.object.player import Player
from unittest.mock import MagicMock
import random


class TestPlayer(unittest.TestCase):
    def test_get_life_point(self):
        life_point = random.randint(1111, 9999)
        player = Player(life_point, None)
        self.assertEqual(life_point, player.get_life_point())

    def test_damage(self):
        player = Player(20, None)
        self.assertEqual(15, player.receive_damage(5).get_life_point())

    def add_mana(self):
        player = Player(None, None)
        player.add_mana(1)
        self.assertEqual(1, player.get_mana())

    def test_draw_card_from_deck(self):
        deck = MagicMock(name='Deck')
        card = {'mana': random.randint(1111, 9999)}
        deck.pick.return_value = card
        player = Player(None, deck)
        player.draw_card()
        deck.pick.assert_called_once_with()
        self.assertEqual(1, player.get_hand_card_number())

    def test_shuffle_deck(self):
        deck = MagicMock(name='Deck')
        player = Player(None, deck)
        player.shuffle_deck()
        deck.card_shuffle.assert_called_once_with(random.shuffle)

    def test_player_can_play_card_if_hasnt_mana(self):
        deck = MagicMock(name='Deck')
        mana_cost = random.randint(1111, 9999)
        card = {'mana': mana_cost}
        deck.pick.return_value = card
        player = Player(None, deck)
        player.add_mana(mana_cost - 1)
        player.draw_card()

        self.assertEqual(0, player.play_cards())
        deck.pick.assert_called_once_with()

    def test_player_can_play_card_when_has_mana(self):
        deck = MagicMock(name='Deck')
        card1 = {'mana': 1, 'damage': 1}
        card2 = {'mana': 2, 'damage': 2}
        deck.pick.side_effect = [card1, card2]

        player = Player(None, deck)
        player.add_mana(3)
        player.draw_card()
        player.draw_card()

        self.assertEqual(3, player.play_cards())


if __name__ == '__main__':
    unittest.main()
