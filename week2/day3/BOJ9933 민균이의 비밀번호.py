from sys import stdin

n = int(input())
words = set()
ans = ''

for _ in range(n):
    s = stdin.readline().rstrip()

    words.add(s)

    if ''.join(reversed(list(s))) in words:
        ans = str(len(s)) + ' ' + s[len(s)//2]

print(ans)
