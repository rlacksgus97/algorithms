#2022-01-07 13:35-13:50
from collections import deque

t = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(i,j):
    q = deque([(i,j)])
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if field[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append((nx, ny))

for _ in range(t):
    m, n, k = map(int, input().split())
    field = [[0]*m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        field[x][y] = 1

    visited = [[False]*m for _ in range(n)]

    count = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1 and visited[i][j] == False:
                bfs(i,j)
                count += 1
    print(count)