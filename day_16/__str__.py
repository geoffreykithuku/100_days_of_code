class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
      """This method controls how a class instance is returned"""
      return f"{self.name} {self.age}"

p1 = Person("John", 36)

print(p1)