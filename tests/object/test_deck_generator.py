import unittest
from unittest.mock import MagicMock, call
from app.deck_generator import DeckGenerator


class MyTestCase(unittest.TestCase):
    def test_deck_generator(self):
        card_cost = [0, 0, 1, 2]
        deck = MagicMock(name='deck')
        deck.add = MagicMock(name='add')
        generator = DeckGenerator()
        return_deck =  generator.generate(card_cost, deck)
        deck.add.assert_has_calls([
            call({'mana': 0, 'damage': 0}),
            call({'mana': 0, 'damage': 0}),
            call({'mana': 1, 'damage': 1}),
            call({'mana': 2, 'damage': 2})
        ])
        self.assertEqual(deck, return_deck)


if __name__ == '__main__':
    unittest.main()
