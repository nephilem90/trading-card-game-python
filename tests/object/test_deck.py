import unittest
from unittest.mock import MagicMock
from app.object.deck import Deck


class TestDeck(unittest.TestCase):
    def test_add_and_pick(self):
        deck = Deck()
        card = {}
        deck.add(card)
        self.assertEqual(card, deck.pick())

    def test_if_empty_return_false(self):
        deck = Deck()
        self.assertFalse(deck.pick())

    def test_shuffle_deck(self):
        deck = Deck()
        deck.add({'mana': 1})
        deck.add({'mana': 2})
        deck.add({'mana': 3})
        shuffle = MagicMock(name='shuffle')
        deck.card_shuffle(shuffle)
        shuffle.assert_called_once_with([{'mana': 1}, {'mana': 2}, {'mana': 3}])


if __name__ == '__main__':
    unittest.main()
