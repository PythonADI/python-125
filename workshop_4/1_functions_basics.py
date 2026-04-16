# Workshop 4 - Functions Basics

# ==============================
# Defining a function
# ==============================

def greet():
    print("Hello, welcome to Python!")

greet()          # Hello, welcome to Python!
greet()          # can call it multiple times


# ==============================
# Parameters and arguments
# ==============================

def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")      # Hello, Alice!
greet_user("Bob")        # Hello, Bob!


# Multiple parameters
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce("Alice", 25)
introduce("Bob", 30)


# ==============================
# Return values
# ==============================

def add(a, b):
    return a + b

result = add(5, 3)
print(result)            # 8
print(add(10, 20))       # 30


def is_even(number):
    return number % 2 == 0

print(is_even(4))        # True
print(is_even(7))        # False


# ==============================
# Return vs Print
# ==============================

# print() displays to the screen but returns None
def add_print(a, b):
    print(a + b)

# return sends a value back to the caller
def add_return(a, b):
    return a + b

result1 = add_print(3, 4)     # prints 7
print(result1)                  # None

result2 = add_return(3, 4)     # prints nothing
print(result2)                  # 7

# With return, you can use the result in other operations
total = add_return(3, 4) + add_return(10, 20)
print(total)                    # 37
