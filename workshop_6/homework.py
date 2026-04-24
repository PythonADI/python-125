


# Workshop 6 - Homework
# Topics: algorithmic thinking, designing an algorithm before writing code
#
# HOW TO DO EACH TASK
# -------------------
# For every task below, follow these four steps IN ORDER:
#
#   1. UNDERSTAND - Read the problem. In a comment, restate it in your own
#                   words. List the inputs, the output, and at least one
#                   tricky case (empty list, duplicates, negatives, etc.).
#
#   2. PLAN       - Write the algorithm as pseudocode in comments. Plain
#                   English, step by step. Do NOT write Python yet.
#                   Example:
#                       # set smallest to the first number
#                       # for each remaining number:
#                       #     if it is smaller than smallest, update smallest
#                       # return smallest
#
#   3. CODE       - Translate your pseudocode into Python, line by line.
#
#   4. TEST       - Run your function on the given test cases AND at least
#                   one edge case of your own. Print each result.
#
# Rule of the workshop: pseudocode first, Python second. If you start typing
# Python before you have written the plan in comments, stop and go back.


# ==============================
# Task 1: Find the smallest number
# ==============================
# Write a function smallest(numbers) that returns the smallest number in a
# list. You are NOT allowed to use min().
#
# Test cases:
#   smallest([4, 2, 9, 1, 7])   -> 1
#   smallest([-3, -10, -1, -7]) -> -10
#   smallest([5])               -> 5

# 1. UNDERSTAND:


# 2. PLAN (pseudocode):


# 3. CODE:


# 4. TEST:




# ==============================
# Task 2: Count even numbers
# ==============================
# Write a function count_evens(numbers) that returns how many numbers in the
# list are even.
#
# Test cases:
#   count_evens([1, 2, 3, 4, 5, 6]) -> 3
#   count_evens([1, 3, 5, 7])       -> 0
#   count_evens([])                 -> 0

# 1. UNDERSTAND:


# 2. PLAN (pseudocode):


# 3. CODE:


# 4. TEST:




# ==============================
# Task 3: Reverse a list
# ==============================
# Write a function reverse_list(items) that returns a new list with the
# elements in reverse order. You are NOT allowed to use .reverse() or the
# slicing trick [::-1].
#
# Test cases:
#   reverse_list([1, 2, 3, 4]) -> [4, 3, 2, 1]
#   reverse_list(["a", "b"])   -> ["b", "a"]
#   reverse_list([])           -> []

# 1. UNDERSTAND:


# 2. PLAN (pseudocode):


# 3. CODE:


# 4. TEST:




# ==============================
# Task 4: Does the list contain a value?
# ==============================
# Write a function contains(numbers, target) that returns True if `target`
# appears anywhere in the list, and False otherwise. You are NOT allowed to
# use the `in` keyword for this task - the point is to design the search
# yourself.
#
# Test cases:
#   contains([3, 7, 2, 8], 7) -> True
#   contains([3, 7, 2, 8], 5) -> False
#   contains([], 1)           -> False

# 1. UNDERSTAND:


# 2. PLAN (pseudocode):


# 3. CODE:


# 4. TEST:




# ==============================
# Task 5: Count a letter in a string
# ==============================
# Write a function count_letter(text, letter) that returns how many times
# `letter` appears in `text`. Treat uppercase and lowercase as the same
# letter (so "A" and "a" both count).
#
# Test cases:
#   count_letter("banana", "a")      -> 3
#   count_letter("Mississippi", "s") -> 4
#   count_letter("Hello", "z")       -> 0

# 1. UNDERSTAND:


# 2. PLAN (pseudocode):


# 3. CODE:


# 4. TEST:




# ==============================
# Task 6: Remove duplicates, keep order
# ==============================
# Write a function remove_duplicates(items) that returns a new list with
# every duplicate removed, while preserving the order of the first time
# each item appeared.
#
# Hint: using set(items) alone does NOT work, because sets do not preserve
# order. Design your own algorithm.
#
# Test cases:
#   remove_duplicates([1, 2, 2, 3, 1, 4]) -> [1, 2, 3, 4]
#   remove_duplicates(["a", "b", "a"])    -> ["a", "b"]
#   remove_duplicates([])                 -> []

# 1. UNDERSTAND:


# 2. PLAN (pseudocode):


# 3. CODE:


# 4. TEST: