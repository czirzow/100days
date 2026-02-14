from turtle import Turtle
import random

# You'll get a ticket if you get caught.
TICKET_SPEED = 10
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
TYPES = ["car", "truck", "semi"]



class Vehicle(Turtle):
    """A Car, or bike or whatever you want"""

    def __init__(self, color) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape('square')
        self.color(color)
        self.seth(180)
        self.setx(300)
        self.max_speed = TICKET_SPEED
        self.length = 1
        self.showturtle()

        self.moves = 0

    def move(self):
        if not self.moves % 100:
            self.forward(self.max_speed)
        self.moves += 1

    def get_random(self):
        color = random.choice(COLORS)
        vehicle = random.choice(TYPES)
        if vehicle == 'truck':
            return Truck(color)
        elif vehicle == 'Semi':
            return Semi(color)
        else:
            return Car(color)

    def initialize(self, heading, xy):
        self.seth(heading)
        self.goto(xy)


    def is_speeding(self):
        if self.max_speed > TICKET_SPEED:
            return True
        return False

class Car(Vehicle):
    """A Car: size and speed"""

    def __init__(self, color):
        super().__init__(color)
        self.length = 2
        self.max_speed = TICKET_SPEED + 5
        self.shapesize(1, stretch_len=self.length)

class Truck(Vehicle):

    def __init__(self, color, length = 3):
        super().__init__(color)
        self.max_speed = TICKET_SPEED
        self.length = 3
        self.shapesize(1, stretch_len=self.length)

class Semi(Vehicle):

    def __init__(self, color, length = 2):
        super().__init__(color)
        self.max_speed = TICKET_SPEED - 5
        self.length = 4
        # TODO: make it smaller than a car.
        self.shapesize(1, stretch_len=self.length)

