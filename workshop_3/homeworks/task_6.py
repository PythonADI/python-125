sentence = input("Enter sentence: ")
vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for character in sentence.lower():
    if character in vowels:
        vowel_count += 1
    elif character.isalpha():
        consonant_count += 1

print(f"\"{sentence}\" has {consonant_count} consonant and {vowel_count} vowels")