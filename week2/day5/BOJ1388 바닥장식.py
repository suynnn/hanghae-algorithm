from sys import stdin

n, m = map(int, input().split())

floor = []
visited = [[False] * m for _ in range(n)]


def dfs(x, y):
    visited[x][y] = True

    if floor[x][y] == '-':
        if y+1 < m and floor[x][y+1] == '-' and not visited[x][y+1]:
            dfs(x, y+1)
    elif floor[x][y] == '|':
        if x+1 < n and floor[x][y] == '|' and floor[x+1][y] == '|' and not visited[x+1][y]:
            dfs(x+1, y)


for _ in range(n):
    deco = stdin.readline().rstrip()
    floor.append(deco)

boards = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i, j)
            boards += 1

print(boards)