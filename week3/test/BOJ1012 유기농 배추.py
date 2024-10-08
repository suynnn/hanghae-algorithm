from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10**6)

t = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(field, visited, x, y, m, n, cnt):

    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < m and 0 <= ny < n) and field[nx][ny] and not visited[nx][ny]:
            visited[x][y] = True
            dfs(field, visited, nx, ny, m, n, cnt+1)


for _ in range(t):
    m, n, k = map(int, input().split())
    field = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, stdin.readline().split())

        field[x][y] = 1

    cnt = 0
    for i in range(m):
        for j in range(n):
            if field[i][j] == 1 and not visited[i][j]:
                dfs(field, visited, i, j, m, n, cnt)
                cnt += 1

    print(cnt)
