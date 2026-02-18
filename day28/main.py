from tkinter import Tk, Canvas, PhotoImage, Label, Button
import math

#TODO: make a class out of this
# Goal: remove the global variables
#       they should be delt within a class that needs them
# class Pomodoro(Tk):
# add grid to to config
#



# ---------------------------- CONSTANTS ------------------------------- #
WHITE="#ffffff"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 300
CHECKMARK = '✔'


reps = 0
reps_settings = [
        { 'mode': 'Work', 'timer': WORK_MIN},
        { 'mode': 'Break', 'timer': SHORT_BREAK_MIN},
        { 'mode': 'You got this', 'timer': WORK_MIN},
        { 'mode': 'Breath', 'timer': SHORT_BREAK_MIN},
        { 'mode': 'Work', 'timer': WORK_MIN},
        { 'mode': 'Relax', 'timer': LONG_BREAK_MIN},
        ]
timer_id = ""
timer_text = ""

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer_id, reps
    window.after_cancel(timer_id)
    config_window(config, to_config)
    reps = 0
    canvas.itemconfig(timer_text, text=f"{0:02d}:{0:02d}")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, reps_settings

    if reps % 2:
        checks['text'] += CHECKMARK

    if reps == len(reps_settings):
        checks['text'] = ''
        reps = 0

    config = reps_settings[reps]
    timer['text'] = config['mode']
    reps += 1

    count_down(config['timer'])


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer_id
    min = math.floor(count / 60)
    sec = count % 60
    canvas.itemconfig(timer_text, text=f"{min:02d}:{sec:02d}")
    if count > 0:
        timer_id = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        pass

# ---------------------------- UI SETUP ------------------------------- #

config = {
        'window': {
            'padx': 100,
            'pady':  50,
            'bg': YELLOW,
            },
        'timer': {
            'text': "Timer",
            'fg': GREEN,
            'bg': YELLOW,
            'font': (FONT_NAME, 25),
            },
        'start': {
            'text': "Start",
            'fg': WHITE,
            'bg': GREEN,
            'command': start_timer
            },
        'reset': {
            'text': "Reset",
            'fg': WHITE,
            'bg': GREEN,
            'command': reset_timer
            },
        'checks': {
            'text': '',
            'fg': GREEN,
            'bg': YELLOW,
            },
        ## there are extra steps to handle canvas
        'canvas': {
            'width': 200,
            'height': 224,
            'bg': YELLOW,
            'highlightthickness': 0,
            },
        'canvas_text': {
            'text': "00:00",
            'fill': "white",
            'font': (FONT_NAME, 24, 'bold'),
            },
        }


def config_window(config, items):
    for name in items:
        i = items[name]
        i.config(config[name])



to_config = {}

window = Tk()
window.title('Pomodoro')
to_config['window'] = window


timer = Label(name="timer_l")
timer.grid(column=1, row=0)
to_config['timer'] = timer


# this is odd, manual configuration
# TODO: figure out a way to auto config this.
canvas = Canvas(**config['canvas'])
image = PhotoImage(file='images/tomato.png')
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 140, **config['canvas_text'])
canvas.grid(column=1, row=1)


start = Button()
start.grid(column=0, row=2)
to_config['start'] = start


reset = Button()
reset.grid(column=2, row=2)
to_config['reset'] = reset


checks = Label()
checks.grid(column=1, row=3)
to_config['checks'] = checks
config_window(config, to_config)



window.mainloop()

