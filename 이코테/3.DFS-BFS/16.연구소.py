from itertools import combinations

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

wall_cases = list(combinations(empty, 3))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < n and nx > -1 and ny < m and ny > -1:
            if test[nx][ny] == 0:
                test[nx][ny] = 2
                dfs(nx, ny)

def score():
    count = 0
    for i in range(n):
        for j in range(m):
            if test[i][j] == 0:
                count += 1
    return count

answer = 0
for walls in wall_cases:

    for i in range(n):
        for j in range(m):
            test[i][j] = lab[i][j]

    for w in walls:
        test[w[0]][w[1]] = 1
    
    for i in range(n):
        for j in range(m):
            if test[i][j] == 2:
                dfs(i, j)
    
    count = score()
    answer = max(answer, count)

print(answer)