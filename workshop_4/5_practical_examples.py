# Workshop 4 - Practical Examples

# ==============================
# Example 1: Password validator
# ==============================

def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters"

    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    if not has_upper:
        return False, "Password must contain an uppercase letter"
    if not has_lower:
        return False, "Password must contain a lowercase letter"
    if not has_digit:
        return False, "Password must contain a digit"

    return True, "Password is strong!"

passwords = ["hello", "Hello123", "HELLO123", "HelloWorld1"]
for pw in passwords:
    valid, message = validate_password(pw)
    print(f"'{pw}' -> {message}")


# ==============================
# Example 2: Temperature converter
# ==============================

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(f"0C = {celsius_to_fahrenheit(0):.1f}F")
print(f"100C = {celsius_to_fahrenheit(100):.1f}F")
print(f"72F = {fahrenheit_to_celsius(72):.1f}C")


# ==============================
# Example 3: Shopping list manager
# ==============================

def add_item(shopping_list, item):
    if item.lower() in [i.lower() for i in shopping_list]:
        return shopping_list, f"'{item}' is already in the list"
    shopping_list.append(item)
    return shopping_list, f"'{item}' added"

def remove_item(shopping_list, item):
    for i, existing in enumerate(shopping_list):
        if existing.lower() == item.lower():
            shopping_list.pop(i)
            return shopping_list, f"'{item}' removed"
    return shopping_list, f"'{item}' not found"

def show_list(shopping_list):
    if not shopping_list:
        print("Shopping list is empty!")
        return
    print("Shopping List:")
    for i, item in enumerate(shopping_list, 1):
        print(f"  {i}. {item}")

my_list = []
my_list, msg = add_item(my_list, "Milk")
print(msg)
my_list, msg = add_item(my_list, "Bread")
print(msg)
my_list, msg = add_item(my_list, "Eggs")
print(msg)
my_list, msg = add_item(my_list, "Milk")  # duplicate
print(msg)

show_list(my_list)

my_list, msg = remove_item(my_list, "Bread")
print(msg)
show_list(my_list)


# ==============================
# Example 4: Simple calculator with functions
# ==============================

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None, "Cannot divide by zero!"
    return a / b, "OK"

def calculator(a, operator, b):
    if operator == "+":
        return add(a, b)
    elif operator == "-":
        return subtract(a, b)
    elif operator == "*":
        return multiply(a, b)
    elif operator == "/":
        result, status = divide(a, b)
        if status != "OK":
            print(status)
            return None
        return result
    else:
        print(f"Unknown operator: {operator}")
        return None

print(calculator(10, "+", 5))   # 15
print(calculator(10, "-", 3))   # 7
print(calculator(10, "*", 4))   # 40
print(calculator(10, "/", 3))   # 3.333...
print(calculator(10, "/", 0))   # Cannot divide by zero!
