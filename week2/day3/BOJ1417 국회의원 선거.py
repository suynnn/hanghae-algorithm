from sys import stdin
import heapq

n = int(input())
dasom = int(input())

candidates = []
cnt = 0

for _ in range(n-1):
    heapq.heappush(candidates, -(int(stdin.readline())))

while n > 1:
    candidate = -heapq.heappop(candidates)

    if dasom > candidate:
        break

    candidate -= 1
    heapq.heappush(candidates, -candidate)

    dasom += 1
    cnt += 1

print(cnt)