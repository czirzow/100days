from turtle import Turtle

# The Scoreboard class
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    """Manages the score board"""

    def __init__(self):
        super().__init__()
        self.undobuffer = ""
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 250)


        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write(f"GAME OVER !", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

