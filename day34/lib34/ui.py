import tkinter as tk
from lib34.quiz_brain import QuizBrain

THEME_COLOR = "#375362"
COLOR_WHITE = "#FFFFFF"
COLOR_RED = '#FFB3B3'
COLOR_GREEN = '#90EE90'
QUESTION_FONT = ('Arial', 15, 'italic')
CANVAS_HEIGHT = 250
CANVAS_WIDTH  = 300


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window =  tk.Tk()
        self.window.title('Quizzler')
        self.window.resizable(False, False)
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.images = {
                'img_yep': tk.PhotoImage(file="images/true.png"),
                'img_nope': tk.PhotoImage(file="images/false.png"),
                }

        self.score = tk.Label(text="Score: 0", fg=COLOR_WHITE, bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=COLOR_WHITE, highlightthickness=0)
        canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.canvas = canvas

        self.question = canvas.create_text(150, 125, font=QUESTION_FONT,
                                           width=280,
                                           fill=THEME_COLOR, text="This is a question" )

        self.btn_nope = tk.Button(image=self.images['img_nope'],
                                  highlightthickness=0,
                                  pady=20,
                                  command=self.on_btn_nope)
        self.btn_nope.grid(row=2, column=0)

        self.btn_yep = tk.Button(image=self.images['img_yep'],
                                 highlightthickness=0,
                                 pady=20,
                                 command=self.on_btn_yep)
        self.btn_yep.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def on_btn_yep(self):
        self.set_yep_nope('disabled')
        self.give_feedback(self.quiz.check_answer('True'))

    def on_btn_nope(self):
        self.set_yep_nope('disabled')
        self.give_feedback(self.quiz.check_answer('False'))

    def set_yep_nope(self, state):
        self.btn_yep.config(state=state)
        self.btn_nope.config(state=state)


    def update_score(self):
        self.score.config(text=f"Score: {self.quiz.score}")


    def do_we_want_more(self):
        self.set_yep_nope('disabled')
        self.canvas.itemconfig(self.question, text="Game Over.")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg=COLOR_GREEN)
        else:
            self.canvas.config(bg=COLOR_RED)
        self.window.after(1000, self.get_next_question)
        self.update_score()
        self.set_yep_nope('normal')

    def get_next_question(self):
        self.canvas.config(bg=COLOR_WHITE)
        if not self.quiz.still_has_questions():
            self.do_we_want_more()
        else:
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question)



