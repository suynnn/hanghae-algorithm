n = int(input())
s = list(input())

ans = 0
for i, x in enumerate(s):
    ans += (ord(x)-96) * (31**i)

ans %= 1234567891
print(ans)