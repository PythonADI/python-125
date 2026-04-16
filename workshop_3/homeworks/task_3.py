evens = []
odds = []

for num in range(1, 21):
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)


# evens = list(range(2, 21, 2))
# odds = list(range(1, 21, 2))
print(evens)
print(odds)