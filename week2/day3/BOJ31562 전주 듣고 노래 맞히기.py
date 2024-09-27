from sys import stdin

n, m = map(int, input().split())
songs = dict()

for _ in range(n):
    songInfo = stdin.readline().rstrip().split()

    songs[songInfo[1]] = ' '.join(songInfo[2:5])

for _ in range(m):
    pitch = stdin.readline().rstrip()

    findSongs = [k for k, v in songs.items() if v == pitch]

    if findSongs:
        if len(findSongs) == 1:
            print(findSongs[0])
        else:
            print('?')
    else:
        print('!')