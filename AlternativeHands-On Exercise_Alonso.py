#Exercise 1: creating a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Fleinchryunsmarlwinflopoerty", 26)

print("Name:",person1.name)
print("Age:",person1.age)

#Exercise 2: Apply Encapsulation
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

#Exercise 3: Apply Inheritance
class Person:
    def __init__(self, name, __age):
        self.name = name
        self.__age = __age

    def get_age(self):
        return self.__age
    
class Student(Person):
    def __init__(self, name, __age):
        super().__init__(name, __age)

    def study(self):
        print(f"{self.name} is studying.")


person1 = Person("Fleinchryunsmarlwinflopoerty", 26)

print("Name:",person1.name)
print("Age:",person1.get_age())
print(person1.name, Student(person1.name, person1.get_age()).study())

#Exercise 4: Create the Teacher class
class Person:
    def __init__(self, name, __age):
        self.name = name
        self.__age = __age

    def get_age(self):
        return self.__age
    
class Student(Person):
    def __init__(self, name, __age):
        super().__init__(name, __age)

    def study(self):
        print(f"{self.name} is studying.")

class Teacher(Person):
    def __init__(self, name, __age):
        super().__init__(name, __age)

    def teach(self):
        print(f"{self.name} is teaching.")

person1 = Student("Fleinchryunsmarlwinflopoerty", 26)
person2 = Teacher("Job", 30)

print("Name:",person2.name)
print("Age:",person2.get_age())
person2.name, Teacher(person2.name, person2.get_age()).teach()






#Exercise 6: Apply Abstraction
import abc
import abstractmethod

class Person(abc.ABC):
    def __init__(self, name, __age):
        self.name = name
        self.__age = __age

    def get_age(self):
        return self.__age

class Student(Person):
    def __init__(self, name, __age):
        super().__init__(name, __age)

    def study(self):
        print(f"{self.name} is studying.")

    def role(self):
        return "is a Student"

class Teacher(Person):
    def __init__(self, name, __age):
        super().__init__(name, __age)

    def teach(self):
        print(f"{self.name} is teaching.")

    def role(self):
        return " is a Teacher"

person1 = Student("Fleinchryunsmarlwinflopoerty", 26)
person2 = Teacher("Job", 30)

print("Name:", person1.name)
print("Age:", person1.get_age())
person1.name, Student(person1.name, person1.get_age()).study()
print(person1.name, Student(person1.name, person1.get_age()).role())

print("")

print("Name:",person2.name)
print("Age:",person2.get_age())
person2.name, Teacher(person2.name, person2.get_age()).teach()
print(person2.name, Teacher(person2.name, person2.get_age()).role())








#Reflection: Its better to access __age through get_age because it is a private attribute
#and should not be accessed directly, it is also easier.
