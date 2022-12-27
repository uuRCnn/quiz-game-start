import data


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.puan = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(data.question_data)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def score(self):
        return (f"{self.puan}/{self.question_number}")

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you got it dogru cevap!")
            self.puan += 1
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}.")
        print(f"{self.puan}/{self.question_number}")

        print(" \n ")