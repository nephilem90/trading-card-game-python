class Player:
    def __init__(self, life_point, deck):
        if not isinstance(life_point, int):
            life_point = 0
        self.life_point = life_point
        self.deck = deck

    def receive_damage(self, damage):
        self.life_point = self.life_point - damage
        return self

    def is_defeat(self):
        if self.life_point > 0:
            return False
        else:
            return True

    def get_life_point(self):
        return self.life_point

    def draw_card(self):
        card = self.deck.pick()
        if card:
            return
        else:
            self.receive_damage(1)
