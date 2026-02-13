# Ping Pong - The classic game
from turtle import Screen
from scoreboard import ScoreBoard
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
sb = ScoreBoard()
p_left = Paddle((-350, -150))
p_right = Paddle((350, 200))
b = Ball()


# TODO: make a Pong() class that handles all this:
# pong.__init()
screen.tracer(0)
screen.title("Pong!")
screen.bgcolor('black')
screen.setup(height=600, width=800)
screen.listen()
screen.onkey(key='Up', fun=p_right.up)
screen.onkey(key='Down', fun=p_right.down)
screen.onkey(key='w', fun=p_left.up)
screen.onkey(key='s', fun=p_left.down)

def ball_bounce(ball):
    height = screen.window_height() - 40 # 40 is a margin

    y = ball.ycor()
    if y < -height/2 or y > height/2:
        return True

    return False

# pong.is_out_of_bounds(ball)
def is_out_of_bounds(ball):
    width = screen.window_width() - 40 # 40 is a margin

    x = ball.xcor()
    if x < -width/2 or x > width/2:
        return True

    return False


game_is_on = True
TOTAL_RESTARTS = 1
restarts = 0
while game_is_on:
    screen.update()
    time.sleep(b.move_speed)

    b.move()
    if ball_bounce(b):
        b.bounce_of_wall()

    if is_out_of_bounds(b):
        restarts += 1
        b.restart_game()
        if restarts > TOTAL_RESTARTS:
            game_is_on = False

    # in this game it is about who can hit the ball
    if b.distance(p_right) < 50 and b.xcor() > 330:
        sb.increase_right()
        b.hit_of_paddle()
    elif b.distance(p_left) < 50 and b.xcor() < -330:
        sb.increase_left()
        b.hit_of_paddle()

    screen.update()

sb.game_over()


screen.exitonclick()
