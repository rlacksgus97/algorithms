n, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
horses = []
for _ in range(k):
    horses.append(list(map(int, input().split())))

state = [[[] for _ in range(n)] for _ in range(n)]
for i in range(k):
    state[horses[i][0]-1][horses[i][1]-1].append(i)

def check_end():
    for i in range(n):
        for j in range(n):
            if len(state[i][j]) >= 4:
                return True
    return False

def find(hi):
    for x in range(n):
        for y in range(n):
            for z in range(len(state[x][y])):
                if state[x][y][z] == hi:
                    return (x, y, z)

def blueOrOut(hi, x, y, tmp):
    if horses[hi][2] == 1:
        horses[hi][2] = 2
        y -= 2
    elif horses[hi][2] == 2:
        horses[hi][2] = 1
        y += 2
    elif horses[hi][2] == 3:
        horses[hi][2] = 4
        x += 2
    else:
        horses[hi][2] = 3
        x -= 2
    
    if 0<=x<n and 0<=y<n:
        if board[x][y] == 1:
            tmp.reverse()
            state[x][y].extend(tmp)
        elif board[x][y] == 0:
            state[x][y].extend(tmp)
        else:
            if horses[hi][2] == 1:
                y -= 1
            elif horses[hi][2] == 2:
                y += 1
            elif horses[hi][2] == 3:
                x += 1
            else:
                x -= 1
            state[x][y].extend(tmp)
    else:
        if horses[hi][2] == 1:
                y -= 1
        elif horses[hi][2] == 2:
            y += 1
        elif horses[hi][2] == 3:
            x += 1
        else:
            x -= 1
        state[x][y].extend(tmp)

def move(hi, x, y, z, tmp):
    if horses[hi][2] == 1:
        y += 1
    elif horses[hi][2] == 2:
        y -= 1
    elif horses[hi][2] == 3:
        x -= 1
    else:
        x += 1
    
    if 0<=x<n and 0<=y<n:
        if board[x][y] == 1:
            tmp.reverse()
            state[x][y].extend(tmp)
        elif board[x][y] == 2:
            blueOrOut(hi, x, y, tmp)
        else:
            state[x][y].extend(tmp)
    else:
        blueOrOut(hi, x, y, tmp)

turn = 0
while True:
    turn += 1
    finish = False
    for i in range(k):
        x, y, z = find(i)
        tmp = state[x][y][z:]
        state[x][y] = state[x][y][:z]
        move(i,x,y,z,tmp)
        if check_end():
            finish = True
            break
    if finish or turn > 1000:
        break
if turn > 1000:
    print(-1)
else:
    print(turn)