# Workshop 5 - Practical Examples

# ==============================
# Example 1: Phone book
# ==============================

def add_contact(phonebook, name, number):
    phonebook[name.lower()] = number
    return phonebook

def find_contact(phonebook, name):
    return phonebook.get(name.lower(), "Not found")

def remove_contact(phonebook, name):
    if name.lower() in phonebook:
        del phonebook[name.lower()]
        return True
    return False

def show_phonebook(phonebook):
    if not phonebook:
        print("Phonebook is empty")
        return
    print("Phonebook:")
    for name, number in sorted(phonebook.items()):
        print(f"  {name.title()}: {number}")

book = {}
book = add_contact(book, "Alice", "555-1234")
book = add_contact(book, "Bob", "555-5678")
book = add_contact(book, "Charlie", "555-9012")

show_phonebook(book)
print(find_contact(book, "Alice"))
print(find_contact(book, "Dave"))
remove_contact(book, "Bob")
show_phonebook(book)


# ==============================
# Example 2: Word frequency analyzer
# ==============================

def word_frequency(text):
    text = text.lower()
    # Remove common punctuation
    for char in ".,!?;:":
        text = text.replace(char, "")

    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts

def top_words(counts, n=3):
    # Sort by count, descending
    sorted_words = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_words[:n]

article = """
Python is great. Python is easy to learn.
Python is powerful, and Python is popular.
Many developers love Python!
"""

counts = word_frequency(article)
print(counts)
print(f"Top 3: {top_words(counts, 3)}")


# ==============================
# Example 3: Inventory management
# ==============================

inventory = {
    "apple": {"price": 0.50, "quantity": 100},
    "bread": {"price": 2.00, "quantity": 20},
    "milk": {"price": 3.50, "quantity": 15},
    "cheese": {"price": 5.00, "quantity": 8},
}

def restock(inventory, item, amount):
    if item in inventory:
        inventory[item]["quantity"] += amount
    else:
        print(f"{item} not in inventory")

def sell(inventory, item, amount):
    if item not in inventory:
        return f"{item} not available"
    if inventory[item]["quantity"] < amount:
        return f"Not enough {item} in stock"
    inventory[item]["quantity"] -= amount
    total = amount * inventory[item]["price"]
    return f"Sold {amount} {item}(s) for ${total:.2f}"

def inventory_value(inventory):
    total = 0
    for item in inventory.values():
        total += item["price"] * item["quantity"]
    return total

print(sell(inventory, "bread", 5))
print(sell(inventory, "cheese", 10))   # not enough
restock(inventory, "cheese", 20)
print(sell(inventory, "cheese", 10))
print(f"Total inventory value: ${inventory_value(inventory):.2f}")
print(inventory)


# ==============================
# Example 4: Removing duplicate users
# ==============================

signups = [
    "alice@mail.com",
    "bob@mail.com",
    "Alice@mail.com",
    "carol@mail.com",
    "bob@mail.com",
    "DAVE@mail.com",
]

def unique_emails(emails):
    # Normalize to lowercase, then de-duplicate with a set
    normalized = {email.lower() for email in emails}
    return sorted(normalized)

print(unique_emails(signups))
# ['alice@mail.com', 'bob@mail.com', 'carol@mail.com', 'dave@mail.com']


# ==============================
# Example 5: Group students by grade
# ==============================

students = [
    ("Alice", 92),
    ("Bob", 75),
    ("Charlie", 88),
    ("Diana", 61),
    ("Eve", 78),
    ("Frank", 95),
    ("Grace", 58),
]

def group_by_grade(students):
    groups = {"A": [], "B": [], "C": [], "D": [], "F": []}
    for name, score in students:
        if score >= 90:
            groups["A"].append(name)
        elif score >= 80:
            groups["B"].append(name)
        elif score >= 70:
            groups["C"].append(name)
        elif score >= 60:
            groups["D"].append(name)
        else:
            groups["F"].append(name)
    return groups

grouped = group_by_grade(students)
for grade, names in grouped.items():
    print(f"{grade}: {names}")
