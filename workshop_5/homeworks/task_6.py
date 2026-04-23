# ==============================
# Task 6: Simple translator
# ==============================
# Create a dictionary that maps English words to another language
# (at least 8 words). Write translate(sentence, dictionary) that
# returns the sentence with each known word replaced.
# Unknown words stay unchanged.
#
# Example:
#   translator = {"hello": "bonjour", "cat": "chat", "dog": "chien"}
#   translate("hello my cat and dog", translator)
#   -> "bonjour my chat and chien"

translator = {
    "hello": "გამარჯობა",
    "cat": "კატა",
    "dog": "ძაღლი",
    "how": "როგორ",
    "are": "ხარ",
    "you": "შენ",
    "he": "ის",
    "she": "ის",
    "it": "ის",
    "outside": "გარეთ"
}


sentence = "hello how are you it is a wonderful day outside"

def translate(sentence):
    translated = []
    for word in sentence.split(" "):
        # print(translator[word])
        translated.append(translator.get(word, word))

    return " ".join(translated)


print(translate(sentence))
