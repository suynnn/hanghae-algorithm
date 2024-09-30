n = int(input())

jump_map = []
visited = [[False] * n for _ in range(n)]
is_reach_the_end = 0


def dfs(x, y):
    visited[x][y] = True

    if jump_map[x][y] == -1:
        global is_reach_the_end
        is_reach_the_end = 1
        return

    if y+jump_map[x][y] < n and not visited[x][y + jump_map[x][y]]:
        dfs(x, y+jump_map[x][y])
    if x+jump_map[x][y] < n and not visited[x + jump_map[x][y]][y]:
        dfs(x+jump_map[x][y], y)


for _ in range(n):
    zone = list(map(int, input().split()))
    jump_map.append(zone)

dfs(0, 0)

if is_reach_the_end == 1:
    print('HaruHaru')
else:
    print('Hing')
