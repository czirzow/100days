# day 31
#force pycharm to read requirements.txt
import pandas as pd
import random
import tkinter as tk


LANGUAGES = {
        'fr': 'French',
        'en': 'English',
        }
CARD_IMAGES = {
        'front': 'images/card_front.png'
        }


COLOR_WHITE = '#FFFFFF'
BG_COLOR = '#B1DDCC'

# TODO: move to flashcard.translator:
# requires: pandas
##import pandas as pd
class Translator():
    translate_dir = 'lang/'

    def __init__(self, lang_from: str, lang_to:str, dir:str = "lang/") -> None:
        """ something like:
        t = Translator('de', 'fr', dir='.langs/')
        """
        try:
            self.translation_dir = dir
            filename = f"{self.translate_dir}{lang_from}_{lang_to}.csv"

            translate = pd.read_csv(filename)


        except FileNotFoundError as e:
            print(f"Unable to open file: {e}")
            exit()
        except pd.errors.EmptyDataError as e:
            print(f"Problem parsing file: {e}")
            pass
        except pd.errors.ParserError as e:
            print(f"Problem parsing file: {e}")
            pass
        else:

            self.lang_from = lang_from.title()
            self.lang_to = lang_to.title()
            self.lookup = {c.lang_from:c.lang_to for (_,c) in translate.iterrows()}

    def get(self):
        """returns a tuple with (lang_from, lang_to)"""
        
        lang_from = ""
        lang_to = ""

        if len(self.lookup):
            lang_from = random.choice(list(self.lookup))
            lang_to = self.lookup[word]

        return (lang_from, lang_to)

    def remove(self, word):
        """remove a word from the list so it won't be returned again"""
        del self.lookup[word]

# a sanity for class
if 0 :
    t = Translator('fr', 'en')
    have_a_word = True
    while have_a_word:
        (word, translated) = t.get()
        if word != '':
            print(f"{word}: {translated}")
            t.remove(word)
        else:
            have_a_word = False


#TODO: make this a class.
def setup_widgets(parent: tk.Tk, widgets: dict, layout: dict):
    """"a widget maker
    parent - a tkinter widget
    widgets - dictionary of widgets
    layout - dictionary of layouts
     """
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


window = tk.Tk()

# 
# layout: a dict for setup widgets(layout=layout) 
layout = {
        'card_front': {
            'type': tk.Button,
            'config': {
                'image': tk.PhotoImage(file=CARD_IMAGES['front']),
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


widgets = {}
setup_widgets(window, widgets, layout)

window.mainloop()



