# day 29
# password manager with tkinter


# FIXME: getting a wild card import * warning, but code runs in pyCharm
from tkinter import *
import json
import pyperclip

#
# TODO: use pyperclip
#       auto copy password gernerated to clipboard.


#
# TODO make this all into a class model
#      there isn't a need to do globals.
#
#Global:
widgets = {}
file_name = 'data/passwords.json'


from random import choice, randint, shuffle, shuffle
class RandomPassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    @classmethod
    def get(cls):
        """ returns a random password """

        password_list  = [choice(cls.letters) for _ in range(randint(8, 10))]
        password_list += [choice(cls.numbers) for _ in range(randint(2, 4))]
        password_list += [choice(cls.symbols) for _ in range(randint(2, 4))]

        shuffle(password_list)

        return "".join(password_list)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    global widgets

    widgets['password'].insert(END, RandomPassword.get())
    pyperclip.copy(widgets['password'].get())
    show_message(message='Password copy to clipboard.', color='green')


# ---------------------------- SAVE PASSWORD ------------------------------- #
def validate_and_save():
    global widgets

    show_message(message='Saving...')

    # with just simple validation
    save_values = ['website', 'username', 'password']
    values = [widgets[n].get() for n in save_values 
              if widgets[n].get().strip() != '']

    if len(values) != len(save_values):
        show_message("All fields must be filled out", color='red')
        return

    if not save_password():
        # save_password() already filled out the message box so just:
        return

    #  clear out the most likely entries
    for name in ['website', 'password']:
        widgets[name].delete(0, END)

    show_message('Saved !', color="green")


def save_password():
    global file_name
    global widgets

    website = widgets['website'].get()
    username = widgets['username'].get()
    password = widgets['password'].get()
    new_data = {
            website: {
                "username": username,
                "password": password,
            }
    }


    #TODO: check for if file exists, if not create it.
    #

    try:
        with open(file_name, 'r') as fh:
            data = json.load(fh)
            data.update(new_data)

    except FileNotFoundError as e:
        show_message(f"Unable to save to {file_name}:\n {e}", color='red')
        return False

    except json.JSONDecodeError as e:
        show_message(f"{file_name} has bad data. remaking it.")
        data = new_data

    try:
        with open(file_name, 'w') as fh:
            json.dump(data, fh, indent=4)

    except PermissionError as e:
        show_message(f"Can't write to {file_name}:\n {e}", color='red')
        return False

    show_message(f"saved to {file_name}.", color='green')

def search_website():
    pass

def show_message(message='', color='black'):
    """sets the message label with a message
    if message is blank it will clear the message label
    """
    global widgets

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
                'width': 21,
                },
            'grid': {
                'column': 1,
                'row': 1,
                'columnspan': 2,
                'sticky': 'w',
                },
            },
        'search_website': {
            'type': Button,
            'config': {
                'text': 'search',
                'command': search_website,
                },
            'grid': {
                'column': 2,
                'row': 1,
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
                'text': 'Save',
                'width': 36,
                'command': validate_and_save,
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
                    'pady': 15,
                    },
                'grid': {
                    'column': 0,
                    'row': 5,
                    'columnspan': 4
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

