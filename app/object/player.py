import random


class Player:
    def __init__(self, life_point):
        if not isinstance(life_point, int):
            life_point = 0
        self.life_point = life_point
        self.mana = 0
        self.hand_cards = []
        self.hand_cards_cost = []
        self.deck = None

    def add_deck(self, deck):
        self.deck = deck
        return self

    def receive_damage(self, damage):
        self.life_point = self.life_point - damage
        return self

    def get_life_point(self):
        return self.life_point

    def add_mana(self, add_to_pool):
        self.mana = self.mana + add_to_pool
        return self

    def set_life_point(self, life_pint):
        self.life_point = life_pint

    def get_mana(self):
        return self.mana

    def draw_card(self):
        if not self.deck:
            return False
        card = self.deck.pick()
        if not card:
            return False
        cost = card['mana']
        self.hand_cards_cost.append(cost)
        self.hand_cards_cost.sort(reverse=True)
        self.hand_cards.insert(self.hand_cards_cost.index(cost), card)
        return True

    def shuffle_deck(self):
        self.deck.card_shuffle(random.shuffle)

    def get_hand_card_number(self):
        return len(self.hand_cards)

    def play_cards(self):
        damage = 0
        while len(self.hand_cards_cost) > 0 and self.mana >= self.hand_cards_cost[-1]:
            self.hand_cards_cost.pop()
            card = self.hand_cards.pop()
            damage = damage + card['damage']
            self.mana = self.mana - card['mana']
        return damage
