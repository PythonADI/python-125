def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


result = greet("Alice")
print(f"{result = }")

result = greet("Marry", "Good Morning")
print(f"{result = }")

result = greet("ნიკა", "გამარჯობა")
print(f"{result = }")