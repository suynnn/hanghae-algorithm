x = input()

cnt = 0

while len(x) > 1:
    ans = 0
    for c in x:
        ans += int(c)
    cnt += 1

    x = str(ans)

print(cnt)

if int(x) % 3 == 0:
    print("YES")
else:
    print("NO")