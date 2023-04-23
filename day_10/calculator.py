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

for key in operations:
    if key == op:
        print(operations[key](n1, n2))