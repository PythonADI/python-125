# Workshop 4 - Multiple Return Values and Tuples

# ==============================
# Tuples - quick intro
# ==============================

# Tuples are like lists, but immutable (cannot be changed)
point = (3, 5)
print(point)         # (3, 5)
print(point[0])      # 3
print(point[1])      # 5

# point[0] = 10      # TypeError: tuples don't support assignment

# Tuple unpacking
x, y = point
print(f"x = {x}, y = {y}")    # x = 3, y = 5


# ==============================
# Returning multiple values
# ==============================

def get_min_max(numbers):
    return min(numbers), max(numbers)

smallest, largest = get_min_max([5, 2, 8, 1, 9])
print(f"Min: {smallest}, Max: {largest}")    # Min: 1, Max: 9


def calculate(a, b):
    add = a + b
    subtract = a - b
    multiply = a * b
    return add, subtract, multiply

s, d, p = calculate(10, 3)
print(f"Sum: {s}, Diff: {d}, Product: {p}")  # Sum: 13, Diff: 7, Product: 30


# ==============================
# Practical example: grade analyzer
# ==============================

def analyze_grades(grades):
    total = sum(grades)
    average = total / len(grades)
    highest = max(grades)
    lowest = min(grades)
    passed = len([g for g in grades if g >= 60])
    return average, highest, lowest, passed

student_grades = [85, 42, 91, 67, 55, 78, 93, 60]

avg, high, low, pass_count = analyze_grades(student_grades)
print(f"Average: {avg:.1f}")
print(f"Highest: {high}")
print(f"Lowest: {low}")
print(f"Passed: {pass_count}/{len(student_grades)}")
