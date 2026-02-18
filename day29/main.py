# day 29
# password manager with tkinter
from tkinter import Tk, Canvas, PhotoImage


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

config = {
        'window': {
            'padx': 20,
            'pady': 20,
            'height': 220,
            'width': 220,
            },
        'canvas': {
            'width': 200,
            'height': 200,
            'highlightthickness': 0,
            }
        }

window = Tk()
window.title('Password Manager')
window.config(config['window'])

#canvas = Canvas(width=400, height=400)
canvas = Canvas(**config['canvas'])
image = PhotoImage(file='images/logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(column=0, row=0)


window.mainloop()
