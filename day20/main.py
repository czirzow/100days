from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


REFRESH_RATE = 0.1

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')


snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


game_is_on = True
i = 0
while game_is_on:
    i += 1
    screen.update()
    time.sleep(REFRESH_RATE)
    snake.move()

    # Detect food collision
    #                              #size of food + 5
    if snake.head.distance(food) < 15:
        snake.eat_food()
        score.increase_score()
        food.refresh()

    # detection with wall
    # FIXME: make a function, passing the dimensions
    # BUG: yeah program isn't fully functional.
    if snake.head.xcor() > 280:
        game_is_on = False
        score.game_over()
    
    # Detect collision with self.
    if snake.collided_with_self():
        game_is_on = False
        score.game_over()
    # __DEBUG__:  I'm to lazy to playe game..  
    # Just loop in a cricle so tail gets eaten quickly
    if i % 2 == 0:
        snake.eat_food()
        snake.head.left(90)



screen.exitonclick()

