import unittest
from unittest.mock import MagicMock
from app.object.deck import Deck


class TestDeck(unittest.TestCase):
    def test_add_and_pick(self):
        deck = Deck()
        card = MagicMock()
        deck.add(card)
        self.assertEqual(card, deck.pick())

    def test_if_empty_return_false(self):
        deck = Deck()
        self.assertFalse(deck.pick())

    def test_shuffle_deck(self):
        deck = Deck()
        deck.add(1)
        deck.add(2)
        deck.add(3)
        shuffle = MagicMock(name='shuffle')
        deck.card_shuffle(shuffle)
        shuffle.assert_called_once_with([1, 2, 3])


if __name__ == '__main__':
    unittest.main()
