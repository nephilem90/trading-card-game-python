class Deck:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def draw(self):
        return_value = False
        if len(self.cards) > 0:
            return_value = self.cards.pop()
        return return_value

    def card_shuffle(self, shuffle_function):
        shuffle_function(self.cards)
