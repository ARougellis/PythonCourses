import sys

sys.path.append('/Users/arougellis/Desktop/PythonCourse/100Days/Projects/QuizGame')

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    # question_bank.append(Question(question_data[question]['text'], question_data[question]['answer']))
    # OR
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    user_answer = quiz.next_question()
    correct_answer = quiz.question_list[quiz.question_number-1].answer

    quiz.check_answer(user_answer, correct_answer)

print("You've completed the quiz!")
print(f"Final Score : {quiz.user_score}/{quiz.question_number}")
