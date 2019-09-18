import unittest
from app.card import Card
import random


class TestCard(unittest.TestCase):
    def test_creation(self):
        cost = random.randrange(1111, 9999)
        card = Card(cost)
        self.assertEqual(card.get_mana(), cost)
        self.assertEqual(card.get_damage(), cost)


if __name__ == '__main__':
    unittest.main()
