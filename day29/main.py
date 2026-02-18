# day 29
# password manager with tkinter
from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    pass

# ---------------------------- UI SETUP ------------------------------- #

layout = {
        'l_website': {
            'type': Label,
            'config': {
                'text': 'Website:',
                },
            'grid': {
                'column': 0,
                'row': 1,
                }
            },
        'website': {
            'type': Entry,
            'config': {
                'justify': 'left',
                'width': 35,
                },
            'grid': {
                'column': 1,
                'row': 1,
                'columnspan': 2,
                'sticky': 'w',
                },
            },
        'l_email': {
            'type': Label,
            'config': {
                'text': 'Email/Username:',
                },
            'grid': {
                'column': 0,
                'row': 2,
                }
            },
        'email': {
            'type': Entry,
            'config': {
                'width': 21,
                },
            'grid': {
                'column': 1,
                'row': 2,
                'columnspan': 2,
                'sticky': 'w',
                },
            },
        'l_password': {
            'type': Label,
            'config': {
                'text': 'Password:',
                },
            'grid': {
                'column': 0,
                'row': 3,
                }
            },
        'password': {
            'type': Entry,
            'config': {
                'width': 21,
                },
            'grid': {
                'column': 1,
                'row': 3,
                'sticky': 'w',
                },
            },
        'generate_password': {
            'type': Button,
            'config': {
                'text': 'Generate Password',
                'command': generate_password,
                },
            'grid': {
                'column': 2,
                'row': 3,
                },
            },
        'add': {
            'type': Button,
            'config': {
                'text': 'Add',
                'width': 36,
                'command': save_password,
                },
            'grid': {
                'column': 1,
                'row': 4,
                'columnspan': 2,
                },
            },

        }

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)


# hard coded canvas.. its a bit tricky
canvas = Canvas(width=200, height=200)
image = PhotoImage(file='images/logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

widgets = {}
for (name, options) in layout.items():
    if 'type' in options:
        widget = options['type']()
        widget.config(options['config'])
        widget.grid(options['grid'])



window.mainloop()
