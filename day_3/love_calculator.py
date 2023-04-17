# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


combined_name = name1 + name2
lowercase_name = combined_name.lower()

t = lowercase_name.count("t")
r = lowercase_name.count("r")
u = lowercase_name.count("u")
e = lowercase_name.count("e")

true = t+r+u+e

l = lowercase_name.count("l")
o = lowercase_name.count("o")
v = lowercase_name.count("v")
e = lowercase_name.count("e")

love = l+o+v+e
true_love = str(true) + str(love)
true_love = int(true_love)

if ((true_love) < 10) or (true_love > 90):
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif (true_love >= 40) and (true_love <=50):
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}")