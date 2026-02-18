# day 29
# password manager with tkinter
from tkinter import *
from tkinter import messagebox


#
# TODO make this all into a class model
#      there isn't a need to do globals.
#
#Global:
widgets = {}
file_name = 'data/passwords.txt'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #
def validate_and_save():
    global widgets

    # reset message
    show_message(message='Saving')

    
    # this should be standard.. 
    # with just simple validation
    save_values = ['website', 'username', 'password']
    values = [widgets[n].get() for n in save_values 
              if widgets[n].get().strip() != '']

    if len(values) != len(save_values):
        show_message(color='red', message="All fields must be filled out")
        return
    
    # Prompt if they want to continue...
    title = widgets['website'].get()
    msg = f"""Do you want to save this data?
    username: {widgets['username'].get()}
    password: {widgets['password'].get()}
    """
    if not messagebox.askyesno(title=title, message=msg):
        show_message(message='Did not save to file')
        return

    save_password(values)

    #  clear out the most likely entries
    for name in ['website', 'password']:
        widgets[name].delete(0, END)

    show_message(message='Saved !', color="green")


def save_password(values):
    global file_name

    try:
        with open(file_name, 'a') as f:
            f.write(" | ".join(values) + "\n")
    except:
        return False

    return True


def show_message(message='', color='black'):
    """sets the message label with a message"""

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
