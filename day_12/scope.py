# global scope
age = 20

def change_age():
    # local scope
    age = 21
    print(age)

# prints from global scope
print(age)

# prints from local scope
change_age()