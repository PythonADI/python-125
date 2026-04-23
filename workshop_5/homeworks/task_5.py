# ==============================
# Task 5: Find unique and common items
# ==============================
# Two classrooms submitted their favorite movies.
# Using sets, find:
#   - Movies liked by BOTH classrooms
#   - Movies liked by only ONE of them
#   - The total number of distinct movies
#
class_a = ["Inception", "Matrix", "Interstellar", "Joker", "Matrix"]
class_b = ["Matrix", "Titanic", "Joker", "Avatar", "Titanic"]

class_a = set(class_a)
class_b = set(class_b)
print(class_a & class_b)
print(class_a.symmetric_difference(class_b))
print(class_a | class_b)


