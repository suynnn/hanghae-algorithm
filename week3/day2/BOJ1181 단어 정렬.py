from sys import stdin

n = int(input())
words = set()

for _ in range(n):
    words.add(stdin.readline().rstrip())

words = sorted(words, key=lambda x: (len(x), x))

for x in words:
    print(x)