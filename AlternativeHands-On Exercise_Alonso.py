#Exercise 1 - creating a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Fleinchryunsmarlwinflopoerty", 26)

print("Name:",person1.name)
print("Age:",person1.age)

#Exercise 2 - Apply Encapsulation
class Person:
    def __init__(self, name, __age):
        self.name = name
        self.__age = __age

    def get_age(self):
        return self.__age

person1 = Person("Fleinchryunsmarlwinflopoerty", 26)

print("Name:",person1.name)
print("Age:",person1.get_age())

#Reflection: Its better to access __age through get_age because it is a private attribute
#and should not be accessed directly, it is also easier.
