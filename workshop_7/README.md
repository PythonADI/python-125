# Workshop 7 - Classes (Object-Oriented Programming)

## Topics
- What is a class? Classes vs. instances (objects)
- Defining a class with `__init__` and the role of `self`
- Instance attributes vs. class attributes
- Methods: changing state, returning values, calling other methods
- Inheritance, `super()`, and method overriding
- Dunder methods: `__init__`, `__str__`, `__repr__`, `__eq__`, `__len__`
- Modeling real things with classes (accounts, products, characters, etc.)

## Files in this workshop
- `1_classes_basics.py` - your first class, attributes, instances
- `2_attributes_and_self.py` - instance vs. class attributes, what `self` really is
- `3_methods.py` - writing methods, returning values, methods calling methods
- `4_inheritance.py` - subclasses, `super()`, overriding
- `5_dunder_methods.py` - `__str__`, `__repr__`, `__eq__`, `__len__`
- `6_practical_examples.py` - bank, shopping cart, library, game characters
- `7_why_classes.py` - the same problem solved without classes and with classes, side by side

Read the files in order. Run each one to see the output.

## Tasks

### Task 1: `Person` class
Create a class `Person` with attributes `name` and `age`. Add a method `greet()` that prints `"Hi, I'm <name> and I'm <age> years old."`. Create three different people and call `greet()` on each.

### Task 2: `Rectangle` class
Create a class `Rectangle` with attributes `width` and `height`. Add methods:
- `area()` - returns the area
- `perimeter()` - returns the perimeter
- `is_square()` - returns `True` if it's a square

Test with at least one rectangle and one square.

### Task 3: `BankAccount` class
Create a class `BankAccount` with attributes `owner` and `balance` (default `0`). Add methods:
- `deposit(amount)` - adds to the balance, refuses negative amounts
- `withdraw(amount)` - subtracts from the balance, refuses if not enough funds
- `__str__()` - returns `"Account(<owner>): $<balance>"`

Open one account, deposit, withdraw (including a withdrawal that should fail), and `print(account)`.

### Task 4: Inheritance - `Animal`, `Dog`, `Cat`
- `Animal` has `name` and a method `speak()` that prints `"<name> makes a sound."`
- `Dog` inherits from `Animal` and overrides `speak()` to print `"<name> says Woof!"`
- `Cat` inherits from `Animal` and overrides `speak()` to print `"<name> says Meow!"`

Put one of each into a list and loop over it calling `speak()` on every animal.

### Task 5: `Book` class with `__eq__`
Create a class `Book` with attributes `title`, `author`, `pages`. Implement:
- `__repr__` that returns `Book(<title>, <author>, <pages>p)`
- `__eq__` so two books are equal when they have the same title AND author (pages may differ - it's a different edition)
- `__len__` that returns the page count

Create three books (two equal under your rule, one different) and verify `==`, `len()`, and `print()` work as expected.

### Task 6: `Student` and `Course`
- `Student` has `name` and a list `grades` (start empty). Add `add_grade(grade)` and `average()`.
- `Course` has `name` and a list of `students`. Add `enroll(student)`, `class_average()` (average of every student's average), and `top_student()` (returns the student with the highest average).

Enroll at least 3 students, give each a few grades, and print the class average and the top student.

## How to Submit
1. Complete all tasks in `homework.py`.
2. Push your work to your GitHub repository.
3. Share the repository link with the instructor.

## How to Run
```bash
python homework.py
```
