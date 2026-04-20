# Workshop 5 - Nested Dictionaries

# ==============================
# Dictionary of dictionaries
# ==============================

students = {
    "alice": {
        "age": 20,
        "major": "Computer Science",
        "grades": [90, 85, 92],
    },
    "bob": {
        "age": 22,
        "major": "Mathematics",
        "grades": [78, 82, 88],
    },
    "charlie": {
        "age": 21,
        "major": "Physics",
        "grades": [95, 91, 89],
    },
}

# Access nested values
print(students["alice"]["major"])         # Computer Science
print(students["bob"]["grades"][0])       # 78


# ==============================
# Iterating through nested dicts
# ==============================

for name, info in students.items():
    average = sum(info["grades"]) / len(info["grades"])
    print(f"{name.title()} ({info['major']}): avg {average:.1f}")


# ==============================
# Adding a new student
# ==============================

students["diana"] = {
    "age": 23,
    "major": "Biology",
    "grades": [88, 90, 85],
}

print(f"Total students: {len(students)}")


# ==============================
# List of dictionaries
# ==============================

products = [
    {"name": "Laptop", "price": 1200, "stock": 5},
    {"name": "Mouse", "price": 25, "stock": 50},
    {"name": "Keyboard", "price": 80, "stock": 12},
    {"name": "Monitor", "price": 300, "stock": 8},
]
# print(products[0])

# Total inventory value
total_value = 0
for product in products:
    total_value += product["price"] * product["stock"]
print(f"Total inventory value: ${total_value}")

# Find products with low stock
low_stock = []
for product in products:
    if product["stock"] < 10:
        low_stock.append(product["name"])
print(f"Low stock: {low_stock}")


# ==============================
# Most expensive product
# ==============================

most_expensive = products[0]
for product in products:
    if product["price"] > most_expensive["price"]:
        most_expensive = product

print(f"Most expensive: {most_expensive['name']} (${most_expensive['price']})")
