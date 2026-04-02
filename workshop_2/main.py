# Workshop 2 - Conditionals, Strings, and User Input

# ==============================
# 1. Input from user
# ==============================

name = input("Enter your name: ")
print(f"Hello, {name}!")

age = int(input("Enter your age: "))
print(f"You are {age} years old.")

# input() always returns a string, so we convert with int() or float()
price = float(input("Enter a price: "))
print(f"Price with tax: {price * 1.12}")


# ==============================
# 2. String methods
# ==============================

message = "  Hello, Python World!  "

print(message.upper())          # "  HELLO, PYTHON WORLD!  "
print(message.lower())          # "  hello, python world!  "
print(message.strip())          # "Hello, Python World!"
print(message.replace("Python", "Java"))  # "  Hello, Java World!  "
print(message.count("l"))       # 3
print(len(message))             # 25 (includes spaces)

email = "user@example.com"
print(email.startswith("user"))  # True
print(email.endswith(".com"))    # True

full_name = "john doe"
print(full_name.title())        # "John Doe"
print(full_name.capitalize())   # "John doe"

# String indexing and slicing
word = "Python"
print(word[0])      # P
print(word[-1])     # n
print(word[0:3])    # Pyt
print(word[2:])     # thon
print(word[:4])     # Pyth

# Check if substring exists
print("Py" in word)      # True
print("java" in word)    # False


# ==============================
# 3. if / elif / else
# ==============================

temperature = 38

if temperature >= 40:
    print("Extreme heat!")
elif temperature >= 30:
    print("It's hot outside.")
elif temperature >= 20:
    print("Nice weather.")
elif temperature >= 10:
    print("It's cool.")
else:
    print("It's cold!")

# Nested conditions
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive.")
    else:
        print("You need a license first.")
else:
    print("You are too young to drive.")


# ==============================
# 4. Logical operators: and, or, not
# ==============================

age = 25
is_student = True

# and - both conditions must be True
if age >= 18 and is_student:
    print("Adult student - eligible for discount.")

# or - at least one condition must be True
is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("No work today!")

# not - reverses the condition
is_raining = False

if not is_raining:
    print("Let's go for a walk!")

# Combining logical operators
score = 85
attendance = 90

if score >= 80 and attendance >= 75:
    print("Passed with good standing.")
elif score >= 60 or attendance >= 90:
    print("Conditionally passed.")
else:
    print("Failed.")


# ==============================
# 5. Putting it all together
# ==============================

# Simple login system
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print(f"Welcome, {username.title()}!")
elif username == "admin":
    print("Wrong password!")
else:
    print("User not found.")

# Grade calculator
score = float(input("Enter your score (0-100): "))

if score > 100 or score < 0:
    print("Invalid score!")
elif score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
