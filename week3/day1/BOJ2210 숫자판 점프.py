board = [input().split() for _ in range(5)]
nums = set()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y, s):
    if len(s) == 6:
        nums.add(s)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, s + board[nx][ny])


for i in range(5):
    for j in range(5):
        dfs(i, j, board[i][j])

print(len(nums))