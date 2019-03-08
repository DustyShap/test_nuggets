
class Player:
    def __init__(self):
        self.bank = 1000

    def bet(self, amount):
        self.bank -= amount
        return amount

    def payout(self, amount):
        self.bank += amount

class Game:
    def __init__(self, *players):
        self.players = players

    def auto_play(self):
        while [player for player in self.players if player.bank > 0]:
            for player in self.players:
                player.bet(500)
                player.payout(0)
        return 1

