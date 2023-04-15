# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years = int(90 - int(age))
months = years * 12
weeks = years * 52
days = years * 365

print(f"You have {days} days, {weeks} weeks, and {months} months left.")