# day 31
import tkinter as tk


LANGUAGES = {
        'fr': 'French',
        'en': 'English',
        }
CARD_IMAGES = {
        'front': 'images/card_front.png',
        'back': 'images/card_back.png',
        'right': 'images/card_right.png',
        'wrong': 'images/card_wrong.png',
        }
COLOR_WHITE = '#FFFFFF'
BG_COLOR = '#B1DDCC'


# is there not a tool that does this?
def setup_widgets(parent: tk.Tk, widgets: dict, layout: dict):
    """"a widget maker
    parent - a tkinter widget
    widgets - dictionary of widgets
    layout - dictionary of layouts
     """
    for (name, options) in layout.items():
        print(f"setting up widget {name}")
        if 'type' in options:
            widget = options['type'](master=parent)
            widget.config(options['config'])
            if 'grid' in options:
                widget.grid(options['grid'])
            if 'place' in options:
                widget.place(x=options['place']['x'],
                             y=options['place']['y'])
            if 'children' in options:
                setup_widgets(widget, widgets, options['children'])

            widgets[name] = widget

    return widgets


window = tk.Tk()

# 
# layout: a dict for setup widgets(layout=layout) 
# TODO: add font and add the two buttons at the bottom.
# TODO: add card_back it's basicly a dup of 'front' but with a different image
layout = {
        'card_front': {
            'type': tk.Button,
            'config': {
                'image': tk.PhotoImage(file=CARD_IMAGES['front']),
                },
            'grid': {
                'column': 0,
                'row': 0,
                'columnspan': 2,
                },
            'children': {
                'front_lang_from': {
                    'type': tk.Label,
                    'config': {
                        'text': 'French',
                        'bg': COLOR_WHITE,
                        },
                    'place': {
                        'x': 400,
                        'y': 150,
                        },
                    }, #/front_lang_from
                'front_lang_to': {
                    'type': tk.Label,
                    'config': {
                        'text': 'Français',
                        'bg': COLOR_WHITE,
                        },
                    'place': {
                        'x': 400,
                        'y': 263,
                        },
                    }, #/front_lang_to
                }, #/children
            }, #/card front
        # TODO: add card_back
        # TODO: add the two buttons on row 1

        }


widgets = {}
setup_widgets(window, widgets, layout)

window.mainloop()



