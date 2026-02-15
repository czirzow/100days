# Day 25
import pandas as pd
import turtle

class StateLabel(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

image = "states/blank_states_img.gif"
state_file = "states/50_states.csv"
states = pd.read_csv(state_file)

screen = turtle.Screen()
screen.setup(725, 491)
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)

label = StateLabel()


found_states = 0
while found_states < 50:
    guess = screen.textinput("Guess State", "Enter a state")
    if guess == None:
        found_states = 51
        continue

    state = states[states.state == guess]
    if not state.empty:
        label.goto(state.x.item(), state.y.item())
        label.write(state.state.item())
        found_states += 1


turtle.mainloop()

