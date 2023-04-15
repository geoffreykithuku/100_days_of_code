#Instructions
#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

#Warning. Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

# 1. ask user input
two_digit_number = input("enter a two digit number\n")
# 2. extract each digit
first_number = two_digit_number[0]
second_number = two_digit_number[1]
# 3. convert to int and add them together
result  = int(first_number) + int(second_number)
# 4. print the sum
print("The sum is: ", result)