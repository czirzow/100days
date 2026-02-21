import tkinter as tk
import lib31.translator as trans

COLOR_WHITE = '#FFFFFF'
COLOR_BG  = '#B1DDC6'
COLOR_BLACK = '#000000'


class Flashy:
    def __init__(self, root, images):
        self.root = root
        self.images = images
        self.timer_id = ""
        self.lang_from = ""
        self.lang_to = ""


        canvas = tk.Canvas(width=800, height=526)
        self.card_side  = canvas.create_image(400, 263, image=images['card_front'])
        self.language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
        self.word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
        canvas.config(bg=COLOR_BG, highlightthickness=0)
        canvas.grid(row=0, column=0, columnspan=2)
        self.canvas = canvas

        self.btn_nope = tk.Button(image=self.images['img_nope'], 
                                  highlightthickness=0, 
                                  command=self.on_btn_nope)
        self.btn_nope.grid(row=1, column=0)

        self.btn_yep = tk.Button(image=self.images['img_yep'], 
                                 highlightthickness=0, 
                                 command=self.on_btn_yep
                                 )
        self.btn_yep.grid(row=1, column=1)

    def set_translator(self, translator):
        self.translator = translator

    def on_btn_yep(self):
        self.translator.remove(self.translated.native)
        self.new_card()

    def on_btn_nope(self):
        self.show_back()
        self.disable_buttons()
        self.count_down(5)

    def enable_buttons(self):
        self.btn_yep.config(state="normal")
        self.btn_nope.config(state="normal")

    def disable_buttons(self):
        self.btn_yep.config(state="disabled")
        self.btn_nope.config(state="disabled")
        pass

    def new_card(self):
        self.enable_buttons()
        self.translated = self.translator.get_translated()
        print(self.translated.native, self.translated.value)
        self.show_front()

    def show_back(self):
        c = self.canvas
        c.itemconfig(self.language, text = self.translator.lang['to'], fill=COLOR_WHITE)  
        c.itemconfig(self.word, text=self.translated.value)
        c.itemconfig(self.card_side, image=self.images['card_back'])


    def show_front(self):
        c = self.canvas
        c.itemconfig(self.language, text = self.translator.lang['from'], fill=COLOR_BLACK)  
        c.itemconfig(self.word, text=self.translated.native)
        c.itemconfig(self.card_side, image=self.images['card_front'])


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
window.config(padx=50, pady=50, bg=COLOR_BG)

# Figured out the hard way... these have to be outside a function
flashy_images = {
        'card_front': tk.PhotoImage(file="images/card_front.png"),
        'card_back': tk.PhotoImage(file="images/card_back.png"),
        'img_nope': tk.PhotoImage(file="images/wrong.png"),
        'img_yep': tk.PhotoImage(file="images/right.png"),
}
flashy = Flashy(window, flashy_images)
flashy.set_translator(trans.Translator('fr', 'en'))
flashy.new_card()




window.mainloop()

