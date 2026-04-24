# Workshop 6 - Homework

## Topic
Algorithmic thinking: designing an algorithm **before** writing code.

## The Four Steps
For every task in this homework you MUST follow these steps, in order:

1. **Understand** - Restate the problem in your own words. Write down the inputs, the output, and at least one tricky case (empty list, duplicates, negatives, etc.).
2. **Plan** - Write the algorithm as pseudocode in comments. Plain English, step by step. Do **not** write Python yet.
3. **Code** - Translate your pseudocode into Python, line by line.
4. **Test** - Run your function on the given test cases and at least one edge case of your own.

> Rule of the workshop: **pseudocode first, Python second.** If you start typing Python before the plan is in comments, stop and go back.

## Tasks

### Task 1: Find the smallest number
Write `smallest(numbers)` that returns the smallest number in a list. You may **not** use `min()`.
```
smallest([4, 2, 9, 1, 7])   -> 1
smallest([-3, -10, -1, -7]) -> -10
smallest([5])               -> 5
```

### Task 2: Count even numbers
Write `count_evens(numbers)` that returns how many numbers in the list are even.
```
count_evens([1, 2, 3, 4, 5, 6]) -> 3
count_evens([1, 3, 5, 7])       -> 0
count_evens([])                 -> 0
```

### Task 3: Reverse a list
Write `reverse_list(items)` that returns a new list with the elements in reverse order. You may **not** use `.reverse()` or `[::-1]`.
```
reverse_list([1, 2, 3, 4]) -> [4, 3, 2, 1]
reverse_list(["a", "b"])   -> ["b", "a"]
reverse_list([])           -> []
```

### Task 4: Does the list contain a value?
Write `contains(numbers, target)` that returns `True` if `target` appears in the list, else `False`. You may **not** use the `in` keyword - design the search yourself.
```
contains([3, 7, 2, 8], 7) -> True
contains([3, 7, 2, 8], 5) -> False
contains([], 1)           -> False
```

### Task 5: Count a letter in a string
Write `count_letter(text, letter)` that returns how many times `letter` appears in `text`. Treat uppercase and lowercase as the same letter.
```
count_letter("banana", "a")      -> 3
count_letter("Mississippi", "s") -> 4
count_letter("Hello", "z")       -> 0
```

### Task 6: Remove duplicates, keep order
Write `remove_duplicates(items)` that returns a new list with every duplicate removed, while keeping the order of the first time each item appeared.

Hint: `set(items)` alone does not work because sets do not preserve order.
```
remove_duplicates([1, 2, 2, 3, 1, 4]) -> [1, 2, 3, 4]
remove_duplicates(["a", "b", "a"])    -> ["a", "b"]
remove_duplicates([])                 -> []
```

## How to Submit
1. Complete all tasks in `homework.py`.
2. Each task must show all four steps (Understand, Plan, Code, Test) in comments.
3. Push your work to your GitHub repository.
4. Share the repository link with the instructor.

## How to Run
```bash
python homework.py
```
