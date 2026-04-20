# Workshop 5 - Dictionaries Basics

# ==============================
# Creating a dictionary
# ==============================

# A dictionary stores key-value pairs
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

person_2 = {
    "name": "Luka",
    "age": 25,
    "city": "New York"
}

print(person)
# {'name': 'Alice', 'age': 25, 'city': 'New York'}


# Empty dictionary
empty = {}
print(empty)            # {}

# Also valid:
empty2 = dict()
print(empty2)           # {}


# ==============================
# Accessing values
# ==============================

print(person["name"])   # Alice
print(person["age"])    # 25

# KeyError if key doesn't exist
# print(person["email"])  # KeyError!

# Safer: use .get() — returns None (or a default) if missing
print(person.get("name"))            # Alice
print(person.get("email"))           # None
print(person.get("email", "N/A"))    # N/A



# ==============================
# Adding and updating values
# ==============================

person["email"] = "alice@example.com"    # add a new key
person["age"] = 26                       # update existing key

print(person)
# {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@example.com'}


# ==============================
# Removing values
# ==============================

del person["city"]
print(person)
# {'name': 'Alice', 'age': 26, 'email': 'alice@example.com'}

removed = person.pop("email")
print(removed)          # alice@example.com
print(person)           # {'name': 'Alice', 'age': 26}


# ==============================
# Checking for keys
# ==============================

print("name" in person)    # True
print("phone" in person)   # False

if "age" in person:
    print(f"Age is {person['age']}")


# ==============================
# Dictionary length
# ==============================

scores = {"math": 90, "science": 85, "history": 78}
print(len(scores))       # 3
