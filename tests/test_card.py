import unittest
from app.card import Card


class TestCard(unittest.TestCase):
    def test_creation(self):
        card = Card({'mana': 3})
        self.assertEqual(card.get_mana(), 3)


if __name__ == '__main__':
    unittest.main()
