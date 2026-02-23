from lib34.question_model import Question
from lib34.quiz_brain import QuizBrain
from lib34.ui import QuizInterface
from data.manager import Manager as DataManager



def to_quiz_brain_data(question_data):
    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    return question_bank



# TODO: where to put this.
manager = DataManager()
#disable 
# TODO: ask 
#manager.refresh_data(30)

quiz = QuizBrain(to_quiz_brain_data(manager.question_data))
ui = QuizInterface(quiz)

