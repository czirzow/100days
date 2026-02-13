from turtle import Turtle



#BALL_SPEED: how fast the ball goes across the screen
BALL_SPEED = 0.1

# SPEED_FACTOR: the small the number the faster the ball will
# move each time it hits a paddle.
# recomended value: 0.9
SPEED_FACTOR = 1
# ie:
# 1   - ball  doesn't change speeds
# < 1 - ball speeds up
# > 1 - ball slows down


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')

        self.x_move = 10
        self.y_move = 10

        self.move_speed = BALL_SPEED


    # export this turtle.pos() for the game to know my position.
    # FIXME: is this needed? my editor said it didn't know about  var.pos()
    def pos(self):
        return super().pos()

    def move(self):
        xy = (
                self.xcor() + self.x_move,
                self.ycor() + self.y_move
             )
        self.goto(xy)

    def bounce_of_wall(self):
        self.y_move *= -1

    def hit_of_paddle(self):
        self.x_move *= -1
        self.move_speed *= SPEED_FACTOR

    def restart_game(self):
        self.goto(0, 0)



