# Workshop 3 - Practical examples

# ==============================
# Building lists with loops
# ==============================

# Collecting even numbers
evens = []
for i in range(1, 21):
    if i % 2 == 0:
        evens.append(i)
print(evens)       # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Filtering a list
scores = [45, 82, 67, 91, 55, 73, 88]
passed = []

for score in scores:
    if score >= 70:
        passed.append(score)

print(f"Passed: {passed}")
print(f"Pass rate: {len(passed)}/{len(scores)}")


# ==============================
# Sum and average
# ==============================

grades = [85, 92, 78, 90, 88]
total = sum(grades)
average = total / len(grades)
print(f"Total: {total}, Average: {average}")


# ==============================
# Finding min/max manually
# ==============================

numbers = [34, 12, 67, 5, 89, 23]
smallest = numbers[0]
largest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

print(f"Smallest: {smallest}, Largest: {largest}")


# ==============================
# Counting occurrences
# ==============================

text = "hello world"
vowels = "aeiou"
vowel_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1

print(f"Vowels in '{text}': {vowel_count}")
