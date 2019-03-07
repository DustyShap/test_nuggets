from traveler import Traveler

def test_time_traveler_has_time_rate():
    traveler = Traveler()
    assert traveler.universal_time_speed == 1.0

def test_time_traveler_can_change_speed():
    traveler = Traveler()
    traveler.increase_speed(2)
    assert traveler.speed == 2

def test_time_travelers_time_rate_changes_with_speed():
    traveler = Traveler()
    traveler.increase_speed(200)
    assert traveler.universal_time_speed == 1.001
    traveler.increase_speed(200)
    assert traveler.universal_time_speed == 1.002
    traveler.increase_speed(-200)
    assert traveler.universal_time_speed == 1.001


def test_time_travelers_clock_ticks_away_at_the_life_of_the_traveler():
    traveler_1 = Traveler()
    traveler_2 = Traveler()
    traveler_2.increase_speed(200*1000)

    assert traveler_1.age == traveler_2.age and traveler_1.age == 0

    traveler_1.clock()
    traveler_2.clock()

    assert traveler_1.age == 1
    assert traveler_2.age == 0.8

def test_time_traveler_travels_to_diff_year():
    traveler = Traveler()
    assert traveler.current_year == 2019
    traveler.change_year(5)
    assert traveler.current_year == 2024
    traveler.change_year(-2)
    assert traveler.current_year == 2022
