"""
Write a function called `count_words(sentence)` that takes a sentence string and returns:
- The number of words
- The number of characters (excluding spaces)
- The longest word
"""

def count_words(sentence):
    # if sentence == "":
    #     counter = 0
    # else:
    #     counter = 1
    #
    # for char in sentence:
    #     if char == " ":
    #         counter += 1
    # return counter

    return len(sentence.split())

def count_characters(sentence):
    counter = 0
    for char in sentence:
        if char != " ":
            counter += 1

    return counter


def longest_word(sentence):
    words = sentence.split(" ")
    lw = words[0]

    for word in words:
        if len(lw) < len(word):
            lw = word

    return lw

sentence = "This is a sentence"



print(count_words(sentence))
print(count_characters(sentence))
print(longest_word(sentence))
print(count_words("This is even bigger sentence"))
# print(len(sentence))
