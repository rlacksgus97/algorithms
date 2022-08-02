from collections import deque

def rotate(board,x,y,l):
    newBoard = [[0 for _ in range(l)] for _ in range(l)]
    for i in range(l):
        for j in range(l):
            newBoard[j][l-1-i] = board[x+i][y+j]
    return newBoard

def draw(board, newBoard, x, y, l):
    for i in range(l):
        for j in range(l):
            board[x+i][y+j] = newBoard[i][j]
    return board

def magic(board, level):
    l = 2**level
    for i in range(0, len(board), l):
        for j in range(0, len(board), l):
            newBoard = rotate(board,i,j,l)
            board = draw(board, newBoard, i, j, l)
    return board

def check(board,x,y):
    count = 0
    for d in [[-1,0],[1,0],[0,-1],[0,1]]:
        nx = x+d[0]
        ny = y+d[1]
        if 0<=nx<len(board) and 0<=ny<len(board):
            if board[nx][ny] > 0:
                count += 1
    if count >= 3:
        return False
    else:
        return True

def melt(board):
    melt = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] > 0 and check(board,i,j):
                melt.append((i,j))
    for m in melt:
        board[m[0]][m[1]] -= 1

def getSize(visited,i,j):
    q = deque([(i,j)])
    visited[i][j] = True
    count = 0
    while q:
        x, y = q.popleft()
        count += 1
        for d in [[-1,0],[1,0],[0,-1],[0,1]]:
            nx = x+d[0]
            ny = y+d[1]
            if 0<=nx<len(board) and 0<=ny<len(board):
                if board[nx][ny] > 0 and visited[nx][ny] == False:
                    q.append((nx,ny))
                    visited[nx][ny] = True
    return count

N, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2**N)]
L = list(map(int, input().split()))

for i in range(Q):
    board = magic(board, L[i])
    melt(board)

totalIce = 0
for i in range(2**N):
    for j in range(2**N):
        totalIce += board[i][j]

visited = [[False for _ in range(2**N)] for _ in range(2**N)]
maxSize = 0
for i in range(2**N):
    for j in range(2**N):
        if board[i][j] > 0 and visited[i][j] == False:
            maxSize = max(maxSize, getSize(visited,i,j))

print(totalIce)
print(maxSize)
