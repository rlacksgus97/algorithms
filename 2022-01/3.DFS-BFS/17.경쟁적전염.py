from collections import deque

n, k = map(int, input().split())

board = []
virus = []
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j] != 0:
            virus.append((board[i][j], 0, i, j))
virus.sort()
q = deque(virus)

s, x, y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
    v, t, a, b = q.popleft()
    if t == s:
        break
    for i in range(4):
        da = a + dx[i]
        db = b + dy[i]
        if da < n and da > -1 and db < n and db > -1 and board[da][db] == 0:
            board[da][db] = v
            q.append((v, t+1, da, db))

print(board[x-1][y-1])
