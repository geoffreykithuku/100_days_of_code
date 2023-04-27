from art import logo, vs
from game_data import data
import random

# display art 

def format_data(account):
    acc_name = account["name"]
    acc_desc =account["description"]
    acc_country = account["country"]
    return f"{acc_name}, a {acc_desc} form {acc_country}."

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    
    
print(logo)
# generate random account from game_data 
score = 0
should_continue = True
acc2 = random.choice(data)
while should_continue:
    acc1 = acc2
    acc2 = random.choice(data)
    if acc1 == acc2:
        acc2 = random.choice(data)

    # format account data into printable data 

    f_acc1 = format_data(acc1)
    f_acc2 = format_data(acc2)
    print(f"Compare A: {f_acc1}")
    print(vs)
    print(f"Against B: {f_acc2}")
    # ask a user for a quess 
    guess = input("Who has more followers? type 'A' or 'B': ").lower()
    # check follower account of each 
    a_followers = acc1["follower_count"]
    b_followers = acc2["follower_count"]

    # use if statement to check if the user is correct 
    is_correct = check_answer(guess, a_followers, b_followers)

    # give user feedback
    if is_correct:
        score+=1
        print(f"Correct. Current score: {score}")
    else:
        should_continue = False
        print(f"Sorry, you got it wrong. Final score: {score}")
        

# score keeping 
# make game repeatable

# making accounts at position b the next a 
#clear the screen