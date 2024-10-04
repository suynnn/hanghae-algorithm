from sys import stdin

t = int(input())
for _ in range(t):
    n = int(stdin.readline())

    newcomers = []
    for _ in range(n):
        document, interview = map(int, stdin.readline().rstrip().split())
        newcomers.append([document, interview])

    newcomers.sort()

    newcomer_cnt = 1
    newcomer_rank = newcomers[0][1]

    for i in range(1, n):
        if newcomer_rank > newcomers[i][1]:
            newcomer_rank = newcomers[i][1]
            newcomer_cnt += 1

    print(newcomer_cnt)
