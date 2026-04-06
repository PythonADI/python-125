# Workshop 3 - Homework

## Topics
- Lists: creating, indexing, slicing, modifying
- List methods: `append()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`, `index()`, `count()`
- Built-in functions: `len()`, `min()`, `max()`, `sum()`
- `in` operator for lists
- `for` loop, `range()`, `enumerate()`
- `while` loop
- `break` and `continue`
- Nested loops
- Building and filtering lists with loops

## Tasks

### Task 1: List Operations
Create a list of 5 favorite movies. Then:
1. Print the first and last movie
2. Add a new movie to the end
3. Insert a movie at index 2
4. Remove one movie by name
5. Print the final list and its length

### Task 2: Sum and Average
Ask the user to enter 5 numbers (one at a time using a `for` loop and `input()`).
Store them in a list, then print:
- The list of numbers
- The sum
- The average
- The largest and smallest number

### Task 3: Even and Odd
Using a `for` loop and `range(1, 21)`, separate numbers into two lists: `evens` and `odds`.
Print both lists.

### Task 4: Password Checker
Using a `while` loop, ask the user to enter a password.
- If the password is "python123", print "Access granted!" and stop.
- If wrong, print "Wrong password, try again."
- After 3 failed attempts, print "Account locked!" and stop.
(Hint: use a counter variable and `break`)

### Task 5: Multiplication Table
Ask the user for a number. Using a `for` loop, print the multiplication table for that number from 1 to 10.
Example for number 4:
```
4 x 1 = 4
4 x 2 = 8
...
4 x 10 = 40
```

### Task 6: Word Analyzer
Ask the user to enter a sentence. Using a loop:
1. Count the number of vowels (a, e, i, o, u)
2. Count the number of consonants (letters that are not vowels)
3. Print the results
(Hint: use `.lower()` and check `if char.isalpha()` before counting)

## How to Submit
1. Complete all tasks in `homework.py`
2. Push your work to your GitHub repository
3. Share the repository link with the instructor

## How to Run
```bash
python homework.py
```
