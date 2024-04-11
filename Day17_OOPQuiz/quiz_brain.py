# the Quiz object is someone who asks questions
# create the Quiz class which has the next_question() function
# the function takes a Question object, displays  question.text during the input(), and check if the input value
# equals question.answer
import question_model


class Quiz:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        """asks the Question object text from the question_list of index question_number, receives answer input and
        verifies answer. score+=1 if correct"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        check = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")

        self.check_answer(current_question.answer, check)
        print(f"Your current score is {self.score}/{self.question_number}\n")

    def still_has_questions(self):
        """Checks if question number of object is within scope of question_list. Returns True"""
        return self.question_number < len(self.question_list)

    def check_answer(self, question_answer, input_p):
        if input_p == question_answer:
            print("Correct.")
            self.score += 1
        else:
            print("Incorrect.")