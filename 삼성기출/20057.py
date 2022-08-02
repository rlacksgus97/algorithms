def getDirections(x,y,dir,dist):
    directions = []
    dir = 0
    dist = 0
    while x >= 0 and y >= 0:
        if dir == 4:
            dir = 0
        if dir == 0:
            dist += 1
        elif dir == 2:
            dist += 1
        for _ in range(dist):
            x = x + dx[dir]
            y = y + dy[dir]
            if x < 0 or y < 0:
                break
            directions.append(dir)
        dir += 1
    return directions

n = int(input())
yard = [list(map(int, input().split())) for _ in range(n)]
answer = 0

x = n//2
y = n//2

dx = [0,1,0,-1]
dy = [-1,0,1,0]

sandMove = [[[-1,0,1],[1,0,1],[-2,-1,2],[-1,-1,7],[1,-1,7],[2,-1,2],[-1,-2,10],[1,-2,10],[0,-3,5],[0,-1],[0,-2]],
            [[0,-1,1],[0,1,1],[1,-2,2],[1,-1,7],[1,1,7],[1,2,2],[2,-1,10],[2,1,10],[3,0,5],[1,0],[2,0]],
            [[-1,0,1],[1,0,1],[-2,1,2],[-1,1,7],[1,1,7],[2,1,2],[-1,2,10],[1,2,10],[0,3,5],[0,1],[0,2]],
            [[0,-1,1],[0,1,1],[-1,-2,2],[-1,-1,7],[-1,1,7],[-1,2,2],[-2,-1,10],[-2,1,10],[-3,0,5],[-1,0],[-2,0]]]

directions = getDirections(x,y,0,0)

for d in directions:
    nx = x + dx[d]
    ny = y + dy[d]
    sand = yard[nx][ny]
    total = 0
    for i in range(9):
        sm = sandMove[d][i]
        sx, sy, p = sm
        amount = int(sand*0.01*p)
        if 0<=x+sx<n and 0<=y+sy<n:
            yard[x+sx][y+sy] += amount
        else:
            answer += amount
        total += amount
    yard[nx][ny] -= total
    ax = x + sandMove[d][-1][0]
    ay = y + sandMove[d][-1][1]
    if 0<=ax<n and 0<=ay<n:
        yard[ax][ay] += yard[nx][ny]
    else:
        answer += yard[nx][ny]
    yard[nx][ny] = 0
    x = nx
    y = ny

print(answer)
