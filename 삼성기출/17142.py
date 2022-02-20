from itertools import combinations
from collections import deque

n, m = map(int, input().split())
lab = []
for _ in range(n):
    lab.append(list(map(int, input().split())))

wall = []
virus = []
for i in range(n):
    for j in range(n):
        if lab[i][j] == 2:
            virus.append([i,j,0])
        elif lab[i][j] == 1:
            wall.append([i,j])
activate = list(combinations(virus, m))

def setting(mylab, act):
    for i,j,t in act:
        mylab[i][j] = 0
    for i,j,t in virus:
        if mylab[i][j] != 0:
            mylab[i][j] = '*'
    for i,j in wall:
        mylab[i][j] = '-'

def spread(act, mylab):
    time = 0
    act = deque(act)
    while act:
        x, y, t = act.popleft()
        for i, j in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx = x+i
            ny = y+j
            if 0<=nx<n and 0<=ny<n:
                if mylab[nx][ny] == -1:
                    mylab[nx][ny] = t + 1
                    time = max(time, mylab[nx][ny])
                    act.append((nx,ny,t+1))
                elif mylab[nx][ny] == '*':
                    mylab[nx][ny] = 0
                    act.append((nx,ny,t+1))
    if check(mylab):
        return time
    else:
        return -1

def check(mylab):
    for i in range(n):
        for j in range(n):
            if mylab[i][j] == -1:
                return False
    return True
    

time = n*n+1
for act in activate:
    mylab = [[-1 for _ in range(n)] for _ in range(n)]
    setting(mylab, list(act))
    mytime = spread(act, mylab)
    if mytime != -1:
        time = min(time, mytime)

if time == n*n+1:
    print(-1)
else:
    print(time)