#Exercise 1 - creating a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Fleinchryunsmarlwinflopoerty", 26)

print("Name:",person1.name)
print("Age:",person1.age)
