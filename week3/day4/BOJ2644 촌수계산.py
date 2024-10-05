from sys import stdin
from collections import deque

n = int(input())
find_relative_num = list(map(int, input().split()))
m = int(input())

relatives = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
distance = [-1 for _ in range(n+1)]


def bfs(start):
    visited[start] = True
    distance[start] = 0

    q = deque()
    q.append(start)

    while q:
        person = q.popleft()

        for relative in relatives[person]:
            if not visited[relative]:
                visited[relative] = True
                distance[relative] = distance[person] + 1
                q.append(relative)


for _ in range(m):
    x, y = map(int, stdin.readline().split())

    relatives[x].append(y)
    relatives[y].append(x)

bfs(find_relative_num[0])

# 두 번째 사람의 촌수 출력, 촌수가 계산되지 않으면 -1 출력
result = distance[find_relative_num[1]]

print(result if result != -1 else -1)