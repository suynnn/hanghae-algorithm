from sys import stdin
import heapq

t = int(input())

for _ in range(t):
    k = int(stdin.readline())

    files = list(map(int, stdin.readline().rstrip().split()))
    heapq.heapify(files)

    cost = 0
    while len(files) > 1:
        tem_cost = heapq.heappop(files) + heapq.heappop(files)
        heapq.heappush(files, tem_cost)

        cost += tem_cost

    print(cost)