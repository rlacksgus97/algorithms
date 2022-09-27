# 16:40
from collections import deque

N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
d = [[-1, 0], [0, 1], [1, 0], [0, -1]]

dice = [1, 2, 3, 5, 4, 1]
x, y = 0, 0


def roll(x, y, dice):
    direction = dice[-1]
    if x+d[direction][0] == -1 or y+d[direction][1] == -1 or x+d[direction][0] == N or y+d[direction][1] == M:
        direction = (direction+2) % 4
    x += d[direction][0]
    y += d[direction][1]

    if direction == 0:
        dice = [dice[3], dice[0], dice[2], 7-dice[0], dice[4], direction]
    elif direction == 1:
        dice = [dice[4], dice[1], dice[0], dice[3], 7-dice[0], direction]
    elif direction == 2:
        dice = [dice[1], 7-dice[0], dice[2], dice[0], dice[4], direction]
    else:
        dice = [dice[2], dice[1], 7-dice[0], dice[3], dice[0], direction]
    return [x, y, dice]


def gain(a, b):
    num = grid[a][b]
    count = 1
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[a][b] = 1
    q = deque([[a, b]])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and grid[nx][ny] == num:
                visited[nx][ny] = 1
                q.append([nx, ny])
                count += 1
    return grid[x][y] * count


def turn(x, y, dice):
    A = 7 - dice[0]
    B = grid[x][y]
    if A > B:
        dice[-1] += 1
        if dice[-1] == 4:
            dice[-1] = 0
    elif A < B:
        dice[-1] -= 1
        if dice[-1] == -1:
            dice[-1] = 3
    return dice


point = 0
for _ in range(K):
    x, y, dice = roll(x, y, dice)
    point += gain(x, y)
    dice = turn(x, y, dice)
print(point)
