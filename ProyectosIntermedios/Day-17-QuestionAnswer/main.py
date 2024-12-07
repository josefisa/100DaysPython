# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#         print("El constructor ha iniciado...")
        
#     def got_followed(self, user):
#         user.followers += 1
#         self.following += 1
        
# user_1 = User("001", "camilito")
# user_2 = User("002", "pepito")

# user_1.got_followed(user_2)
    
# print(user_1.followers)
# print(user_2.followers)
# print(user_1.following)
# print(user_2.following)


#  H E R E   S T A R T S   T H E    C O D E    F O R    T H E   Q U I Z    G A M E

from question_model import Question
#from data import question_data  #Unquote this line or the next, to unlock new data
from data import opentdb
from quiz_brain import QuizBrain
question_bank = []
victory_streak = 0


#for question in question_data:
for question in opentdb:
                    #To play with different dataset, just cange the attribute name in question["Here"].
    question_text = question["question"]  #text
    question_answer = question["correct_answer"]  #answer
    
    new_question = Question(question_text,question_answer)
    
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

#print(f"Procces finished at {quiz.question_number}")
print("You have completed the Quiz!!!")
print(f"Your total score is : {quiz.score}/{quiz.question_number}")