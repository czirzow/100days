from turtle import Turtle

# You'll get a ticket if you get caught.
TICKET_SPEED = 10

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
        self.max_speed = (TICKET_SPEED * 0.80)
        self.length = 1
        self.showturtle()

        self.moves = 0

    def move(self):
        if not self.moves % 10:
            self.forward(self.max_speed)
        self.moves += 1


    def is_speeding(self):
        if self.max_speed > TICKET_SPEED:
            return True
        return False

class Car(Vehicle):
    """A Car: size and speed"""

    def __init__(self, color):
        super().__init__(color)
        self.max_speed = TICKET_SPEED + 10 

class Truck(Vehicle):

    def __init__(self, color, length = 3):
        super().__init__(color)
        self.max_speed = TICKET_SPEED
        self.length = length
        self.shapesize(stretch_wid=2, stretch_len=self.length)

class Semi(Vehicle):

    def __init__(self, color, length = 2):
        super().__init__(color)
        self.max_speed = 1
        self.length = 2
        # TODO: make it smaller than a car.
        self.shapesize(stretch_wid=2, stretch_len=self.length)

