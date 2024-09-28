from sys import stdin
import heapq

n, h, t = map(int , input().split())
giants = []
cnt = 0

for _ in range(n):
    heapq.heappush(giants, -(int(stdin.readline())))

for _ in range(t):
    giant = -heapq.heappop(giants)

    if giant < h or giant <= 1:
        heapq.heappush(giants, -giant)
        break
    else:
        heapq.heappush(giants, -(giant//2))
        cnt += 1

giant = -heapq.heappop(giants)

if giant < h:
    print("YES")
    print(cnt)
else:
    print("NO")
    print(giant)
