from itertools import combinations

n = int(input())
room = []
space = []
teacher = []
for i in range(n):
    room.append(list(input().split()))
    for j in range(n):
        if room[i][j] == 'X':
            space.append((i, j))
        if room[i][j] == 'T':
            teacher.append((i, j))


def search(x, y, d):
    if d == 0:
        while x>=0:
            if room[x][y] == 'S':
                return True
            if room[x][y] == 'O':
                return False
            x -= 1
    elif d == 1:
        while x<n:
            if room[x][y] == 'S':
                return True
            if room[x][y] == 'O':
                return False
            x += 1
    elif d == 2:
        while y>=0:
            if room[x][y] == 'S':
                return True
            if room[x][y] == 'O':
                return False
            y -= 1
    elif d == 3:
        while y<n:
            if room[x][y] == 'S':
                return True
            if room[x][y] == 'O':
                return False
            y += 1
    return False

ans = False

def hide():
    for x, y in teacher:
        for d in range(4):
            if search(x, y, d):
                return False
    return True

for case in combinations(space, 3):
    for x, y in case:
        room[x][y] = 'O'
    if hide():
        ans = True
        break
    for x, y in case:
        room[x][y] = 'X'

if ans:
    print('YES')
else:
    print('NO')