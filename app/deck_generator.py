class DeckGenerator:

    @staticmethod
    def generate(cards_cost, deck):
        for cost in cards_cost:
            deck.add({'mana': cost, 'damage': cost})
        return deck
