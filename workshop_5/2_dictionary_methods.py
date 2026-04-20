# Workshop 5 - Dictionary Methods and Iteration

scores = {"math": 90, "science": 85, "history": 78, "english": 92}


# ==============================
# .keys(), .values(), .items()
# ==============================

print(scores.keys())     # dict_keys(['math', 'science', 'history', 'english'])
print(scores.values())   # dict_values([90, 85, 78, 92])
print(scores.items())    # dict_items([('math', 90), ('science', 85), ...])


# ==============================
# Iterating over a dictionary
# ==============================

# Iterating directly goes over keys
for subject in scores:
    print(subject)

# Iterate over values
for score in scores.values():
    print(score)

# Iterate over key-value pairs
for subject, score in scores.items():
    print(f"{subject}: {score}")


# ==============================
# Useful operations
# ==============================

# Average score
total = sum(scores.values())
average = total / len(scores)
print(f"Average: {average:.1f}")     # Average: 86.2

# Highest score
best_subject = max(scores, key=scores.get)
print(f"Best subject: {best_subject} ({scores[best_subject]})")

# Lowest score
worst_subject = min(scores, key=scores.get)
print(f"Worst subject: {worst_subject} ({scores[worst_subject]})")


# ==============================
# .update() — merge dictionaries
# ==============================

new_scores = {"art": 88, "math": 95}
scores.update(new_scores)
print(scores)
# {'math': 95, 'science': 85, 'history': 78, 'english': 92, 'art': 88}


# ==============================
# .clear() and copying
# ==============================

backup = scores.copy()   # shallow copy
scores.clear()
print(scores)   # {}
print(backup)   # still has all scores


# ==============================
# Counting with dictionaries
# ==============================

sentence = "the quick brown fox jumps over the lazy dog the fox is quick"
word_count = {}

for word in sentence.split(" "):
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
# {'the': 3, 'quick': 2, 'brown': 1, 'fox': 2, ...}


# A cleaner version using .get()
word_count2 = {}
for word in sentence.split():
    word_count2[word] = word_count2.get(word, 0) + 1

print(word_count2)
