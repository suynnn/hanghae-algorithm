from sys import stdin

testcase = int(input())

for _ in range(testcase):
    a, b = map(int, stdin.readline().rstrip().split())

    while a != b:
        if a < b:
            b = b//2
        else:
            a = a//2

    print(a*10)
