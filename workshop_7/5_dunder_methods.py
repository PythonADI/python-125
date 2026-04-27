# Workshop 7 - Dunder ("magic") methods

# Methods with names like __something__ are called "dunder" methods
# (double underscore). Python calls them automatically in certain situations.
#
# We've already seen one: __init__ is called when you create an instance.


# ==============================
# __str__ - what print() shows
# ==============================

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


rex = Dog("Rex", 5)
print(rex)              # <__main__.Dog object at 0x...>  - not friendly

class FriendlyDog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Dog(name={self.name}, age={self.age})"


buddy = FriendlyDog("Buddy", 3)
print(buddy)            # Dog(name=Buddy, age=3)


# ==============================
# __repr__ - what shows in the REPL / lists
# ==============================

# __str__ is for users. __repr__ is for developers (debugging).
# If you only define one, define __repr__ - it's used as a fallback for __str__.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


p = Point(1, 2)
print(p)                            # Point(1, 2)
# quit()
print([Point(0, 0), Point(3, 4)])   # [Point(0, 0), Point(3, 4)]


# ==============================
# __eq__ - what == means
# ==============================

# By default, two different instances are NEVER equal, even with the same data.

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency


a = Money(100, "USD")
b = Money(100, "USD")
print(a == b)                       # False - different objects in memory


class SmartMoney:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        if not isinstance(other, SmartMoney):
            return False
        return self.amount == other.amount and self.currency == other.currency


x = SmartMoney(100, "USD")
y = SmartMoney(100, "USD")
z = SmartMoney(50, "USD")
print(x == y)                       # True
print(x == z)                       # False
# print(x is not y)


# ==============================
# __len__ - what len() returns
# ==============================

class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add(self, member):
        self.members.append(member)

    def __len__(self):
        return len(self.members)


team = Team("Avengers")
team.add("Iron Man")
team.add("Thor")
team.add("Hulk")
print(len(team))                    # 3


# ==============================
# Putting it together
# ==============================

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __repr__(self):
        return f"Book({self.title!r}, {self.pages})"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.pages == other.pages

    def __len__(self):
        return self.pages


b1 = Book("Python 101", 300)
b2 = Book("Python 101", 300)
b3 = Book("Algorithms", 500)

print(b1)               # Book('Python 101', 300)
print(b1 == b2)         # True
print(b1 == b3)         # False
print(len(b1))          # 300
print(id(b1), id(b2))
print(b1 is b2)
