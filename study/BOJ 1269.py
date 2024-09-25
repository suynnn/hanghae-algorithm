a, b = map(int, input().split())
listA = set(map(int, input().split()))
listB = set(map(int, input().split()))

cnt = len(listA-listB) + len(listB-listA)

print(cnt)