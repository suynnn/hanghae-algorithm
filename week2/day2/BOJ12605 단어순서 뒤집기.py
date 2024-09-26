from sys import stdin

n = int(input())

for i in range(n):
    s = stdin.readline().rstrip().split()

    answer = 'Case #' + str(i+1) + ': '

    while s:
        answer += s.pop() + ' '

    print(answer)