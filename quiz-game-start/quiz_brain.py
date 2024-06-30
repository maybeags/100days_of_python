#TODO:1. asking the questions.
#TODO:2. checking if the answer was correct.
#TODO:3. checking if we're the end of the quiz.

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # def next_question(self, question_list):
    #     score = 0
    #     is_on = True
    #     while is_on:
    #         for n in range(len(question_list)):
    #             response = input(f"{question_list[n].text} True / False : ")
    #             if response == question_list[n].answer:
    #                 score += 1
    #             print(f"현재 점수는 {score}입니다.")

    # def still_has_question(self, question_list):
    #     """ Returns True or False """
    #     for n in range(len(question_list)):
    #         return True
    # #     return False

    # def next_question(self):
    #     current_question_number = 0
    #     while self.still_has_question(self.question_list):
    #         if current_question_number < len(self.question_list):
    #             current_question = self.question_list[self.question_number]
    #             self.question_number += 1
    #             current_question_number += 1
    #             input(f"Q.{self.question_number}: {current_question.text} (True/False): ")

    # def still_has_questions(self):
    #     if self.question_number < len(self.question_list):
    #         return True
    #     else:
    #         return False

    def still_has_questions(self):
        return self.question_number < len(self.question_list)       # 위의 것보다 간단하다

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The answer is {correct_answer}.")
        print(f"Your current score is : {self.score} / {self.question_number}")
        print("\n")
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)


