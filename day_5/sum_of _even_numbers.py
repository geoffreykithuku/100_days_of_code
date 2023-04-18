#code that adds even numbers from 1-100, including 100
#using loops and range
# no using sum


total = 0

for number in range (0, 101, 2):
    total += number
    
print(total)