from sys import stdin
import heapq

n = int(input())
presents = []

for _ in range(n):
    info = list(map(int, stdin.readline().split()))

    if info[0] == 0:
        if presents: print(-heapq.heappop(presents))
        else: print(-1)
    else:
        for i in range(1, info[0]+1):
            heapq.heappush(presents, -(info[i]))
