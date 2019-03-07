
class Traveler:
    def __init__(self):
        self.universal_time_speed = 1
        self.speed = 0
        self.age = 0
        self.current_year = 2019

    def increase_speed(self, speed_delta):
        self.speed += speed_delta
        self.universal_time_speed = 1.0 + (.001*self.speed)/200

    def clock(self):
        self.age += 1.0 - ((self.universal_time_speed - 1.0) * .2)

    def change_year(self, years):
        self.current_year += years
