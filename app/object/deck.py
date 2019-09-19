class Deck:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def draw(self):
        return self.cards.pop()
