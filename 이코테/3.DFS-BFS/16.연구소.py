n, m = map(int, input().split())
lab = []
for _ in range(n):
    lab.append(list(map(int, input().split())))
test = [[0]*m for _ in range(n)]

empty = []
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            empty.append((i,j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < n and nx > -1 and ny < m and ny > -1:
            if test[nx][ny] == 0:
                test[nx][ny] = 2
                virus(nx, ny)

def score():
    count = 0
    for i in range(n):
        for j in range(m):
            if test[i][j] == 0:
                count += 1
    return count

answer = 0
def dfs(wall):
    global answer
    if wall == 3:
        for i in range(n):
            for j in range(m):
                test[i][j] = lab[i][j]
        for i in range(n):
            for j in range(m):
                if test[i][j] == 2:
                    virus(i, j)
        answer = max(answer, score())
        return
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                wall += 1
                dfs(wall)
                lab[i][j] = 0
                wall -= 1
dfs(0)
print(answer)