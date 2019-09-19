import unittest
from unittest.mock import MagicMock
from app.object.deck import Deck


class TestDeck(unittest.TestCase):
    def test_add_and_draw(self):
        deck = Deck()
        card = MagicMock()
        deck.add(card)
        self.assertEqual(card, deck.draw())


if __name__ == '__main__':
    unittest.main()
