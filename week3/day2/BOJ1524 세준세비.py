'''
[문제 분석]
- 전쟁 규칙
    - 여러 번의 전투로 이루어짐
    - 살아있는 병사 중 제일 약한 병사가 죽음
        - 만약 제일 약한 병사가 여러 명이고, 제일 약한 병사가 모두 같은 편에 있다면, 그 중에 한 명이 임의로 선택되어 죽음
        - 제일 약한 병사가 여러 명이고, 양 편에 모두 있다면, 세비의 제일 약한 병사 중 한 명이 임의로 선택되어 죽음

[의사결정]
- 양쪽의 병사가 남아있을 때까지 while문 반복하고 값을 비교해서 군사력 제거

'''

t = int(input())

for _ in range(t):
    input()

    n, m = map(int, input().split())
    s_soldiers = list(map(int, input().split()))
    b_soldiers = list(map(int, input().split()))

    # 양쪽의 병사가 모두 남아 있는 동안 반복
    while len(s_soldiers) > 0 and len(b_soldiers) > 0:

        if s_soldiers[-1] >= b_soldiers[-1]:
            b_soldiers.pop()
        else:
            s_soldiers.pop()

    # 반복문이 끝난 후 세준이의 병사가 더 많이 남아있으면 세준이의 승리
    if len(s_soldiers) > len(b_soldiers):
        print('S')
    else:
        print('B')
