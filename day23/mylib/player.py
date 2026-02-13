from turtle import Turtle

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('green')
        self.seth(90)
        self.goto(0, -280)
        self.showturtle()


    def reset(self):
        self.hideturtle()
        self.goto(0, -280)
        self.penup()
        self.showturtle()

    def up(self):
        self.sety(self.ycor() + 20)

