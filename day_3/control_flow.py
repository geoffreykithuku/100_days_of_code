#if else

age = int(input("What is your age? "))

if age >= 18:
    print("You can drink alcohol")
else:
    print("You are under age")

#elif

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
    
    
#nested if
#using age from the first program

if age >= 18:
    ticket = (input("Do you have a ticket? "))
    if ticket.lower() == 'yes':
        print("You can enter")
    else:
        print("You need a ticket to enter")
else:
    print("You are too young to enter")