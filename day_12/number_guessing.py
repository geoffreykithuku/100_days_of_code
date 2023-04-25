# # import the random module

# function to determine the level of difficulty
# let a user guess a number
# function to compare the user's guess wth the answer

# track number of turns left

# repeat if wrong


import random 
from art import logo
EASY_LEVEL = 10
HARD_LEVEL = 5
game_over = False
turns = 0

def game_level():
    level = input("Enter the level of difficult. Type 'easy' or 'hard' ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL



def check_answer(guess, answer, turns):
    if guess == answer:
        print("You won")
    elif guess > answer:
        print("Too high")
        print("Guess again ")
        return turns-1
    else:
        print("Too low")
        print("Guess again ")
        return turns-1
 
   


def game():
    turns = game_level()
    answer = random.randint(1, 101)
    guess = 0
   
    while guess != answer and turns != 0:
        guess = int(input("Guess a number between 1 and 100 "))
        
        turns = check_answer(guess, answer, turns)
        
        print(f"You have {turns} turns left")
        
        
    if turns == 0:
        print("You lost!")

print(logo)       
game()
