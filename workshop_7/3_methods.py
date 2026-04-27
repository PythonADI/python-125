# Workshop 7 - Methods
import math


# A method is a function defined inside a class.
# It can read and change the instance's data through "self".


# ==============================
# Methods that change state
# ==============================

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def check_amount(self, amount):
        if amount <= 0:
            print("Amount should be positive")
            return False
        return True

    def deposit(self, amount):
        if not self.check_amount(amount):
            return
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Not enough funds. Balance is {self.balance}")
            return
        if not self.check_amount(amount):
            return
        self.balance -= amount

    def show(self):
        print(f"{self.owner}: ${self.balance}")


acc = BankAccount("Alice", 100)
acc.show()              # Alice: $100
acc.deposit(50)
acc.withdraw(30)
acc.show()              # Alice: $120
acc.withdraw(1000)      # Not enough funds...
# quit()

# ==============================
# Methods that return values
# ==============================

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height


r = Rectangle(4, 5)
print(r.area())             # 20
print(r.perimeter())        # 18
print(r.is_square())        # False

s = Rectangle(3, 3)
print(s.is_square())        # True


# ==============================
# Methods calling other methods
# ==============================

# A method can call another method on the same object via self.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def describe(self):
        # reuse area() instead of repeating the formula
        print(f"Circle with radius {self.radius} and area {self.area():.2f}")


c = Circle(10)
c.describe()                # Circle with radius 10 and area 314.16


# ==============================
# Methods that take other objects as arguments
# ==============================

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        # "other" is another Point
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx * dx + dy * dy)


p1 = Point(0, 0)
p2 = Point(3, 4)
print(p1.distance_to(p2))   # 5.0


# ==============================
# A class can hold a list (or dict) of things
# ==============================

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add(self, song):
        self.songs.append(song)

    def remove(self, song):
        if song in self.songs:
            self.songs.remove(song)

    def show(self):
        print(f"Playlist: {self.name}")
        for i, song in enumerate(self.songs, start=1):
            print(f"  {i}. {song}")


pl = Playlist("Workout")
pl.add("Eye of the Tiger")
pl.add("Lose Yourself")
pl.add("Stronger")
pl.show()
pl.remove("Lose Yourself")
pl.show()
