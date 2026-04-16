# Homework 4
# Topics: functions, parameters, return values, default arguments, keyword arguments, scope, tuples

# Task 1: Greeting Function
# Write a function called `greet(name, greeting="Hello")` that returns a greeting string.
# Example: greet("Alice") -> "Hello, Alice!"
# Example: greet("Bob", "Good morning") -> "Good morning, Bob!"
# Call the function 3 times with different arguments and print the results.

# Write your code below:


# Task 2: Math Functions
# Write three functions:
# - `circle_area(radius)` that returns the area of a circle (use 3.14159 for pi)
# - `circle_circumference(radius)` that returns the circumference of a circle
# - `circle_info(radius)` that calls both functions above and returns area AND circumference
# Call circle_info() with radius 5 and print both values.

# Write your code below:


# Task 3: List Statistics
# Write a function called `list_stats(numbers)` that takes a list of numbers and returns:
# - the sum
# - the average
# - the smallest number
# - the largest number
# Test it with the list [10, 25, 3, 47, 18, 32, 6]

# Write your code below:


# Task 4: Word Counter
# Write a function called `count_words(sentence)` that takes a sentence string and returns:
# - the number of words
# - the number of characters (excluding spaces)
# - the longest word
# Test it with: "the quick brown fox jumps over the lazy dog"

# Write your code below:


# Task 5: Grade Calculator
# Write a function called `letter_grade(score)` that takes a numeric score and returns a letter grade:
# - 90-100: "A"
# - 80-89: "B"
# - 70-79: "C"
# - 60-69: "D"
# - Below 60: "F"
# Then write a function `class_report(grades)` that takes a list of numeric scores,
# uses letter_grade() for each one, and prints a report like:
# Score: 85 -> Grade: B
# It should also print the class average at the end.
# Test with: [92, 85, 67, 74, 55, 91, 80]

# Write your code below:


# Task 6: Password Generator
# Write a function called `generate_password(length=12, use_digits=True, use_uppercase=True)`.
# The function should build a password by:
# 1. Starting with lowercase letters: "abcdefghijklmnopqrstuvwxyz"
# 2. If use_uppercase is True, also include "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# 3. If use_digits is True, also include "0123456789"
# 4. Use a loop to pick `length` random characters from the combined characters
# Hint: import random and use random.choice()
# Call the function with different settings and print the results:
# - generate_password()
# - generate_password(8)
# - generate_password(16, use_digits=False)

# Write your code below:
