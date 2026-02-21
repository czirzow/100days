# day 31
#force pycharm to read requirements.txt
import pandas as pd
import random



LANGUAGES = {
        'fr': 'French',
        'en': 'English',
        }

class Translator():
    translate_dir = 'lang/'

    def __init__(self, lang_from, lang_to):
        try:

            filename = f"{self.translate_dir}{lang_from}_{lang_to}.csv"
            translate = pd.read_csv(filename)

        except FileNotFoundError as e:
            print(f"Unable to open file: {e}")
            exit()
        else:

            self.lang_from = lang_from.title()
            self.lang_to = lang_to.title()
            self.lookup = {c.lang_from:c.lang_to for (_,c) in translate.iterrows()}

    def get(self):
        word = ""
        translated = ""

        if len(self.lookup):
            word = random.choice(list(self.lookup))
            translated = self.lookup[word]

        return (word, translated)


    def is_correct(self, word, test):
        return self.lookup[word] == test

    def remove(self, word):
        del self.lookup[word]
        pass


def setup_widgets(parent, widgets, layout):
    for (name, options) in layout.items():
        print(name)
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

import tkinter as tk
COLOR_WHITE = '#FFFFFF'
BG_COLOR = '#B1DDCC'

window = tk.Tk()
layout = {
        'card_front': {
            'type': tk.Button,
            'config': {
                'image': tk.PhotoImage(file='images/card_front.png'),
                },
            'grid': {
                'column': 0,
                'row': 0,
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
                    },
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
                    },
                },
            },
        }

#bg_image = tk.PhotoImage(file='images/card_front.png')
#bg_label = tk.Label(window, image=bg_image)
#bg_label.place(relwidth=1, relheight=1)
#bg_label.grid(column=0, row=0)
widgets = {}
setup_widgets(window, widgets, layout)

window.mainloop()






if 0 :
    # a sanity check:
    t = Translator('fr', 'en')
    have_a_word = True
    while have_a_word:
        (word, translated) = t.get()
        if word != '':
            print(f"{word}: {translated}")
            t.remove(word)
        else:
            have_a_word = False

