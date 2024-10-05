'''
[문제 분석]
- *N*개의 정점과 *M*개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어짐
- 정점 *R*에서 시작하여 너비 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력
- 인접 정점은 **오름차순**으로 방문

[의사결정]
- 인접 리스트로 간선 집합 만듦
- bfs로 각 정점 탐색하고 그 순서 저장

'''

from sys import stdin, stdout
from collections import deque


# nodes: 그래프의 인접 리스트
# r: 시작 정점
def bfs(nodes, r):
    # 방문 순서를 기록할 변수
    # 현재 시작 정점을 방문 처리한 후 방문 순서 1 증가
    seq = 1
    visited[r] = seq
    seq += 1

    q = deque()
    q.append(r)

    while q:
        # 큐에서 가장 앞의 정점을 꺼냄
        u = q.popleft()

        # 현재 정점에 연결된 인접 정점(오름차순 정렬된)들을 방문
        for node in sorted(nodes[u]):

            # 아직 방문하지 않은 정점만 탐색
            # 방문 순서를 기록 후 순서 1 증가시킴
            if visited[node] == 0:
                visited[node] = seq
                seq += 1

                # 인접 정점을 큐에 삽입
                q.append(node)


n, m, r = map(int, input().split())

# 방문 순서를 기록할 리스트. 0으로 초기화 (정점 번호는 1부터 시작하므로 n+1)
# 인접 리스트로 그래프를 표현
visited = [0 for _ in range(n + 1)]
nodes = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, stdin.readline().split())
    nodes[u].append(v)
    nodes[v].append(u)

bfs(nodes, r)

for i in range(1, n + 1):
    stdout.write(f"{visited[i]}\n")