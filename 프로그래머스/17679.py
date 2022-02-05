def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i] = list(board[i])
        
    def check_point(m, n, board):
        check = [[0 for _ in range(n)] for _ in range(m)]
        point = 0
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != '0':
                    if board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j] and board[i][j] == board[i+1][j+1]:
                        check[i][j] = 1
                        check[i][j+1] = 1
                        check[i+1][j] = 1
                        check[i+1][j+1] = 1
        for i in range(m):
            for j in range(n):
                if check[i][j] == 1:
                    board[i][j] = '0'
                    point += 1
        return point
    
    def move_down(board):
        for j in range(n):
            temp = []
            for i in range(m):
                if board[i][j] != '0':
                    temp.append(board[i][j])
            for i in range(m-len(temp)):
                board[i][j] = '0'
            for i in range(len(temp)):
                board[m-len(temp)+i][j] = temp[i]
    
    while True:
        p = check_point(m, n, board)
        if p == 0:
            break
        else:
            answer += p
        move_down(board)
    
    return answer