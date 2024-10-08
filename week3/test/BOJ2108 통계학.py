from sys import stdin
from collections import defaultdict


n = int(input())
nums = []

for _ in range(n):
    nums.append(int(stdin.readline()))

nums.sort()


def custom_round(num):
    if num >= 0:
        if num - int(num) >= 0.5:
            return int(num) + 1
        else:
            return int(num)
    else:
        if -num - int(-num) >= 0.5:
            return int(num) -1
        else:
            return int(num)


nums_sum = custom_round(sum(nums)/n)
nums_mid = nums[len(nums)//2]

nums_dict = defaultdict(int)
for num in nums:
    nums_dict[num] += 1

keys = []
if len(nums_dict) != 1:
    max_value = max(nums_dict.values())
    keys = sorted([key for key, value in nums_dict.items() if value == max_value], reverse=True)
    if len(keys) != 1:
        keys.pop()

else:
    keys.append(list(nums_dict.keys())[0])

nums_mode = keys.pop()

nums_range = nums[len(nums)-1] - nums[0]

print(nums_sum)
print(nums_mid)
print(nums_mode)
print(nums_range)
