N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
magics = [list(map(int, input().split())) for _ in range(M)]


def getCoordLine():
    dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    sx, sy, sd = N//2, N//2, 0
    coordLine = [[sx, sy]]
    step = 1
    while True:
        for _ in range(2):
            for _ in range(step):
                sx += dirs[sd][0]
                sy += dirs[sd][1]
                if 0 <= sx < N and 0 <= sy < N:
                    coordLine.append([sx, sy])
                else:
                    return coordLine
            sd = (sd+1) % 4
        step += 1


def getBallLine():
    newBallLine = []
    for x, y in coordLine:
        if grid[x][y] == 0:
            break
        newBallLine.append(grid[x][y])
    return newBallLine


def ice(magic):
    d, s = magic
    direction = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]]
    iceList = set()
    sx, sy = N//2, N//2
    for _ in range(s):
        sx += direction[d][0]
        sy += direction[d][1]
        iceList.add((sx, sy))

    newBallLine = []
    for x, y in coordLine:
        if [x, y] != [N//2, N//2] and grid[x][y] == 0:
            break
        if (x, y) not in iceList:
            newBallLine.append(grid[x][y])
    return newBallLine


def explode():
    newBallLine = []
    temp = []
    for x in ballLine:
        if temp == [] or temp[-1] == x:
            temp.append(x)
        elif temp != [] and temp[-1] != x:
            if len(temp) < 4:
                newBallLine.extend(temp)
            else:
                count = len(temp)
                number = temp[-1]
                ballCount[number] += count
            temp = [x]
    if len(temp) < 4:
        newBallLine.extend(temp)
    else:
        count = len(temp)
        number = temp[-1]
        ballCount[number] += count
    return newBallLine


def change():
    newBallLine = [0]
    temp = []
    for x in ballLine[1:]:
        if temp == [] or temp[-1] == x:
            temp.append(x)
        elif temp != [] and temp[-1] != x:
            newBallLine.extend([len(temp), temp[-1]])
            temp = [x]
    if temp:
        newBallLine.extend([len(temp), temp[-1]])
    if len(newBallLine) > N*N:
        newBallLine = newBallLine[:N*N]
    return newBallLine


def drawGrid():
    newGrid = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(len(coordLine)):
        x, y = coordLine[i]
        if i == len(ballLine):
            break
        newGrid[x][y] = ballLine[i]
    return newGrid


def printGrid():
    for row in grid:
        print(row)
    print()


ballCount = [0, 0, 0, 0]
coordLine = getCoordLine()
ballLine = getBallLine()
for magic in magics:
    ballLine = ice(magic)

    beforeLength = len(ballLine)
    ballLine = explode()
    afterLength = len(ballLine)
    while beforeLength != afterLength:
        beforeLength = len(ballLine)
        ballLine = explode()
        afterLength = len(ballLine)

    ballLine = change()

    grid = drawGrid()

answer = 0
for i in range(1, 4):
    answer += i*ballCount[i]
print(answer)
