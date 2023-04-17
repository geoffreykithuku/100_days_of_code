
print("*********************************************")
print("******Welcome to rock paper scissor game******")
print("********************************************")

import random 

user_choice = int(input("Enter 0 for Rock, 1 for Paper or 2 for Scissors\n"))
computer_choice = random.randint(0, 2)
if user_choice >= 3 or user_choice < 0:
    print('You lost')
    
elif user_choice == 0 and computer_choice == 2:
    print("You won!")
elif computer_choice == 0 and user_choice == 2:
    print("You lost!")
elif computer_choice > user_choice:
    print("You lost!")
elif user_choice > computer_choice:
    print("You won!")
elif computer_choice == user_choice:
    print("It is a draw!")
