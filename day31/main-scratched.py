# day 31
import tkinter as tk
from lib31 import translator as t


CARD_IMAGES = {
        'front': 'images/card_front.png',
        'back': 'images/card_back.png',
        'right': 'images/right.png',
        'wrong': 'images/wrong.png',
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

class Flashy():
    def __init__(self, front_img, back_img):
        self.front_img = front_img
        self.back_img = back_img
        self.timer_id = ""

    def set_widgets(self, widgets):
        self.widgets = widgets

    def set_translator(self, translator):
        self.translator = translator

    def set_buttons(self):
        self.widgets['press_right'].config(command=self.press_right)
        self.widgets['press_wrong'].config(command=self.press_wrong)
        pass


    def press_right(self):
        if self.timer_id:
            return
        self.translator.remove(self.lang_from)
        self.new_card()

    def press_wrong(self):
        if self.timer_id:
            return
        self.show_back()
        self.count_down(5)

    def new_card(self):
        (self.lang_from, self.lang_to) = self.translator.get()
        self.show_front()
        print(self.lang_from, self.lang_to)

    def show_front(self):
        self.widgets['top_label'].config(text=self.translator.lang['from'])
        self.widgets['bottom_label'].config(text=self.lang_from)
        self.widgets['card_front'].config(image=self.front_img)

    def show_back(self):
        self.widgets['top_label'].config(text=self.translator.lang['to'])
        self.widgets['bottom_label'].config(text=self.lang_to)
        self.widgets['card_front'].config(image=self.back_img)

    def start_timer(self):
        pass

    def finish_timer(self):
        window.after_cancel(self.timer_id)
        self.timer_id = ""
        self.new_card()


    def count_down(self, count):
        if count > 0:
            print("count: ", count)
            self.timer_id = window.after(1000, self.count_down, count - 1)
        else:
            self.finish_timer()





window = tk.Tk()
window.title("Flashy")
window.config(bg=BG_COLOR,
              padx=50,
              pady=50)
window.resizable(False, False)


flashy = Flashy(front_img=tk.PhotoImage(file=CARD_IMAGES['front']),
                back_img=tk.PhotoImage(file=CARD_IMAGES['back']))
flashy.set_translator(t.Translator('fr', 'en'))

# 
# layout: a dict for setup widgets(layout=layout) 
layout = {
        'card_front': {
            # Front of card
            'type': tk.Button,
            'config': {
                'image': tk.PhotoImage(file=CARD_IMAGES['front']),
                'height': 526,
                'width': 800,
                'bg': BG_COLOR,
                'relief': 'flat',
                'activebackground': BG_COLOR,
                'bd': 0,
                },
            'grid': {
                'column': 0,
                'row': 0,
                'columnspan': 2,
                },
            'children': {
                'top_label': {
                    'type': tk.Label,
                    'config': {
                        'text': 'French',
                        'font': ('Arial', 15, 'italic'),
                        'bg': COLOR_WHITE,
                        },
                    'place': {
                        'x': 300,
                        'y': 150,
                        },
                    }, #/front_lang_from
                'bottom_label': {
                    'type': tk.Label,
                    'config': {
                        'text': 'Français',
                        'bg': COLOR_WHITE,
                        'font': ('Arial', 20, 'bold'),
                        },
                    'place': {
                        'x': 300,
                        'y': 263,
                        },
                    }, #/front_lang_to
                }, #/children
            }, #/card
        'press_wrong': {
            'type': tk.Button,
            'config': {
                'image': tk.PhotoImage(file=CARD_IMAGES['wrong']),
                },
            'grid': {
                'column': 0,
                'row': 1,
                },
            },
        'press_right': {
            'type': tk.Button,
            'config': {
                'image': tk.PhotoImage(file=CARD_IMAGES['right']),
                },
            'grid': {
                'column': 1,
                'row': 1,
                },
            },
        }


widgets = {}
setup_widgets(window, widgets, layout)

flashy.set_widgets(widgets)
flashy.set_buttons()

flashy.new_card()

window.mainloop()



