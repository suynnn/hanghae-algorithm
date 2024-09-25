from sys import stdin

n = int(stdin.readline())

deq = []

for _ in range(n):
    # 반복문으로 여러줄을 입력 받아야 할 때 input()으로 입력 받는다면 시간초과가 발생할 수 있음
    cmd = stdin.readline().split()

    if cmd[0] == 'push_back':
        deq.append(int(cmd[1]))
    elif cmd[0] == 'push_front':
        deq.insert(0, int(cmd[1]))
    elif cmd[0] == 'pop_front':
        if not deq:
            print(-1)
        else:
            print(deq[0])
            deq = deq[1:]
    elif cmd[0] == 'pop_back':
        if not deq:
            print(-1)
        else:
            print(deq.pop())
    elif cmd[0] == 'size':
        print(len(deq))
    elif cmd[0] == 'empty':
        if not deq:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if not deq:
            print(-1)
        else:
            print(deq[0])
    elif cmd[0] == 'back':
        if not deq:
            print(-1)
        else:
            print(deq[len(deq)-1])

