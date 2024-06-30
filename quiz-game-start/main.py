from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank =[]
# for n in range(len(question_data)):
#     question_bank.append(question_data[n])
#
# print(question_bank)

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# quiz_brain = QuizBrain(question_bank)
# quiz_brain.next_question(question_bank)
#
quiz = QuizBrain(question_bank)
# print(len(question_bank))
# while quiz.still_has_question(question_bank): # if quiz still has questions remaining:
#     quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was : {quiz.score} / {quiz.question_number}")
