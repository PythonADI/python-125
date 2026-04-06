# Workshop 3 - break and continue

# ==============================
# break - exits the loop immediately
# ==============================

for i in range(10):
    if i == 5:
        break
    print(i)       # prints 0, 1, 2, 3, 4


# ==============================
# continue - skips the current iteration
# ==============================

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)       # prints 1, 3, 5, 7, 9
