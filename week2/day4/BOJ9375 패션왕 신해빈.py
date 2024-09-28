from sys import stdin
from collections import defaultdict

testcase = int(input())

for _ in range(testcase):
    n = int(stdin.readline())

    clothes = defaultdict(list)
    for _ in range(n):
        clothesInfo = stdin.readline().rstrip().split()
        clothes[clothesInfo[1]].append(clothesInfo[0])

    res = 1
    for k in clothes:
        res *= len(clothes.get(k))+1
    res -= 1

    print(res)
