from collections import deque

space = [[[0,0] for _ in range(4)] for _ in range(4)]
for i in range(4):
    info = list(map(int, input().split()))
    for j in range(0, 8, 2):
        space[i][j//2][0] = info[j]
        space[i][j//2][1] = info[j+1]

dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

def get_location(fish_num):
    for i in range(4):
        for j in range(4):
            if space[i][j][0] == fish_num:
                return [i,j]
    return [-1,-1]

def fish_move(x, y):
    direction = space[x][y][1]-1
    for _ in range(8):
        direction += 1
        if direction == 9:
            direction = 1
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0<=nx<4 and 0<=ny<4 and space[nx][ny][0] != 0:
            space[x][y][1] = direction
            space[x][y], space[nx][ny] = space[nx][ny], space[x][y]
            return

def flow():
    for i in range(1, 17):
        location = get_location(i)
        if location[0] == -1:
            continue
        else:
            fish_move(location[0], location[1])

def shark_check():
    move = []
    x, y = get_location(0)
    direction = space[x][y][1]
    for _ in range(4):
        x += dx[direction]
        y += dy[direction]
        if 0<=x<4 and 0<=y<4 and space[x][y] != -1:
            move.append([x,y])
    return move

def shark_move(move):
    global answer
    if len(move) == 0:
        return
    else:
        while move:
            x, y = move.popleft()
            answer += space[x][y][0]
            space[x][y][0] = 0
            flow()
            candidate = deque(shark_check())
            shark_move(candidate)



answer = 0
answer += space[0][0][0]
space[0][0][0] = 0

while True:
    shark_move()