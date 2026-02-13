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
        self.end_point = start_x * -1 # other side of screen

        if start_x > 0:
            self.seth(0)
        else:
            self.seth(180)

        self.vehicles = []

    def reset(self):
        self.goto(self.start_xy)
        pass


    def add_vehicle(self, vehicle):
        vehicle.seth(self.heading())
        vehicle.goto(self.start_xy)
        self.vehicles.append(vehicle)

    def move_vehicles(self):

        # always move the first vehicle
        last_moved = self.vehicles[0]
        last_moved.move()

        for i in range(1, len(self.vehicles)):
            v = self.vehicles[i]
            # seperation
            if last_moved.distance(v) > randint(70, 350):
                v.move()
                last_moved = v
            else:
                #TODO: 
                # if they have moved off the screen
                # hide and add reset them.
                return

