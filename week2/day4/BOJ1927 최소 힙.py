from sys import stdin
import heapq

n = int(input())
nums = []

for _ in range(n):
    num = int(stdin.readline())

    if num == 0:
        if not nums: print(0)
        else: print(heapq.heappop(nums))
    else:
        heapq.heappush(nums, num)