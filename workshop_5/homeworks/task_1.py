

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
