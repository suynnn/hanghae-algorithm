'''
[문제 분석]
- 1부터 N번까지의 도시 및 M개의 단방향 도로 존재
    - 거리는 모두 1
    - 특정한 도시 *X*로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 *K*인 모든 도시들의 번호를 출력하는 프로그램을 작성

[의사결정]
최단 거리 구하는데 적합한 bfs로 모든 도시 경로 탐색

'''

from sys import stdin
from collections import deque

# 거리정보들을 저장하고 방문한 도시 정보를 저장할 리스트 선언
n, m, k, x = map(int, input().split())
roads = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

# 주어진 거리정보만큼 갈 수 있는 도시 데이터 담기 위한 리스트 선언
ans_cites = []


def bfs():
    # 출발 도시 방문 처리
    visited[x] = 1

    # 큐에 출발 도시 및 방문 횟수 cnt를 0으로 설정하고 append
    q = deque()
    q.append([x, 0])

    while q:
        city, cnt = q.popleft()

        # 만약 최단 거리가 K라면 정답 리스트에 해당 도시 데이터 추가
        if cnt == k:
            ans_cites.append(city)

        for road in roads[city]:
            # 이전에 방문하지 않은 곳들만 탐색할 수 있음
            if visited[road] == 0:
                visited[road] = 1
                q.append([road, cnt + 1])


for _ in range(m):
    a, b = map(int, stdin.readline().split())
    roads[a].append(b)

bfs()

# 최단거리를 만족하는 도시가 없다면 -1을, 있다면 오름차순으로 정렬해서 출력
if not ans_cites:
    print(-1)
else:
    for city in sorted(ans_cites):
        print(city)