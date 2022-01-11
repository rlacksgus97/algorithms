from collections import deque

n = int(input())
pic = []
for _ in range(n):
    pic.append(list(input()))

visited = [[0]*n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(a, b):
    q = deque([(a,b)])
    visited[a][b] = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if pic[nx][ny] == pic[x][y] and visited[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = 1

count = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i,j)
            count += 1
print(count, end=' ')

for i in range(n):
    for j in range(n):
        if pic[i][j] == 'G':
            pic[i][j] = 'R'

visited = [[0]*n for _ in range(n)]
count = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i,j)
            count += 1
print(count, end=' ')