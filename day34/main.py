from lib34.question_model import Question
from lib34.quiz_brain import QuizBrain

from data.data import question_data

from opentrivia.api import OpenTriviaApi
import json
from lib34.ui import QuizInterface






def refresh_data():
    api = OpenTriviaApi(amount=1)

    result = api.get()
    with open('data/data.py', 'w') as fh:
        print("refresh")
        fh.write("question_data = ")
        json.dump(result, fh, indent=4)

    return result


def get_question_bank(question_data):
    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    return question_bank


quiz = QuizBrain(get_question_bank(question_data))
ui = QuizInterface(quiz)

exit()

while True:
    while quiz.still_has_questions():
        question = quiz.next_question()
        input()
        



    print("refreshing data bank")
    question_data = refresh_data()
    quiz = QuizBrain(get_question_bank(question_data))


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
