#if the number is diviible by 3, print fizz
#if the number is divisible by 5, print buzz
#if the number is divisible by both 3 and 5, print fizzbuzz
#else, print number itself


for number in range(1, 100):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)