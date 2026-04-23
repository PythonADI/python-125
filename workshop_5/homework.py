# Workshop 5 - Homework
# Complete each task below. Test your code by running this file.


# ==============================
# Task 1: Student grades dictionary
# ==============================
# Create a dictionary called `grades` with at least 5 students
# (name -> numeric score). Then:
#   - Print each student and their grade
#   - Print the class average
#   - Print the highest-scoring student

grades = {
    "Nika": 88,
    "Giorgi": 57,
    "Levan": 97,
    "Mari": 90,
    "Xaiver": 78
}

# total = 0
student = {
    "name": "",
    "grade": 0
}
for name, grade in grades.items():
    print(name, grade)
    # total += grade
    if student["grade"] < grade:
        student["name"] = name
        student["grade"] = grade

average = sum(grades.values()) / len(grades)
print(average)
print(student["name"])

# print(total / len(grades))





# ==============================
# Task 2: Word counter function
# ==============================
# Write count_letters(text) that returns a dictionary mapping
# each letter to how many times it appears in `text`.
# Ignore spaces and treat upper/lowercase as the same letter.
# Test with: "Hello World"



# ==============================
# Task 3: Merge two shopping lists
# ==============================
# Two people made shopping lists with item -> quantity.
# Write merge_lists(list1, list2) that returns a combined dictionary
# where quantities are summed for items that appear in both.
#
# list1 = {"milk": 2, "bread": 1, "eggs": 12}
# list2 = {"bread": 2, "cheese": 1, "milk": 1}
# Expected: {"milk": 3, "bread": 3, "eggs": 12, "cheese": 1}



# ==============================
# Task 4: Contact manager
# ==============================
# Build a small contact manager where each contact is a dictionary
# with keys: name, phone, email.
# Store them all in a list called `contacts`. Write these functions:
#   - add_contact(contacts, name, phone, email)
#   - find_by_name(contacts, name) -> returns the contact dict or None
#   - all_emails(contacts) -> returns a list of every email address
#
# Add 3 contacts and test each function.



# ==============================
# Task 5: Find unique and common items
# ==============================
# Two classrooms submitted their favorite movies.
# Using sets, find:
#   - Movies liked by BOTH classrooms
#   - Movies liked by only ONE of them
#   - The total number of distinct movies
#
# class_a = ["Inception", "Matrix", "Interstellar", "Joker", "Matrix"]
# class_b = ["Matrix", "Titanic", "Joker", "Avatar", "Titanic"]



# ==============================
# Task 6: Simple translator
# ==============================
# Create a dictionary that maps English words to another language
# (at least 8 words). Write translate(sentence, dictionary) that
# returns the sentence with each known word replaced.
# Unknown words stay unchanged.
#
# Example:
#   translator = {"hello": "bonjour", "cat": "chat", "dog": "chien"}
#   translate("hello my cat and dog", translator)
#   -> "bonjour my chat and chien"
