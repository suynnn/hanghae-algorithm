import collections

n, k = map(int, input().split())
nums = collections.deque(i+1 for i in range(n))

permu = []

while len(permu) < n:
    for _ in range(k-1):
        nums.append(nums.popleft())

    permu.append(nums.popleft())

ans = '<' + ', '.join(map(str, permu)) + '>'

print(ans)
