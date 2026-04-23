# Workshop 6 — Algorithmic Thinking & Basic Algorithms

## Context

Python-125 is an introductory Python course. Workshops 1–5 have covered:

1. Variables and types
2. Conditionals and strings
3. Lists and loops
4. Functions
5. Dictionaries and sets

Workshop 6 is the natural next step: teaching students how to **think through a problem** before writing code, using algorithms they can build entirely with the tools from Workshops 1–5.

## Goal

Teach students the skill of designing an algorithm — not just memorizing a handful of classic ones. By the end of Workshop 6, a student should be able to:

1. Read a problem and restate it in their own words.
2. Write pseudocode for a solution before touching Python.
3. Implement basic linear-time algorithms on lists and strings.
4. Trace variable state through a loop by hand.
5. Walk a small problem through the full **Understand → Plan → Code → Test** loop.

## Non-Goals

- Big-O notation (too early — mentioned in passing only, if at all).
- Recursion (separate future workshop).
- Advanced sorting (merge sort, quicksort).
- Introducing new Python syntax (no comprehensions, no `lambda` in teaching code, no `with` or `try`).

## File layout

```
workshop_6/
├── 1_algorithmic_thinking.py
├── 2_searching_and_counting.py
├── 3_sorting.py
├── 4_string_algorithms.py
├── 5_practical_examples.py
└── homework.py
```

## File contents

### `1_algorithmic_thinking.py`

Establishes the meta-skill of the workshop.

- What an algorithm is — compared to a recipe.
- The four-step design process: **Understand → Plan → Code → Test**.
- A small worked example: "sum of a list", shown three times — plain English, pseudocode, Python.
- Key reminder: *pseudocode first, code second*.

### `2_searching_and_counting.py`

Four algorithms the student can reason about directly, each implemented without built-ins that trivialize them.

- Linear search — returns the index of a value, or `-1` if absent.
- Find minimum (manual, not `min()`).
- Find maximum (manual, not `max()`).
- Count occurrences of a value.
- Check whether a list has any duplicates.

Each section includes a trace-table comment showing variable state on a short input, so students can see how loops *mutate* state step by step.

### `3_sorting.py`

One algorithm taught deeply, rather than many shallowly.

- Bubble sort, step-by-step, on `[5, 2, 4, 1, 3]`, with the comparison/swap pattern annotated.
- A second version with the "no swaps this pass → done early" optimization.
- A one-line mention that Python provides `sorted()` and `.sort()`, but "we're learning *how*, not *what*."

### `4_string_algorithms.py`

Applies the same mindset to strings, re-using dictionary skills from Workshop 5.

- Reverse a string — two ways: slicing (`[::-1]`) as a reference, and a manual loop for teaching.
- Palindrome check.
- Count vowels.
- Anagram check using a letter-count dictionary (callback to Workshop 5).

### `5_practical_examples.py` — the walked-through algorithmic challenge

This is the **capstone** file. One problem, fully designed in front of the student.

**Problem:** Find the second-largest number in a list.

The file walks through the full four-step process as distinct, labeled comment sections:

1. **Understand** — the problem restated. Edge cases spelled out as test cases in comments: empty list, single element, all-duplicates, negatives, already sorted.
2. **Plan** — three pseudocode approaches, each with a trade-off comment:
   - *Naive:* sort the list, take the second-to-last element.
   - *Better:* find max, remove it, find max again.
   - *Best:* one pass, track largest and second-largest simultaneously.
3. **Code** — implement the one-pass version as a function.
4. **Test** — run it against every test case from step 1, including edges. Print pass/fail inline.

A second, shorter worked example follows in the same style — "find the most common character in a string" — to reinforce the pattern without re-teaching it from scratch.

### `homework.py`

Five tasks at increasing difficulty. Each asks the student to follow **Understand → Plan → Code → Test**. The file contains the problem statements and space for the student's pseudocode and code.

1. Find the smallest number in a list *without* using `min()`.
2. Reverse a list in place *without* using `.reverse()` or `[::-1]`.
3. Remove duplicates from a list *preserving original order* (so `set()` alone is not enough).
4. Check whether two strings are anagrams of each other.
5. Challenge: find the longest word in a sentence and return it.

## Style conventions

All files follow the patterns established in Workshops 1–5:

- First line header comment: `# Workshop 6 - <topic>`.
- Section dividers: `# ==============================` with a title line.
- Runnable top-to-bottom — no `if __name__ == "__main__":` guard.
- Expected output shown inline as `# prints: ...` or `# -> ...` comments where helpful.
- No `lambda` in teaching code. No list/dict comprehensions. No `try/except`. No imports.
- Print statements over returns for top-level demos; functions are used where the concept is itself reusable (search, sort, palindrome, etc.).

## Success criteria

- All six files run top-to-bottom with no errors on Python 3.
- No use of Python features the students haven't yet seen.
- The walked-through challenge in `5_practical_examples.py` demonstrates all four design steps explicitly in comments.
- Homework tasks can each be completed using only Workshops 1–6 material.