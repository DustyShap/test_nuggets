
from blackjack import Game, Player

def test_a_player_starts_with_amount():
    p = Player()
    assert p.bank == 1000

def test_a_player_can_bet_amounts():
   p = Player()
   assert p.bet(50) == 50
   assert p.bank == 950

def test_a_player_can_win_or_lose_a_hand():
    p = Player()
    p.bet(100)
    assert p.bank == 900
    p.payout(200)
    assert p.bank == 1100
    p.bet(500)
    assert p.bank == 600
    p.payout(0)
    assert p.bank == 600

def test_a_game_has_many_players():
    players = [Player(), Player(), Player()]
    game = Game(*players)
    assert set(game.players) == set(players)


def test_a_game_auto_plays_until_someone_has_zero_dollars():
    game = Game(Player(), Player(), Player())
    turns = game.auto_play()
    assert turns > 0

    assert any(p.bank == 0 for p in game.players)
