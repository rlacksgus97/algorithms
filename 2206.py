from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

walls = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            walls.append((i, j))

def bfs(array):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    q = deque([(0, 0)])
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < n and nx >= 0 and ny < m and ny >= 0 and array[nx][ny] == 0 and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    return visited[-1][-1]

ans = 1000000
for w in walls:
    board[w[0]][w[1]] = 0
    c = bfs(board)
    if c != 0:
        ans = min(ans, c)
    board[w[0]][w[1]] = 1

if ans == 1000000:
    print(-1)
else:
    print(ans)