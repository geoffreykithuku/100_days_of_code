#if else

age = int(input("What is your age? "))

if age >= 18:
    print("You can drink alcohol")
else:
    print("You are under age")

#nested if

day = int(input("Enter a number between 1 and 7 "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid number")