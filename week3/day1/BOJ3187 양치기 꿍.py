from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**6)

r, c = map(int, input().split())
board = []
visited = [[False] * c for _ in range(r)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(r):
    info = list(stdin.readline().rstrip())
    board.append(info)

def dfs(x, y):
    visited[x][y] = True

    wolf_cnt = 0
    sheep_cnt = 0

    if board[x][y] == 'v':
        wolf_cnt += 1
    elif board[x][y] == 'k':
        sheep_cnt += 1
    elif board[x][y] == '#':
        return [wolf_cnt, sheep_cnt]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < r and 0 <= ny < c) and not visited[nx][ny] and board[nx][ny] != '#':
            animals = dfs(nx, ny)

            wolf_cnt += animals[0]
            sheep_cnt += animals[1]


    return [wolf_cnt, sheep_cnt]


wolf_total_cnt = 0
sheep_total_cnt = 0

for i in range(r):
    for j in range(c):
        if not visited[i][j] and board[i][j] != '#':
            animals = dfs(i, j)

            wolf = animals[0]
            sheep = animals[1]

            if wolf < sheep:
                sheep_total_cnt += sheep
            else:
                wolf_total_cnt += wolf

print(f'{sheep_total_cnt}' + ' ' + f'{wolf_total_cnt}')