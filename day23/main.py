# turtller - a mimic of frogger

from turtle import Screen

# rename mylib to game/
from mylib.vehicles import Truck,Car,Semi
from mylib.player import Player
from mylib.lane import Lane
from mylib.scoreboard import ScoreBoard

import time

screen = Screen()
screen.setup(600, 600)
screen.title("Turtler")
screen.tracer(0)

def vehicle_out_of_screen(vehicle):
    width = screen.window_width()
    if vehicle.xcor() < -width/2:
        return True
    return False

def player_won(player):
    height = screen.window_height() - 40
    if player.ycor() > height/2:
        return True
    return False

p = Player()
c = Truck('red')
c2 = Car('blue')
c3 = Truck('green')
c4 = Semi('yellow')

#right to left only supported

# FIXME: figure out the proper parameters to pass.
border = screen.window_width() * -1
border_right = screen.window_width()/2
l = Lane(border, (border_right, -100))
l.add_vehicle(c)
l.add_vehicle(c2)
l.add_vehicle(c3)

sb = ScoreBoard()


screen.listen()
screen.onkey(key="Up", fun=p.up)
screen.onkey(key="Down", fun=p.down)

screen = Screen()
screen.tracer(0)
screen.setup(600, 600)
screen.title("Turtller 2.0")
screen.listen()
screen.onkey(key="Up", fun=p.up)

game_is_on = True
while game_is_on:

    #if vehicle_out_of_screen(c):
        #c.setx(300)

    #if player_won(p):
        #sb.level_up()
        #p.reset()

    #if c.distance(p) < 20:
        #print(f"Collided {c.distance(p)}")
        #game_is_on = False

    l.move_vehicles()
    screen.update()
    time.sleep(0.01)


screen.exitonclick()

