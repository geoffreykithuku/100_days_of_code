def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1 * n2

def div(n1, n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}

n1  = int(input("Enter the first number"))
n2  = int(input("Enter the second number"))

for operation in operations:
    print(operation)
    
op = input("Which of the above operation do you want to perform? ")

calculate = operations[op]
first_answer = calculate(n1,n2)
print(f"{n1} {op} {n2} = ", first_answer)

op = input("Which of the above operation do you want to perform? ")

n3  = int(input("Enter the next number"))
calculate = operations[op]
print(f"{first_answer} {op} {n3} = ", calculate(first_answer,n3))