

class QuizBrain:
    def __init__(self, question_list):
        self.quiz_number = 0
        self.question_list = question_list
        self.score = 0
        
    def still_has_questions(self):
        length = len(self.question_list)
        return self.quiz_number < length
    
    def next_question(self):
        current_question = self.question_list[self.quiz_number]
        self.quiz_number+=1
        user_answer = str(input(f"Q.{self.quiz_number}: {current_question.text} (True/False)?:"))
        self.check_answer(user_answer, str(current_question.answer))
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")  
        else:
            print(f"Wrong")
            
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.quiz_number}")
        print("\n")
        