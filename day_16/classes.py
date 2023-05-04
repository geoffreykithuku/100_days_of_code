class Car:
    model = "Honda"
    year= 2021
    
car1 = Car()
    


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
   
    def __str__(self):
        return f"{self.name} {self.age}"
    
person1 = Person("Alice", 25)

print(person1)