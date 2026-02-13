from turtle import Turtle

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):


    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('black')

        self.level = 1
        self.goto(-280, 230)
        self.show_level()

    def level_up(self):
        self.level += 1
        self.show_level()

    def show_level(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)
        print(f"Level: {self.level}")

    def game_over(self):
        self.home()
        self.write("GAME  OVER", align="center", font=FONT)
        print("GAME  OVER")

