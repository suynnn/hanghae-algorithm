'''
[문제 분석]
네트워크 상에서 연결되어 있는 컴퓨터끼리 바이러스가 전파됨

[의사결정]
dfs로 연결되어 있는 컴퓨터 끝까지 탐색

'''


from sys import stdin

# 컴퓨터 수, 컴퓨터 쌍의 수, 네트워크 상 연결된 컴퓨터 정보, 컴퓨터 방문 여부 저장할 변수 선언
computer_cnt = int(input())
computer_relation_cnt = int(input())
network = [[] for _ in range(computer_cnt + 1)]
visited = [False for _ in range(computer_cnt + 1)]


def dfs(computer, cnt):
		# 현재 위치의 컴퓨터는 방문처리 함
    visited[computer] = True

    for x in network[computer]:
		    # 현재 컴퓨터와 연결된 컴퓨터들 중 아직 방문하지 않은 곳들만
		    # 바이러스에 감염시키므로 그 카운트 하나씩 증가하고 리턴
        if not visited[x]:
            cnt = dfs(x, cnt+1)

    return cnt


for _ in range(computer_relation_cnt):
    a, b = map(int, stdin.readline().split())

    network[a].append(b)
    network[b].append(a)

# 1번 컴퓨터부터 dfs
virus_computer_cnt = dfs(1, 0)

print(virus_computer_cnt)