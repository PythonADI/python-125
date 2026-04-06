nums = [5, 7, 10, -3, 2, 0, 1, 2, -9, 2, 3, -10, -100, -99, 12312, -1345135, -1324513451, -324234234234, -24123213]
min_num = nums[0]
max_num = nums[0]

for num in nums:
    if num < min_num:
        min_num = num
    
    if max_num < num:
        max_num = num

print(min_num)
print(max_num)

print(min(nums))
print(max(nums))


