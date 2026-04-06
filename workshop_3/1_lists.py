# Workshop 3 - Lists

# ==============================
# Creating lists
# ==============================

fruits = ["apple", "banana", "cherry", "mango"]
numbers = [10, 20, 30, 40, 50]
mixed = ["hello", 42, 3.14, True]

print(fruits)        # ['apple', 'banana', 'cherry', 'mango']
print(len(fruits))   # 4

# Accessing elements (indexing)
print(fruits[0])     # apple
print(fruits[-1])    # mango
print(fruits[1:3])   # ['banana', 'cherry']

# Modifying lists
fruits[1] = "blueberry"
print(fruits)        # ['apple', 'blueberry', 'cherry', 'mango']


# ==============================
# Adding elements
# ==============================

fruits.append("orange")          # adds to the end
print(fruits)

fruits.insert(1, "grape")        # inserts at index 1
print(fruits)


# ==============================
# Removing elements
# ==============================

fruits.remove("cherry")          # removes by value
print(fruits)

removed = fruits.pop()           # removes and returns last element
print(f"Removed: {removed}")
print(fruits)

removed = fruits.pop(0)          # removes and returns element at index
print(f"Removed: {removed}")
print(fruits)


# ==============================
# Other useful list methods
# ==============================

numbers = [5, 2, 8, 1, 9, 3]
numbers.sort()                   # sorts in place
print(numbers)                   # [1, 2, 3, 5, 8, 9]

numbers.reverse()                # reverses in place
print(numbers)                   # [9, 8, 5, 3, 2, 1]

print(min(numbers))              # 1
print(max(numbers))              # 9
print(sum(numbers))              # 28

# Checking if element exists
print(5 in numbers)              # True
print(100 in numbers)            # False

print(numbers.index(5))          # index of first occurrence
print(numbers.count(5))          # how many times 5 appears
