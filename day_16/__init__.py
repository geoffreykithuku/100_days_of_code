class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

dog = Animal("Dog", "barks")

cat= Animal
cat.name = "cat"
cat.sound = "miaw"
print(cat.sound)