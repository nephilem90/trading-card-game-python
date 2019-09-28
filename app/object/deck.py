class Deck:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def pick(self):
        return_value = False
        if len(self.cards) > 0:
            return_value = self.cards.pop()
        return return_value

    def card_shuffle(self, shuffle_function):
        shuffle_function(self.cards)

    @classmethod
    def generate(cls, cards_cost):
        deck = cls()
        for cost in cards_cost:
            deck.add({'mana': cost, 'damage': cost})
        return deck
