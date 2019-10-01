class Game:
    def __init__(self, player_one, player_two):
        player_one.set_life_point(20)
        player_two.set_life_point(20)
        self.players = [player_one, player_two]

    def get_players(self):
        return self.players

