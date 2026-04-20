# Workshop 5 - Homework

## Topics
- Dictionaries: creating, accessing, updating, removing
- Dictionary methods: `.get()`, `.keys()`, `.values()`, `.items()`, `.update()`
- Iterating through dictionaries
- Nested dictionaries and lists of dictionaries
- Sets: unique collections and set operations (`|`, `&`, `-`, `^`)
- Using dictionaries and sets to solve practical problems

## Tasks

### Task 1: Student Grades Dictionary
Create a dictionary `grades` with at least 5 students (name -> numeric score). Then:
- Print each student and their grade
- Print the class average
- Print the highest-scoring student

### Task 2: Letter Counter
Write a function `count_letters(text)` that returns a dictionary mapping each letter to how many times it appears in `text`. Ignore spaces and treat upper/lowercase as the same letter.

Test with: `"Hello World"`

### Task 3: Merge Shopping Lists
Two people made shopping lists mapping item -> quantity. Write `merge_lists(list1, list2)` that returns a combined dictionary where quantities are summed for items that appear in both.

```python
list1 = {"milk": 2, "bread": 1, "eggs": 12}
list2 = {"bread": 2, "cheese": 1, "milk": 1}
# Expected: {"milk": 3, "bread": 3, "eggs": 12, "cheese": 1}
```

### Task 4: Contact Manager
Build a small contact manager where each contact is a dictionary with keys: `name`, `phone`, `email`. Store them all in a list called `contacts`. Write these functions:
- `add_contact(contacts, name, phone, email)`
- `find_by_name(contacts, name)` - returns the contact dict or `None`
- `all_emails(contacts)` - returns a list of every email address

Add 3 contacts and test each function.

### Task 5: Unique and Common Items (Sets)
Two classrooms submitted their favorite movies. Using sets, find:
- Movies liked by BOTH classrooms
- Movies liked by only ONE of them
- The total number of distinct movies

```python
class_a = ["Inception", "Matrix", "Interstellar", "Joker", "Matrix"]
class_b = ["Matrix", "Titanic", "Joker", "Avatar", "Titanic"]
```

### Task 6: Simple Translator
Create a dictionary that maps English words to another language (at least 8 words). Write `translate(sentence, dictionary)` that returns the sentence with each known word replaced. Unknown words stay unchanged.

```python
translator = {"hello": "bonjour", "cat": "chat", "dog": "chien"}
translate("hello my cat and dog", translator)
# -> "bonjour my chat and chien"
```

## How to Submit
1. Complete all tasks in `homework.py`
2. Push your work to your GitHub repository
3. Share the repository link with the instructor

## How to Run
```bash
python homework.py
```
