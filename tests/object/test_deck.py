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

    def test_deck_generator(self):
        card_cost = [0, 0, 1, 2]
        deck = Deck.generate(card_cost)
        cards_expected = [
            {'mana': 0, 'damage': 0},
            {'mana': 0, 'damage': 0},
            {'mana': 1, 'damage': 1},
            {'mana': 2, 'damage': 2},
        ]
        self.assertEqual(deck.cards, cards_expected)


if __name__ == '__main__':
    unittest.main()
