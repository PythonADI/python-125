# Workshop 7 - Classes Basics

# ==============================
# What is a class?
# ==============================

# A class is a blueprint for creating objects.
# An object (also called an "instance") is one specific thing built from that blueprint.
#
# Example: "Dog" is a class. "Rex" and "Buddy" are dogs (instances of Dog).


# ==============================
# Defining a simple class
# ==============================

class Dog:
    # __init__ is the "constructor": it runs when you create a new Dog.
    # "self" refers to the specific instance being created.
    def __init__(self, name, age):
        self.name = name      # attribute on this instance
        self.age = age        # attribute on this instance

    # A method - a function that belongs to the class.
    def bark(self):
        print(f"{self.name} says: Woof!")


# Creating instances
rex = Dog("Rex", 5)
buddy = Dog("Buddy", 2)

print(rex.name)         # Rex
print(buddy.age)        # 2

rex.bark()             # Rex says: Woof!
buddy.bark()            # Buddy says: Woof!


# ==============================
# Each instance keeps its own data
# ==============================

# Changing one instance does not affect another.
rex.age = 6
print(rex.age)          # 6
print(buddy.age)        # 2 (unchanged)


# ==============================
# A more complete class
# ==============================

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def introduce(self):
        print(f"Hi, I'm {self.name} and my grade is {self.grade}.")

    def passed(self):
        return self.grade >= 60


s1 = Student("Alice", 85)
s2 = Student("Bob", 42)

s1.introduce()                  # Hi, I'm Alice and my grade is 85.
s2.introduce()                  # Hi, I'm Bob and my grade is 42.

print(s1.passed())              # True
print(s2.passed())              # False

# ==============================
# Why classes?
# ==============================

# Without a class, you might do this with a dictionary:
alice = {"name": "Alice", "grade": 85}
bob = {"name": "Bob", "grade": 42}

# But every time you want to "introduce" a student, you have to write
# the print statement yourself. With a class, the data AND the behavior
# (methods) live together in one place.
