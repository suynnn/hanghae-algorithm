from sys import stdin

n = int(input())
stack = []

for _ in range(n):
    stick = int(stdin.readline())
    stack.append(stick)

cnt = 1
standard = stack.pop()

while stack:
    tmp = stack.pop()

    if tmp > standard:
        standard = tmp
        cnt += 1

print(cnt)