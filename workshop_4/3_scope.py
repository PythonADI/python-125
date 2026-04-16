# Workshop 4 - Scope (Local vs Global)

# ==============================
# Local scope
# ==============================

def my_function():
    x = 10              # local variable - only exists inside this function
    print(f"Inside function: x = {x}")

my_function()
# print(x)             # NameError: x is not defined


# ==============================
# Global scope
# ==============================

name = "Alice"          # global variable

def say_hello():
    print(f"Hello, {name}!")    # can READ global variables

say_hello()             # Hello, Alice!
print(name)             # Alice


# ==============================
# Local vs Global with same name
# ==============================

color = "blue"          # global

def change_color():
    color = "red"       # this creates a NEW local variable, doesn't change global
    print(f"Inside: {color}")

change_color()          # Inside: red
print(f"Outside: {color}")   # Outside: blue


# ==============================
# Best practice: use parameters and return values
# ==============================

# Bad: using global variables
total = 0

def add_to_total_bad(amount):
    global total
    total += amount

add_to_total_bad(10)
add_to_total_bad(20)
print(total)            # 30


# Good: using parameters and return values
def add_to_total_good(current_total, amount):
    return current_total + amount

my_total = 0
my_total = add_to_total_good(my_total, 10)
my_total = add_to_total_good(my_total, 20)
print(my_total)         # 30
