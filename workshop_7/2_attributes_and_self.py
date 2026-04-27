# Workshop 7 - Attributes and self

# ==============================
# Instance attributes
# ==============================

# Instance attributes belong to ONE specific object.
# They are usually created inside __init__ via "self.something = ...".

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color


car1 = Car("Toyota", "red")
car2 = Car("BMW", "black")

print(car1.brand)       # Toyota
print(car2.brand)       # BMW

# Each instance has its own independent attributes.
car1.color = "green"
print(car1.color)       # green
print(car2.color)       # black (unchanged)

# Never do this!
# car1.wheels = 4

# ==============================
# Class attributes
# ==============================

# Class attributes are shared by ALL instances of the class.
# They are defined directly inside the class, not inside __init__.

class Employee:
    company = "Acme Inc."   # class attribute - shared

    def __init__(self, name, salary):
        self.name = name        # instance attribute
        self.salary = salary    # instance attribute


e1 = Employee("Alice", 5000)
e2 = Employee("Bob", 4000)

print(e1.company)           # Acme Inc.
print(e2.company)           # Acme Inc.

# If we change the class attribute, it changes for everyone.
Employee.company = "Globex"
# print(Employee.name)
# e1.company = "Apple"
print(e1.company)           # Globex
print(e2.company)           # Globex
# quit()

# ==============================
# Instance attribute can shadow class attribute
# ==============================

# If you assign to self.company, only that instance gets a new value.
e1.company = "Stark Industries"
print(e1.company)           # Stark Industries  (instance attribute wins)
print(e2.company)           # Globex            (still the class attribute)


# ==============================
# Understanding "self"
# ==============================

# "self" is the FIRST parameter of every instance method.
# It refers to the specific instance the method was called on.
# Python passes it automatically when you write "obj.method()".

class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        # "self" is the specific Counter the user called .increment() on.
        self.value += 1

    def show(self):
        print(f"value = {self.value}")


a = Counter()
b = Counter()

a.increment()
a.increment()
a.increment()
b.increment()

a.show()        # value = 3
b.show()        # value = 1

# These two calls are equivalent:
a.show()                    # the normal way
Counter.show(a)             # explicit form - "self" is just a regular argument


# ==============================
# Common mistake: forgetting self
# ==============================

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        # CORRECT: use self.name to read the instance attribute
        print(f"{self.name} says woof")

    # def bark_wrong(self):
    #     print(f"{name} says woof")   # NameError - "name" is not defined here
