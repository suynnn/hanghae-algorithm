from sys import stdin

r, c = map(int, input().split())

grass_map = []
visited = [[False] * c for _ in range(r)]


def dfs(x, y):
    visited[x][y] = True

    if y+1 < c and grass_map[x][y+1] == '#' and not visited[x][y+1]:
        dfs(x, y+1)
    elif x+1 < r and grass_map[x+1][y] == '#' and not visited[x+1][y]:
        dfs(x+1, y)


for _ in range(r):
    grass = stdin.readline().rstrip()
    grass_map.append(grass)

grass_bundle = 0
for i in range(r):
    for j in range(c):
        if grass_map[i][j] == '#' and not visited[i][j]:
            dfs(i, j)
            grass_bundle += 1

print(grass_bundle)