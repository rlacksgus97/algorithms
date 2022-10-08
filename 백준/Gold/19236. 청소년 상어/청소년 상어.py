from copy import deepcopy

grid = [[[] for _ in range(4)] for _ in range(4)]
for i in range(4):
    f = list(map(int, input().split()))
    for j in range(0, 8, 2):
        grid[i][j//2] = [f[j], f[j+1]]

direction = [[0, 0], [-1, 0], [-1, -1], [0, -1],
             [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]


def fishMove(beforeGrid):
    fishList = [[] for _ in range(17)]
    for i in range(4):
        for j in range(4):
            if beforeGrid[i][j] != [] and beforeGrid[i][j][0] != 0:
                fishList[beforeGrid[i][j][0]] = [
                    beforeGrid[i][j][0], beforeGrid[i][j][1], i, j]
    for fish in fishList:
        if fish == []:
            continue
        n, d, x, y = fish
        for i in range(8):
            nd = (d + i) % 8
            if nd == 0:
                nd = 8
            nx = x + direction[nd][0]
            ny = y + direction[nd][1]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if beforeGrid[nx][ny] == []:
                    beforeGrid[x][y] = []
                    beforeGrid[nx][ny] = [n, nd]

                    fishList[n] = [n, nd, nx, ny]
                    break
                elif beforeGrid[nx][ny][0] == 0:
                    continue
                else:
                    oFish = [n, nd, x, y]
                    nFish = beforeGrid[nx][ny]

                    beforeGrid[x][y] = nFish
                    beforeGrid[nx][ny] = [n, nd]

                    fishList[oFish[0]] = [n, nd, nx, ny]
                    fishList[nFish[0]] = [nFish[0], nFish[1], x, y]
                    break
    return beforeGrid


def getNextPos(afterGrid, myShark):
    nextPosList = []
    n, d, x, y = myShark
    for i in range(1, 4):
        nx = x + direction[d][0]*i
        ny = y + direction[d][1]*i
        if 0 <= nx < 4 and 0 <= ny < 4:
            if afterGrid[nx][ny] != []:
                fn, fd = afterGrid[nx][ny]
                nextPosList.append([fn, fd, nx, ny])
        else:
            break
    return nextPosList


def dfs(myShark, beforeGrid, score):
    global answer

    afterGrid = fishMove(beforeGrid)

    nextPosList = getNextPos(afterGrid, myShark)

    if nextPosList == []:
        answer = max(answer, score)
        return

    mn, md, mx, my = myShark
    for nextPos in nextPosList:
        nn, nd, nx, ny = nextPos
        afterGrid[mx][my] = []
        afterGrid[nx][ny] = [0, nd]
        dfs([0, nd, nx, ny], deepcopy(afterGrid), score+nn)
        afterGrid[mx][my] = [0, nd]
        afterGrid[nx][ny] = [nn, nd]


answer = 0
score = grid[0][0][0]
shark = [0, grid[0][0][1], 0, 0]
grid[0][0] = [0, shark[1]]
dfs(shark, grid, score)
print(answer)
