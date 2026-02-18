# day 29
# password manager with tkinter
from tkinter import *


#Global:
widgets = {}
file_name = 'data/passwords.txt'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    # reset message??
    show_message()

    values = []
    for name in ['website', 'username', 'password']:
        values.append(widgets[name].get())

    with open(file_name, 'a') as f:
        f.write(" | ".join(values) + "\n")

    for name in ['website', 'username', 'password']:
        widgets[name].delete(0, END)

    show_message(message='Saved', color="green")


def show_message(color='black', message=''):
    widgets['message'].config({
            'fg': color,
            'text': message,
            })


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
        'username': {
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
        'message': {
                'type': Label,
                'config': {
                    'text': '',
                    'width': 40,
                    'pady': 15,
                    },
                'grid': {
                    'column': 1,
                    'row': 5,
                    'columnspan': 3
                    },
                },



        }

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)


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
        widgets[name] = widget

widgets['website'].focus()



window.mainloop()
