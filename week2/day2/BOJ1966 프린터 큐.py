from sys import stdin
import collections

n = int(input())

for _ in range(n):
    n, m = map(int, stdin.readline().rstrip().split())
    docs = list(map(int, stdin.readline().rstrip().split()))

    deque = collections.deque()
    cnt = 0

    for i, x in enumerate(docs):
        deque.append([i, x])

    while True:
        maxDocs = max(deque, key=lambda x: x[1])[1]

        printDocs = deque.popleft()

        if maxDocs > printDocs[1]:
            deque.append(printDocs)
        else:
            cnt += 1
            if m == printDocs[0]:
                print(cnt)
                break
