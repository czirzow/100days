from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 40, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()

        self.l_score = 0
        self.r_score = 0
        self.show_score()




    def show_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def increase_left(self):
        self.l_score += 1
        self.show_score()

    def increase_right(self):
        self.r_score += 1
        self.show_score()

    def game_over(self):
        self.show_score()
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)


