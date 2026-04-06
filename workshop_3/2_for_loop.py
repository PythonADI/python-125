# Workshop 3 - for loop

# ==============================
# Looping through a list
# ==============================

colors = ["red", "green", "blue"]

for color in colors:
    print(f"Color: {color}")


# ==============================
# range() function
# ==============================

for i in range(5):           # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 6):        # 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):    # 0, 2, 4, 6, 8 (step of 2)
    print(i)


# ==============================
# Looping with index
# ==============================

students = ["Alice", "Bob", "Charlie"]

# Using range + len
for i in range(len(students)):
    print(f"{i + 1}. {students[i]}")

# Using enumerate (preferred)
for index, student in enumerate(students):
    print(f"{index + 1}. {student}")
