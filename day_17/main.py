from question_class import Question 
from quiz_data import QUESTIONS 
from quiz_brain import QuizBrain


question_list = []

for item in QUESTIONS:
    text = item["text"]
    answer = item["answer"]
    new_queston = Question(text, answer)
    question_list.append(new_queston)
    
quiz= QuizBrain(question_list)

while quiz.still_has_questions():
    quiz.next_question()
print("You have completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.quiz_number}")