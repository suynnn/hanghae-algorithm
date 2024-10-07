from collections import deque

farm = []
visited = [[False] * 10 for _ in range(10)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(barn, cow_cnt):
    visited[barn[0]][barn[1]] = True

    q = deque()
    q.append([[barn[0], barn[1]], cow_cnt])

    while q:
        now, cow_cnt = q.popleft()

        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]

            if 0 <= nx < 10 and 0 <= ny < 10:
                if farm[nx][ny] == '.' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([[nx, ny], cow_cnt+1])

                elif farm[nx][ny] == 'L':
                    return cow_cnt


for _ in range(10):
    farm.append(list(input()))

now = []
lake = []
for i in range(10):
    for j in range(10):
        if farm[i][j] == 'B':
            now.append(i)
            now.append(j)

        if farm[i][j] == 'L':
            lake.append(i)
            lake.append(j)

cows = bfs(now, 0)
print(cows)
