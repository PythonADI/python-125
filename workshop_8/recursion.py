from functools import cache
# 1 1 2 3 5 8 13 21

results = {}



def fib(n):
    if n <= 2:
        # base case
        return 1
    if n in results:
        return results[n]

    results[n] = fib(n - 1) + fib(n - 2)
    return results[n]


for n in range(1, 1000):
    print(fib(n))


# n = 1000
# a = 1
# a2 = 1
# num = 0
# for _ in range(n):
#     num = a + a2
#     a = a2
#     a2 = num
#     print(num)
#
# print(num)


