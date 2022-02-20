r, c, t = map(int, input().split())
room = []
filter = []
move = []
for _ in range(r):
    room.append(list(map(int, input().split())))

def find_filter():
    for i in range(r):
        for j in range(c):
            if room[i][j] == -1:
                filter.append((i,j))

def find_dust():
    for i in range(r):
        for j in range(c):
            if room[i][j] != 0 and room[i][j] != -1:
                dust.append((i,j))

def spread(x, y):
    s = room[x][y] // 5
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx = x + dx
        ny = y + dy
        if 0<=nx<r and 0<=ny<c and room[nx][ny] != -1:
            move.append((nx, ny, s))
            room[x][y] -= s

def apply():
    while move:
        x, y, s = move.pop()
        room[x][y] += s

def blow(x, y, p):
    if p == 0:
        t0 = room[0][0]
        t1 = room[x][y]
        t2 = room[x][-1]
        t3 = room[0][-1]

        for i in range(c-1, 0, -1):
            room[x][i] = room[x][i-1]
        for j in range(0, x):
            room[j][-1] = room[j+1][-1]
        for i in range(0, c-1):
            room[0][i] = room[0][i+1]
        for j in range(x-1, 0, -1):
            room[j][0] = room[j-1][0]

        room[1][0] = t0
        room[x-1][-1] = t2
        room[0][-2] = t3

        room[x][y] = -1
        room[x][y+1] = 0

    else:
        t0 = room[x][y]
        t1 = room[-1][0]
        t2 = room[-1][-1]
        t3 = room[x][-1]

        for i in range(c-1, 0, -1):
            room[x][i] = room[x][i-1]
        for j in range(r-1, x, -1):
            room[j][-1] = room[j-1][-1]
        for i in range(0, c-1):
            room[-1][i] = room[-1][i+1]
        for j in range(x, r-1):
            room[j][0] = room[j+1][0]

        room[-2][0] = t1
        room[-1][-2] = t2
        room[x+1][-1] = t3

        room[x][y] = -1
        room[x][y+1] = 0

find_filter()
for _ in range(t):
    dust = []
    find_dust()
    while dust:
        dx, dy = dust.pop()
        spread(dx, dy)
    apply()
    blow(filter[0][0], filter[0][1], 0)
    blow(filter[1][0], filter[1][1], 1)

answer = 0
for i in range(r):
    answer += sum(room[i])
print(answer+2)