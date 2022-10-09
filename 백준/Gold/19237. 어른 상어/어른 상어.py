# 15:40
N, M, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
shark_dir = [0] + list(map(int, input().split()))
priorities = [[list(map(int, input().split()))
               for _ in range(4)] for _ in range(M)]
smell = [[[] for _ in range(N)] for _ in range(N)]

# 최초 냄새 세팅
for i in range(N):
    for j in range(N):
        if grid[i][j] != 0:
            smell[i][j] = [grid[i][j], k]

direction = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]]


def isDone():
    for i in range(N):
        for j in range(N):
            if grid[i][j] > 1:
                return False
    return True


def getNextPos(sn, sd, x, y):
    # 빈 칸
    for d in priorities[sn-1][sd-1]:
        nx = x + direction[d][0]
        ny = y + direction[d][1]
        if 0 <= nx < N and 0 <= ny < N:
            if smell[nx][ny] == []:
                shark_dir[sn] = d
                return [nx, ny]

    # 자기 냄새
    for d in priorities[sn-1][sd-1]:
        nx = x + direction[d][0]
        ny = y + direction[d][1]
        if 0 <= nx < N and 0 <= ny < N:
            if smell[nx][ny] != [] and smell[nx][ny][0] == sn:
                shark_dir[sn] = d
                return [nx, ny]


def move():
    newGrid = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if grid[i][j] != 0:
                sn = grid[i][j]
                sd = shark_dir[sn]
                ni, nj = getNextPos(sn, sd, i, j)
                if newGrid[ni][nj] == 0:
                    newGrid[ni][nj] = sn
                else:
                    newGrid[ni][nj] = min(newGrid[ni][nj], sn)
    return newGrid


def stink():
    for i in range(N):
        for j in range(N):
            if grid[i][j] != 0:
                smell[i][j] = [grid[i][j], k+1]


def decrease():
    for i in range(N):
        for j in range(N):
            if smell[i][j] != []:
                smell[i][j][1] -= 1
                if smell[i][j][1] == 0:
                    smell[i][j] = []


def printGrid(g):
    for row in g:
        print(row)
    print()


time = 0
while not isDone() and time < 1001:
    grid = move()
    stink()
    decrease()
    # printGrid(grid)
    # printGrid(smell)
    time += 1
if time == 1001:
    print(-1)
else:
    print(time)
