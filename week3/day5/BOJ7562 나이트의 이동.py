'''
[문제 분석]
나이트가 몇 번 움직여야 움직이려고 하는 곳에 갈 수 있을지 계산하는 문제

[의사결정]
최소 몇 번만에 이동할 수 있는지 묻는 문제이므로 최단거리를 구하는데 적합한 bfs 사용

'''

from sys import stdin
from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


# 시작지점, 체스판 보드 크기, 도달지점을 가지고 bfs 함수 시작
def bfs(start_x, start_y, l, goal):
    chess_board = [[False] * l for _ in range(l)]

    # 큐에 시작 위치와 움직인 횟수를 저장
    q = deque([[start_x, start_y, 0]])
    chess_board[start_x][start_y] = True  # 시작 위치 방문 처리

    while q:
        x, y, cnt = q.popleft()

        if x == goal[0] and y == goal[1]:
            return cnt

        # 나이트가 이동할 수 있는 8가지 방향으로 이동
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l and not chess_board[nx][ny]:
                chess_board[nx][ny] = True  # 방문처리
                q.append([nx, ny, cnt + 1])  # 이동 횟수를 1 증가시키고 큐에 추가


testcase = int(input())
for _ in range(testcase):
    l = int(stdin.readline())

    now_x, now_y = map(int, stdin.readline().split())
    goal_x, goal_y = map(int, stdin.readline().split())

    cnt = bfs(now_x, now_y, l, [goal_x, goal_y])

    print(cnt)