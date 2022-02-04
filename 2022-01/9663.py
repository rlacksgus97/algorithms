n = int(input())

def attackable(row, col):
    for r in range(row):
        if board[r] == col:
            return False
        if abs(board[r]-col) == abs(row-r):
            return False
    return True

answer = 0
def rec_func(row):
    global answer
    if row == n:
        answer += 1
        return
    for c in range(n):
        if attackable(row, c):
            board[row] = c
            rec_func(row+1)
            # board[row] = -1

board = [-1 for _ in range(n)]
rec_func(0)
print(answer)