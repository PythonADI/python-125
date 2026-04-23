# ==============================
# Task 2: Word counter function
# ==============================
# Write count_letters(text) that returns a dictionary mapping
# each letter to how many times it appears in `text`.
# Ignore spaces and treat upper/lowercase as the same letter.
# Test with: "Hello World"

text = "Hello World"

"""
1. შექვმნათ მეხსიერება სადაც დავიმახსოვრებთ რამდენჯერ გამეორდა თითოეული ასო (repetition)
h: 1
e: 1
l: 2

2. ავიღოთ თითოეული (ch) სიმბოლო text -დან 
3. თუ ch არ არის ალფაბეტური, მაშინ გადადი შემდეგ სიმბოლოზე
4. მოვძებნოთ ეს სიმბოლო (case-insensitive) repetition ცხრილში და გავზარდოთ მისი მნიშვნელობა 1-ით
5. თუ ეს სიმბოლო არ წერია ცხილში მაშინ დაამატე და მისი მნიშვნელობა იყოს 1
"""


"""
repetition = {}
for ch in text:
    if ch is not alphabetical:
        continue
    if ch not in repetition:
        repetition[ch] = 1
    else:
        repetition[ch] += 1
"""

def count_text(text):
    repetition = {}
    for ch in text.lower():
        if not ch.isalpha():
            continue
        if ch not in repetition:
            repetition[ch] = 1
        else:
            repetition[ch] += 1

    return repetition
