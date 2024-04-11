from data import question_data
from question_model import Question
from quiz_brain import Quiz

question_bank = []
for element in question_data:
    question_bank.append(Question(element["question"], element["correct_answer"]))

quiz = Quiz(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

