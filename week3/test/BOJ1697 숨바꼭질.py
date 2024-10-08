from collections import deque

n, k = map(int, input().split())
direction = [-1, 1, 2]
visited = [False for _ in range(100_001)]


def bfs(cnt):
    q = deque()
    q.append([n, cnt])

    visited[n] = True

    while q:
        num, cnt = q.popleft()

        if num == k:
            return cnt

        for i in range(3):
            if i == 2:
                next_num = num * 2
            else:
                next_num = num + direction[i]

            if 0 <= next_num <= 100_000 and not visited[next_num]:
                visited[next_num] = True
                q.append([next_num, cnt+1])


ans = bfs(0)
print(ans)