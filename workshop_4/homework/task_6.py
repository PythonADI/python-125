"""
Write a function `generate_password(length=12, use_digits=True, use_uppercase=True)` that:
1. Starts with lowercase letters: `"abcdefghijklmnopqrstuvwxyz"`
2. Adds uppercase letters if `use_uppercase` is True
3. Adds digits if `use_digits` is True
4. Uses a loop to pick `length` random characters


CHALLENGE:
write a code that checks output of function calls for different inputs
"""
import random
import string


def generate_password(length=12, use_digits=True, use_uppercase=True):
    available_characters = string.ascii_lowercase

    password = random.choice(string.ascii_lowercase)

    if use_uppercase:
        available_characters += string.ascii_uppercase
    if use_digits:
        available_characters += string.digits

    for i in range(length):
        password += random.choice(available_characters)

    return password


print(generate_password(30))
print(generate_password(100))
print(generate_password(100, False, False))
print(generate_password(100, True, False))
print(generate_password(100, False, True))


# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.ascii_letters)
# print(string.digits)

