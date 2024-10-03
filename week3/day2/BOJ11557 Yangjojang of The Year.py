'''
[문제 분석]
학교별로 한 해동안 술 소비량이 주어질 때, 가장 술 소비가 많은 학교 이름을 출력

[의사결정]
술 소비량을 기준으로 내림차순 정렬 후 정답 출력

'''

from sys import stdin

t = int(input())

for _ in range(t):
    n = int(stdin.readline())
    schools = []

    for _ in range(n):
        s, l = input().split()
        schools.append([s, int(l)])

    # 술 소비량을 기준으로 내림차순 정렬 후 소비량이 가장 높은 학교 출력
    schools.sort(key=lambda x: x[1], reverse=True)
    print(schools[0][0])
