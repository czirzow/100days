#the snake classs
from turtle import Turtle

MOVE_DISTANCE = 20
MOVE_UP = 90
MOVE_DOWN = 270
MOVE_LEFT = 180
MOVE_RIGHT = 0


class Snake:
    """controls the snake"""

    def __init__(self) -> None:
        self.snake = []
        self.create_snake()
        self.head: Turtle


    def create_snake(self):
        head = Turtle('square')
        head.color('white')
        head.penup()
        self.head = head
        self.tail = head

        # initialize slelf.snake attribute.
        self.snake = [head]
        for x in range(1, 3):
            #TODO: don't hard code -20
            xy =  (x * MOVE_DISTANCE * -1, head.ycor())
            self.grow(xy)


    def eat_food(self):
        self.grow(self.tail.position())
        pass

    def grow(self, position: tuple):
        t = self.head.clone()
        t.goto(position)
        self.snake.append(t)
        self.tail = t

    def collided_with_self(self) -> bool:
        for s in self.snake[1:-1]:
          if self.head.distance(s) < 10:
              return True

        return False

    def move(self):
        snake = self.snake
        for seg in range(len(snake) - 1, 0, -1):
            xy = snake[seg - 1].pos()
            snake[seg].goto(xy)
        snake[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != MOVE_DOWN:
            self.head.seth(MOVE_UP)

    def down(self):
        if self.head.heading() != MOVE_UP:
            self.head.seth(MOVE_DOWN)

    def left(self):
        if self.head.heading() != MOVE_RIGHT:
            self.head.seth(MOVE_LEFT)

    def right(self):
        if self.head.heading() != MOVE_LEFT:
            self.head.seth(MOVE_RIGHT)

