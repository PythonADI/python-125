# Workshop 5 - Sets

# ==============================
# Creating a set
# ==============================

# A set is an unordered collection of unique items
fruits = {"apple", "banana", "cherry"}
print(fruits)

# Duplicates are automatically removed
numbers = {1, 2, 3, 2, 1, 4}
print(numbers)          # {1, 2, 3, 4}

# Empty set — must use set(), {} creates a dict!
empty = set()
print(type(empty))      # <class 'set'>


# ==============================
# Adding and removing
# ==============================

fruits.add("orange")
print(fruits)

fruits.remove("banana")     # raises KeyError if not found
print(fruits)

fruits.discard("grape")     # safe — does nothing if not found
print(fruits)


# ==============================
# Membership testing (very fast)
# ==============================

print("apple" in fruits)       # True
print("banana" in fruits)      # False


# ==============================
# Set operations
# ==============================

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Union — items in either set
print(a | b)                  # {1, 2, 3, 4, 5, 6, 7, 8}
print(a.union(b))

# Intersection — items in both sets
print(a & b)                  # {4, 5}
print(a.intersection(b))

# Difference — items in a but not in b
print(a - b)                  # {1, 2, 3}
print(a.difference(b))

# Symmetric difference — items in either but not both
print(a ^ b)                  # {1, 2, 3, 6, 7, 8}


# ==============================
# Removing duplicates from a list
# ==============================

emails = [
    "alice@x.com",
    "bob@x.com",
    "alice@x.com",
    "carol@x.com",
    "bob@x.com",
]

unique_emails = set(emails)
print(unique_emails)
print(f"Unique: {len(unique_emails)}, Total: {len(emails)}")


# ==============================
# Practical example: common friends
# ==============================

alice_friends = {"Bob", "Charlie", "Diana", "Eve"}
bob_friends = {"Alice", "Charlie", "Frank", "Diana"}

common = alice_friends & bob_friends
print(f"Common friends: {common}")

only_alice = alice_friends - bob_friends
print(f"Only Alice's: {only_alice}")
