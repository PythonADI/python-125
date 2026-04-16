# Workshop 4 - Homework

## Topics
- Defining functions with `def`
- Parameters and arguments
- Return values (`return` vs `print()`)
- Default parameter values
- Keyword arguments
- Returning multiple values (tuples)
- Variable scope (local vs global)
- Combining functions with lists and loops

## Tasks

### Task 1: Greeting Function
Write a function called `greet(name, greeting="Hello")` that returns a greeting string.
- `greet("Alice")` should return `"Hello, Alice!"`
- `greet("Bob", "Good morning")` should return `"Good morning, Bob!"`
- Call the function 3 times with different arguments and print the results.

### Task 2: Math Functions
Write three functions:
- `circle_area(radius)` - returns the area of a circle (use 3.14159 for pi)
- `circle_circumference(radius)` - returns the circumference
- `circle_info(radius)` - calls both functions above and returns area AND circumference

Call `circle_info()` with radius 5 and print both values.

### Task 3: List Statistics
Write a function called `list_stats(numbers)` that takes a list of numbers and returns:
- The sum
- The average
- The smallest number
- The largest number

Test it with: `[10, 25, 3, 47, 18, 32, 6]`

### Task 4: Word Counter
Write a function called `count_words(sentence)` that takes a sentence string and returns:
- The number of words
- The number of characters (excluding spaces)
- The longest word

Test it with: `"the quick brown fox jumps over the lazy dog"`

### Task 5: Grade Calculator
Write a function `letter_grade(score)` that converts a numeric score to a letter grade:
- 90-100: "A"
- 80-89: "B"
- 70-79: "C"
- 60-69: "D"
- Below 60: "F"

Then write `class_report(grades)` that takes a list of numeric scores, uses `letter_grade()` for each, and prints a report:
```
Score: 85 -> Grade: B
Score: 92 -> Grade: A
...
Class average: 77.7
```
Test with: `[92, 85, 67, 74, 55, 91, 80]`

### Task 6: Password Generator
Write a function `generate_password(length=12, use_digits=True, use_uppercase=True)` that:
1. Starts with lowercase letters: `"abcdefghijklmnopqrstuvwxyz"`
2. Adds uppercase letters if `use_uppercase` is True
3. Adds digits if `use_digits` is True
4. Uses a loop to pick `length` random characters

(Hint: `import random` and use `random.choice()`)

Test with different settings:
- `generate_password()`
- `generate_password(8)`
- `generate_password(16, use_digits=False)`

## How to Submit
1. Complete all tasks in `homework.py`
2. Push your work to your GitHub repository
3. Share the repository link with the instructor

## How to Run
```bash
python homework.py
```
