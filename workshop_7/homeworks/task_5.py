class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.pages}p)"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __gt__(self, other):
        return self.pages > other.pages

    def __ge__(self, other):
        return self.pages >= other.pages

    def __len__(self):
        return self.pages


book_1 = Book("Shelock Holmes", "Arthur Conan Doyle", 300)
book_2 = Book("Shelock Holmes", "Arthur Conan Doyle", 301)
book_3 = Book("Train", "Viktor Pelevin", 200)
print(book_1)
print(book_1 == book_2)
print(book_1 == book_3)
print(book_1 != book_2)
print(f"{book_1 > book_2 = }")
print(f"{book_1 > book_2 = }")
print(f"{book_1 <= book_2 = }")
print(f"{book_1 >= book_2 = }")
print(len(book_1))
print(len(book_2))
