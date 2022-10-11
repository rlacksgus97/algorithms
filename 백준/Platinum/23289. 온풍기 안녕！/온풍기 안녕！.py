# 12:30
R, C, K = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
W = int(input())
wall = [list(map(int, input().split())) for _ in range(W)]
temperature = [[0 for _ in range(C)] for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
directions = [[0, 0], [0, 1], [0, -1], [-1, 0], [1, 0]]

canNotMove = set()
for x, y, t in wall:
    x -= 1
    y -= 1
    if t == 0:
        canNotMove.add((x, y, x-1, y))
        canNotMove.add((x-1, y, x, y))
    else:
        canNotMove.add((x, y, x, y+1))
        canNotMove.add((x, y+1, x, y))


def check():
    for i in range(R):
        for j in range(C):
            if room[i][j] == 5 and temperature[i][j] < K:
                return False
    return True


def inRange(x, y):
    if 0 <= x < R and 0 <= y < C:
        return True
    return False


def blow(x, y, d, power):
    global visited
    if power == 0:
        return
    temperature[x][y] += power
    visited[x][y] = 1
    if d in [3, 4]:
        for nd in [1, 2]:
            x1, y1 = x + directions[nd][0], y + directions[nd][1]
            if inRange(x1, y1) and (x, y, x1, y1) not in canNotMove:
                x2, y2 = x1 + directions[d][0], y1 + directions[d][1]
                if inRange(x2, y2) and visited[x2][y2] == 0 and (x1, y1, x2, y2) not in canNotMove:
                    blow(x2, y2, d, power-1)
    else:
        for nd in [3, 4]:
            x1, y1 = x + directions[nd][0], y + directions[nd][1]
            if inRange(x1, y1) and (x, y, x1, y1) not in canNotMove:
                x2, y2 = x1 + directions[d][0], y1 + directions[d][1]
                if inRange(x2, y2) and visited[x2][y2] == 0 and (x1, y1, x2, y2) not in canNotMove:
                    blow(x2, y2, d, power-1)
    x1, y1 = x + directions[d][0], y + directions[d][1]
    if inRange(x1, y1) and visited[x1][y1] == 0 and (x, y, x1, y1) not in canNotMove:
        blow(x1, y1, d, power-1)


def heaterWork():
    global visited
    for i in range(R):
        for j in range(C):
            if 1 <= room[i][j] <= 4:
                nd = room[i][j]
                ni = i + directions[nd][0]
                nj = j + directions[nd][1]
                visited = [[0 for _ in range(C)] for _ in range(R)]
                if (i, j, ni, nj) not in canNotMove:
                    visited[ni][nj] = 1
                    blow(ni, nj, nd, 5)


def balance():
    newTemperature = [[0 for _ in range(C)] for _ in range(R)]
    loose = []
    for i in range(R):
        for j in range(C):
            # 주변에 흩어지는 양 계산
            gain = []
            for d in range(1, 5):
                ni = i + directions[d][0]
                nj = j + directions[d][1]
                if 0 <= ni < R and 0 <= nj < C and (i, j, ni, nj) not in canNotMove and temperature[i][j] > temperature[ni][nj]:
                    amount = (temperature[i][j] - temperature[ni][nj]) // 4
                    gain.append([ni, nj, amount])

            # 흩어진 온도 추가
            total = 0
            for x, y, a in gain:
                newTemperature[x][y] += a
                total += a
            loose.append([i, j, total])

    # 남은 온도 추가
    for x, y, a in loose:
        newTemperature[x][y] += temperature[x][y]-a

    return newTemperature


def decrease():
    for i in range(R):
        for j in range(C):
            if i == 0 or i == R-1 or j == 0 or j == C-1:
                if temperature[i][j] >= 1:
                    temperature[i][j] -= 1


def printGrid(g):
    for row in g:
        print(row)
    print()


chocolate = 0
while not check() and chocolate <= 100:
    heaterWork()
    temperature = balance()
    decrease()
    chocolate += 1
if chocolate <= 100:
    print(chocolate)
else:
    print(101)
