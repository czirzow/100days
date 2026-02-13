from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, xy):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(5, 1)
        self.penup()
        self.goto(xy)

    def up(self):
        self.sety(self.ycor() + 20)

    def down(self):
        self.sety(self.ycor() - 20)

