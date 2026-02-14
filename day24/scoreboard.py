from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()

        self.score = 0
        self.high_score_file = 'highscore.txt'
        self.high_score = self.high_score_read()
        self.update_scoreboard()

    def high_score_read(self):
        try:
            with open(self.high_score_file) as f:
                score = f.read()
                if not score.isnumeric():
                    score = 0

        except FileNotFoundError:
            score = 0


        return int(score)

    def high_score_save(self):
        with open(self.high_score_file, mode='w') as f:
            f.write(str(self.score))


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.high_score_save()

        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
