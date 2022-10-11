# 18:40
from copy import deepcopy

M, S = map(int, input().split())
grid = [[[] for _ in range(4)] for _ in range(4)]
smell = [[0 for _ in range(4)] for _ in range(4)]

for _ in range(M):
    fx, fy, fd = map(int, input().split())
    grid[fx-1][fy-1].append(fd)

sx, sy = map(int, input().split())
shark = [sx-1, sy-1]

direction = [[0, 0], [0, -1], [-1, -1], [-1, 0],
             [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]


def fishMove():
    newGrid = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            while grid[x][y]:
                fd = grid[x][y].pop()
                flag = False
                for d in range(8):
                    nd = fd-d
                    if nd < 1:
                        nd = 8+nd
                    nx = x + direction[nd][0]
                    ny = y + direction[nd][1]
                    if 0 <= nx < 4 and 0 <= ny < 4 and [nx, ny] != shark and smell[nx][ny] == 0:
                        newGrid[nx][ny].append(nd)
                        flag = True
                        break
                if not flag:
                    newGrid[x][y].append(fd)
    return newGrid


def getNextSharkMoves(x, y, route, eatCount):
    global maxEatCount, nextSharkMoves

    if len(route) == 3:
        if eatCount > maxEatCount:
            maxEatCount = eatCount
            nextSharkMoves = route
        return

    for i in [3, 1, 7, 5]:
        nx = x + direction[i][0]
        ny = y + direction[i][1]
        if 0 <= nx < 4 and 0 <= ny < 4:
            fishes = newGrid[nx][ny]
            newGrid[nx][ny] = []
            getNextSharkMoves(nx, ny, route+[[nx, ny]], eatCount+len(fishes))
            newGrid[nx][ny] = fishes


def sharkMove():
    for x, y in nextSharkMoves:
        if newGrid[x][y] != []:
            newGrid[x][y] = []
            smell[x][y] = 3
    return nextSharkMoves[-1]


def removeSmell():
    for x in range(4):
        for y in range(4):
            if smell[x][y] > 0:
                smell[x][y] -= 1


def finishMagic(originalGrid, newGrid):
    for x in range(4):
        for y in range(4):
            newGrid[x][y].extend(originalGrid[x][y])
    return newGrid


def printGrid(g):
    for x in range(4):
        print(g[x])
    print()


for _ in range(S):
    # 복제 마법 시전
    originalGrid = deepcopy(grid)

    # 물고기 이동
    newGrid = fishMove()

    # 상어 이동
    maxEatCount = -1
    nextSharkMoves = []

    sx, sy = shark
    getNextSharkMoves(sx, sy, [], 0)
    shark = sharkMove()

    # 냄새 제거
    removeSmell()

    grid = finishMagic(originalGrid, newGrid)

answer = 0
for x in range(4):
    for y in range(4):
        answer += len(grid[x][y])
print(answer)
