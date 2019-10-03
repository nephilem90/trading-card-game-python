class Game:
    def __init__(self, player_one, player_two):
        self.next = 0
        self.players = [player_one, player_two]

    def get_players(self):
        return self.players

    def play_turn(self):
        next_player = (self.next + 1) % 2
        if int(self.players[self.next].get_life_point()) <= 0:
            return False
        self.players[self.next].add_mana(1)
        if not self.players[self.next].draw_card():
            self.players[self.next].receive_damage(1)
            if int(self.players[self.next].get_life_point()) <= 0:
                return False
        else:
            damage = self.players[self.next].play_cards()
            self.players[next_player].receive_damage(damage)
        self.next = next_player
        return True
