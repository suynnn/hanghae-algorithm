import collections
from sys import stdin

n = int(input())
que = collections.deque()

for _ in range(n):
    cmd = stdin.readline().rstrip().split()

    if cmd[0] == 'push':
        que.append(cmd[1])

    elif cmd[0] == 'pop':
        if not que:
            print(-1)
        else:
            print(que.popleft())

    elif cmd[0] == 'size':
        print(len(que))

    elif cmd[0] == 'empty':
        if que:
            print(0)
        else:
            print(1)

    elif cmd[0] == 'front':
        if not que:
            print(-1)
        else:
            print(que[0])

    elif cmd[0] == 'back':
        if not que:
            print(-1)
        else:
            print(que[-1])
