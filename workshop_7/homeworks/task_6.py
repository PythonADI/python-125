import random

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        return sum(self.grades) / len(self.grades)
        # total = 0
        # for grade in self.grades:
        #     total += grade
        #
        # return total / len(self.grades)

    def __repr__(self):
        return self.name


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def enroll(self, student):
        self.students.append(student)

    def class_average(self):
        total_average = 0
        for student in self.students:
            total_average += student.average()

        return total_average / len(self.students)


    def top_student(self):
        top_student = self.students[0]

        for student in self.students:
            if student.average() > top_student.average():
                top_student = student

        return top_student



course = Course("Python")

course.enroll(Student("Nick"))
course.enroll(Student("Valery"))
course.enroll(Student("Marry"))

for student in course.students:
    for _ in range(10):
        student.add_grade(random.randint(51, 100))

for student in course.students:
    print(student, student.average())
print(course.class_average())
print(course.top_student())
