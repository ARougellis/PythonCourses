class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.user_score = 0

    def still_has_questions(self):
        more_questions = True
        if self.question_number == len(self.question_list):
            more_questions = False

        return more_questions

    def next_question(self):
        question = self.question_list[self.question_number].text
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question} (true/false)? : ").lower()

        return user_answer

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("Correct!")
            self.user_score += 1
        else:
            print("Incorrect...")
            print(f"The correct answer is {correct_answer}.")

        print(f"Current score : {self.user_score}/{self.question_number}")
        print("")
