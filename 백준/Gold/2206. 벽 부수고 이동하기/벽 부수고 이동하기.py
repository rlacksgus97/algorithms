from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
answer = 1e9

visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
q = deque([[0,0,0]])
visited[0][0][0] = 1
while q:
    x, y, layer = q.popleft()
    for d in [[1,0],[-1,0],[0,1],[0,-1]]:
        nx = x + d[0]
        ny = y + d[1]
        if 0<=nx<n and 0<=ny<m:
            if board[nx][ny] == 0:
                if visited[nx][ny][layer] == 0:
                    q.append([nx, ny, layer])
                    visited[nx][ny][layer] = visited[x][y][layer] + 1
            else:
                if layer == 0:
                    q.append([nx, ny, 1])
                    visited[nx][ny][1] = visited[x][y][0] + 1

first, second = visited[n-1][m-1]
if first == 0 and second == 0:
    print(-1)
elif first == 0:
    print(second)
elif second == 0:
    print(first)
else:
    print(min(first,second))