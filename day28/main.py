from tkinter import Tk, Canvas, PhotoImage, Label, Button
import math

# ---------------------------- CONSTANTS ------------------------------- #
WHITE="#ffffff"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = '✔'


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min = math.floor(count / 60)
    sec = count % 60
    canvas.itemconfig(timer_text, text=f"{min:02d}:{sec:02d}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        # next stage.
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

window = Tk()
window.title('Pomodoro')
window.config(**config['window'])


timer_l = Label()
timer_l.config(**config['timer'])
timer_l.grid(column=1, row=0)

canvas = Canvas(**config['canvas'])

image = PhotoImage(file='images/tomato.png')
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 140, **config['canvas_text'])
canvas.grid(column=1, row=1)


start_b = Button(text="Start", fg=WHITE, bg=GREEN, command=start_timer)
start_b.config(**config['start'])
start_b.grid(column=0, row=2)

reset_b = Button(text="Reset", fg=WHITE, bg=GREEN, command=reset_timer)
reset_b.config(**config['reset'])
reset_b.grid(column=2, row=2)

checks_l = Label(text=CHECKMARK*4, fg=GREEN, bg=YELLOW)
checks_l.config(**config['checks'])
checks_l.grid(column=1, row=3)


window.mainloop()

