'''
[문제 분석]
- *N*개의 정점과 *M*개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어짐
- 정점 번호는 1번부터 *N*번이고 모든 간선의 가중치는 1
- 정점 *R*에서 시작하여 깊이 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서 출력

[의사결정]
- 인접 리스트로 간선 집합 만듦
- dfs로 각 정점 탐색하고 그 순서 저장

'''

from sys import stdin, stdout, setrecursionlimit

# 재귀 깊이를 늘려주는 설정 (기본적으로 재귀 호출의 깊이가 제한되어 있기 때문에 큰 값으로 설정)
setrecursionlimit(10 ** 6)


# v: 노드의 개수, e: 인접 리스트(그래프), r: 시작 노드, cnt: 방문 순서를 기록하는 카운트
def dfs(v, e, r, cnt):
    # 현재 노드를 방문 처리하고 방문 순서 기록
    visited[r] = cnt
    # 방문 순서를 증가시킴
    cnt += 1

    # 인접 노드들을 정렬한 후, 방문하지 않은 노드를 DFS로 재귀 호출
    # 정렬 이유 : 인접 정점은 오름차순으로 방문해야 하므로
    for x in sorted(e[r]):
        if not visited[x]:
            # 다음 노드를 재귀 호출하면서 방문 순서도 업데이트
            cnt = dfs(v, e, x, cnt)

            # 현재까지의 방문 순서를 반환 (재귀에서 돌아왔을 때 순서를 이어받기 위해)
    return cnt


n, m, r = map(int, input().split())

# 그래프를 인접 리스트 방식으로 표현 (노드의 수 n+1만큼 리스트를 생성)
nodes = [[] for _ in range(n + 1)]

# 각 노드의 방문 여부와 방문 순서를 기록하는 리스트
visited = [0 for _ in range(n + 1)]

# 간선 정보 입력 받기
# 양방향 그래프이므로 양쪽 노드에 서로 연결을 추가
for _ in range(m):
    u, v = map(int, stdin.readline().split())
    nodes[u].append(v)
    nodes[v].append(u)

# 깊이 우선 탐색 시작 (시작 노드 r에서 cnt는 1부터 시작)
dfs(n, nodes, r, 1)

# 결과를 빠르게 출력하기 위해 stdout 사용
for i in range(1, n + 1):
    stdout.write(f"{visited[i]}\n")