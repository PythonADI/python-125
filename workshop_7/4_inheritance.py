# Workshop 7 - Inheritance

# Inheritance lets one class reuse code from another class.
#
#   Parent class (also called "base" or "superclass") defines shared behavior.
#   Child class (also called "subclass") gets all of that for free,
#   and can add or change behavior.


# ==============================
# Basic inheritance
# ==============================

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Dog(Animal):              # Dog inherits from Animal
    def bark(self):
        print(f"{self.name} says: Woof!")


horse = Animal("Bucefal")
print(horse.name)
horse.eat()
horse.sleep()

rex = Dog("Rex")
rex.eat()           # inherited from Animal
rex.sleep()         # inherited from Animal
rex.bark()          # defined on Dog


# ==============================
# Overriding methods
# ==============================

# A child class can REPLACE a parent's method by defining one with the same name.

class Cat(Animal):
    def eat(self):
        # override - different message
        print(f"{self.name} eats slowly and dramatically.")


whiskers = Cat("Whiskers")
whiskers.eat()              # uses Cat.eat, not Animal.eat
whiskers.sleep()            # still uses Animal.sleep


# ==============================
# Calling the parent with super()
# ==============================

# Sometimes the child wants to extend the parent, not replace it.
# super() gives you access to the parent's version of a method.

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def describe(self):
        print(f"{self.year} {self.brand}")


class Car(Vehicle):
    def __init__(self, brand, year, doors):
        # Run the parent's __init__ first to set brand and year
        super().__init__(brand, year)
        # Then add the new field that's specific to Car
        self.doors = doors

    def describe(self):
        super().describe()                          # parent's version
        print(f"  with {self.doors} doors")


my_car = Car("Toyota", 2022, 4)
my_car.describe()
# 2022 Toyota
#   with 4 doors


# ==============================
# A bigger example
# ==============================

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def yearly_pay(self):
        return self.salary * 12

    def info(self):
        print(f"{self.name} - yearly pay: ${self.yearly_pay()}")


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    # Override: managers also get a bonus
    def yearly_pay(self):
        return super().yearly_pay() + self.bonus


class Intern(Employee):
    # No need to override __init__ - the parent's is fine

    # Override: interns work fewer months
    def yearly_pay(self):
        return self.salary * 3


alice = Manager("Alice", 5000, 10000)
bob = Employee("Bob", 4000)
carol = Intern("Carol", 1500)

alice.info()        # Alice - yearly pay: $70000
bob.info()          # Bob - yearly pay: $48000
carol.info()        # Carol - yearly pay: $4500


# ==============================
# isinstance() checks the type
# ==============================

print(isinstance(alice, Manager))       # True
print(isinstance(alice, Employee))      # True - Manager IS an Employee
print(isinstance(bob, Manager))         # False
