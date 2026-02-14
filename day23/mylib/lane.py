from turtle import Turtle
from random import randint


CARS_PER_LANE = 2

class Lane(Turtle):
    """A Lane for vehicles"""

    def __init__(self, start_x, start_xy) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()

        self.start_xy = start_xy
        print(f"{start_xy}");
        self.reset()

        self.start_x = start_x
        self.start_point = self.start_x
        self.end_point = -300 #start_x * -1 # other side of screen

        if start_x > 0:
            self.seth(0)
        else:
            self.seth(180)

        self.vehicles = []

    def reset(self):
        print(f"{self.start_xy}")
        self.goto(self.start_xy)
        pass


    def add_vehicle(self, vehicle):
        vehicle.initialize(self.heading(), self.start_xy)
        self.vehicles.append(vehicle)

    def player_is_hit(self, player):

        for v in self.vehicles:
            if v.distance(player) < 10:
                return True

        return False

    def move_vehicles(self, person):

        # always move the first vehicle
        last_moved = self.vehicles[0]
        last_moved.move()
        #if last_moved.distance(person) > 20:
        #    return True

        # if we are beyond the screen, put it at the end of the list.
        if last_moved.xcor() < self.end_point - last_moved.length -100:
            self.vehicles.pop(0)
            self.vehicles.append(last_moved)
            last_moved.initialize(self.heading(), self.start_xy)


        for i in range(1, len(self.vehicles)):
            v = self.vehicles[i]
            # seperation
            if last_moved.distance(v) > randint(70, 150):
                v.move()
                last_moved = v

            else:
                # no need to move anymore.
                return

        #return False
