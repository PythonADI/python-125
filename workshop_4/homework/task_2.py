import math

def circle_area(r):
    return math.pi * (r ** 2)


def circle_circumference(r):
    return 2 * math.pi * r

def circle_info(r):
    area = circle_area(r)
    circumference = circle_circumference(r)
    return area, circumference


print(circle_area(7))

print(circle_circumference(7))

result = circle_info(7)
print(type(result), result)

nums = (5, 7, 10, 11, -10, 27)
print(nums)
print(nums[-1])
print(len(nums))

# nums[0] = 1

print(sum(nums))
print(max(nums))
print(min(nums))

for num in nums:
    print(num)

