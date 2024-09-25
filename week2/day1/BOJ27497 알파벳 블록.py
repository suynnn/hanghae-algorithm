import collections
from sys import stdin

n = int(stdin.readline())

alpha = collections.deque()
loc = list()

for _ in range(n):
    info = stdin.readline()

    if info[0] == '1':
        alpha.append(info.split()[1])
        loc.append(1)
    elif info[0] == '2':
        alpha.appendleft(info.split()[1])
        loc.append(2)

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