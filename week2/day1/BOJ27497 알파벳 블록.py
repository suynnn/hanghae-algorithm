import collections
from sys import stdin

n = int(stdin.readline())

# 문자열 저장할 deque 변수 및 문자열을 어디 위치에 저장했는지 그 값을 저장할 리스트 변수 선언
alpha = collections.deque()
loc = list()

for _ in range(n):
    # 반복문으로 여러줄을 입력 받아야 할 때는 input()으로 입력 받는다면 시간초과가 발생할 수 있음
    info = stdin.readline()

    # 1이면 맨 뒤에 문자 추가
    # 2이면 맨 앞에 문자 추가
    # append(), appendleft(), pop(), popleft()는 모두 O(1) 시간 복잡도를 가짐
    if info[0] == '1':
        alpha.append(info.split()[1])
        loc.append(1)
    elif info[0] == '2':
        alpha.appendleft(info.split()[1])
        loc.append(2)

    # 3이면 loc에서 가장 최근 위치 데이터 pop()해서 그 값을 기반으로 문자 제거
    else:
        if not alpha:
            continue
        else:
            if loc.pop() == 1:
                alpha.pop()
            else:
                alpha.popleft()

if not alpha:
    print(0)
else:
    print(''.join(alpha))