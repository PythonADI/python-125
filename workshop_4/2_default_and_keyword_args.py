# Workshop 4 - Default and Keyword Arguments

# ==============================
# Default parameter values
# ==============================

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")                # Hello, Alice!
greet("Bob", "Good morning")  # Good morning, Bob!


def power(base, exponent=2):
    return base ** exponent

print(power(5))       # 25  (5 squared)
print(power(2, 10))   # 1024  (2 to the 10th)


# ==============================
# Keyword arguments
# ==============================

def create_profile(name, age, city):
    print(f"{name}, {age}, from {city}")

# Positional arguments (order matters)
create_profile("Alice", 25, "New York")

# Keyword arguments (order doesn't matter)
create_profile(city="London", name="Bob", age=30)

# Mix: positional first, then keyword
create_profile("Charlie", city="Paris", age=28)


# ==============================
# Practical example: receipt printer
# ==============================

def print_receipt(item, price, quantity=1, tax_rate=0.10):
    subtotal = price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax
    print(f"Item: {item}")
    print(f"Price: ${price:.2f} x {quantity}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax ({tax_rate:.0%}): ${tax:.2f}")
    print(f"Total: ${total:.2f}")
    print("-" * 25)

print_receipt("Laptop", 999.99)
print_receipt("Headphones", 49.99, quantity=3)
print_receipt("Book", 15.00, quantity=2, tax_rate=0.05)
