n = int(input())

def attackable(row, col, board):
    for r in range(row):
        if board[r][col] == 1:
            return False
    for x in range(1, min(row, col)+1):
        if (0 <= col-x and board[row-x][col-x] == 1) or (col+x < n and board[row-x][col+x] == 1):
            return False
    return True

answer = 0
def rec_func(row, board):
    global answer
    if row == n:
        answer += 1
        # for i in range(n):
        #     print(board[i])
        # print()
        return
    for col in range(n):
        if attackable(row, col, board):
            board[row][col] = 1
            rec_func(row+1, board)
            board[row][col] = 0

for i in range(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    board[0][i] = 1
    rec_func(i, board)
print(answer)