import random


class Player:
    def __init__(self, life_point, deck):
        if not isinstance(life_point, int):
            life_point = 0
        self.life_point = life_point
        self.deck = deck
        self.mana = 0
        self.hand_cards = []
        self.hand_cards_cost = []

    def receive_damage(self, damage):
        self.life_point = self.life_point - damage
        return self

    def get_life_point(self):
        return self.life_point

    def add_mana(self, add_to_pool):
        self.mana = self.mana + add_to_pool
        return self

    def get_mana(self):
        return self.mana

    def draw_card(self):
        card = self.deck.pick()
        cost = card.get_mana()
        self.hand_cards_cost.append(cost)
        self.hand_cards_cost.sort(reverse=True)
        self.hand_cards.insert(self.hand_cards_cost.index(cost), card)
        return self

    def shuffle_deck(self):
        self.deck.card_shuffle(random.shuffle)

    def get_hand_card_number(self):
        return len(self.hand_cards)

    def play_cards(self):
        damage = 0
        while len(self.hand_cards_cost) > 0 and self.mana >= self.hand_cards_cost[-1]:
            self.hand_cards_cost.pop()
            card = self.hand_cards.pop()
            damage = damage + card.get_damage()
            self.mana = self.mana - card.get_mana()
        return damage
