import random

# nums = []
#
# for i in range(100):
#     nums.append(random.randint(0, 100))
#
# print(nums)
# print(len(nums))


# nums = [5] * 100
nums = [random.randint(0, 100) for _ in range(8)]
print(nums)


# nums = set()
#
# while len(nums) < 8:
#     num = random.randint(0, 100)
#     print(num)
#     nums.add(num)
#
# nums = list(nums)
# print(nums)

nums = []

while len(nums) < 50:
    num = random.randint(0, 100)
    if num not in nums:
        nums.append(num)

print(nums)

nums = [
    num
    for num in nums
    if num % 2 == 0
]
print(nums)