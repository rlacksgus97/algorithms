def install_row(x, y):
    cnt = 0
    for i in range(l):
        if board[x][y] == board[x][y+i]:
            cnt += 1
        else:
            break
        if check[x][y+i] == 1:
            return False
    if cnt == l:
        for i in range(l):
            check[x][y+i] = 1
        return True
    else:
        return False

def install_col(x, y):
    cnt = 0
    for i in range(l):
        if board[x][y] == board[x+i][y]:
            cnt += 1
        else:
            break
        if check[x+i][y] == 1:
            return False
    if cnt == l:
        for i in range(l):
            check[x+i][y] = 1
        return True
    else:
        return False

def check_row(index):
    for i in range(n-1):
        if board[index][i+1] - board[index][i] == 1:
            if i-(l-1) >= 0:
                if not install_row(index, i-(l-1)):
                    return False
            else:
                return False
        elif board[index][i] - board[index][i+1] == 1:
            if i+1+(l-1) <= n-1:
                if not install_row(index, i+1):
                    return False
            else:
                return False
        elif board[index][i] != board[index][i+1]:
            return False
    return True

def check_col(index):
    for i in range(n-1):
        if board[i+1][index] - board[i][index] == 1:
            if i-(l-1) >= 0:
                if not install_col(i-(l-1), index):
                    return False
            else:
                return False
        elif board[i][index] - board[i+1][index] == 1:
            if i+1+(l-1) <= n-1:
                if not install_col(i+1, index):
                    return False
            else:
                return False
        elif board[i][index] != board[i+1][index]:
            return False
    return True

n, l = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

answer = 0
for i in range(n):
    check = [[0 for _ in range(n)] for _ in range(n)]
    if check_row(i):
        answer += 1
for i in range(n):
    check = [[0 for _ in range(n)] for _ in range(n)]
    if check_col(i):
        answer += 1
print(answer)