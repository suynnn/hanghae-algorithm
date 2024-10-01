from sys import stdin

n = int(input())
stack = []
building_cnt = 0

for _ in range(n):
    x, y = map(int, stdin.readline().split())

    if not stack or stack[-1] < y:
        stack.append(y)
    elif stack[-1] == y:
        continue
    elif stack[-1] > y:
        while stack and stack[-1] > y:
            if stack[-1] > 0:
                building_cnt += 1
            stack.pop()

        if y > 0:
            # 스택의 최상단 값과 다를 때만 스택에 추가
            if not stack or stack[-1] != y:
                stack.append(y)

# 스택에 남은 높이에 대해 처리
while stack:
    if stack[-1] > 0:
        building_cnt += 1
    stack.pop()

print(building_cnt)
