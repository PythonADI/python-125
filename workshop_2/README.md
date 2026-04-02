# Workshop 2 - Homework

## Topics
- `input()` function and type conversion (`int()`, `float()`)
- String methods: `upper()`, `lower()`, `strip()`, `replace()`, `split()`, `join()`, `count()`, `startswith()`, `endswith()`, `title()`, `capitalize()`
- String indexing and slicing
- `in` operator for strings
- `len()` function
- Conditionals: `if`, `elif`, `else`
- Logical operators: `and`, `or`, `not`

## Tasks

### Task 1: User Greeting
Ask the user for their name using `input()`. Print the name in uppercase, lowercase, and title case.

### Task 2: String Operations
Create a variable `sentence = "  the quick brown fox jumps over the lazy dog  "`.
- Print the sentence stripped of extra spaces
- Print the number of times the letter "o" appears
- Replace "fox" with "cat" and print the result
- Print the first 3 words using `split()` and slicing

### Task 3: Age Checker
Ask the user for their age (convert to `int`). Print a message based on the age:
- Under 13: "You are a child."
- 13 to 17: "You are a teenager."
- 18 to 64: "You are an adult."
- 65 and above: "You are a senior."
- Negative number: "Invalid age!"

### Task 4: Login System
Ask the user for a username and password.
- If username is "admin" and password is "secret": print "Welcome, Admin!"
- If username is "admin" but wrong password: print "Incorrect password."
- If username is anything else: print "User not found."

### Task 5: Ticket Price Calculator
Ask the user for their age (`int`) and whether they are a student (`yes`/`no`).
Calculate the ticket price:
- Children (under 12): $5
- Students (12 and above): $8
- Adults (18-64, not student): $15
- Seniors (65+): $10
Print the ticket price.

## How to Submit
1. Complete all tasks in `homework.py`
2. Push your work to your GitHub repository
3. Share the repository link with the instructor

## How to Run
```bash
python homework.py
```
