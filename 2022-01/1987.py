r, c = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(input()))

answer = 1
def rec_func(x, y, history, count):
    global answer
    for d in [(-1,0),(0,1),(1,0),(0,-1)]:
        nx = x + d[0]
        ny = y + d[1]
        if 0<=nx<r and 0<=ny<c and board[nx][ny] not in history:
            history.append(board[nx][ny])
            rec_func(nx, ny, history, count+1)
            history.remove(board[nx][ny])
    answer = max(answer, count)

rec_func(0, 0, [board[0][0]], 1)
print(answer)
