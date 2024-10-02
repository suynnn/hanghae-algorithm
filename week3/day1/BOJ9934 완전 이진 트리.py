k = int(input())
visited_buildings = list(map(int, input().split()))
ans = [[] for _ in range(k)]

def findBuilding(level, start, end):
    if start > end:
        return

    mid = (start + end) // 2
    ans[level].append(visited_buildings[mid])

    findBuilding(level+1, start, mid-1)
    findBuilding(level+1, mid+1, end)


findBuilding(0, 0, len(visited_buildings)-1)


for i in range(k):
    print(' '.join(map(str, ans[i])))