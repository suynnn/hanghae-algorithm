from sys import stdin

s = list(input().strip())
n = int(input())
stk = []

for _ in range(n):
    cmd = stdin.readline().rstrip().split()

    if cmd[0] == 'L':
        if s:
            stk.append(s.pop())
    elif cmd[0] == 'D':
        if stk:
            s.append(stk.pop())
    elif cmd[0] == 'B':
        if s:
            s.pop()
    elif cmd[0] == 'P':
        s.append(cmd[1])

s.extend(reversed(stk))

print(''.join(s))