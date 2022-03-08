n = int(input())
dragon_curves = []
for _ in range(n):
    dragon_curves.append(list(map(int, input().split())))

dragon_moves = []
for dc in dragon_curves:
    move = [dc[2]]
    for _ in range(dc[3]):
        next_move = []
        for i in range(len(move)-1, -1, -1):
            if move[i] == 0:
                next_move.append(1)
            elif move[i] == 1:
                next_move.append(2)
            elif move[i] == 2:
                next_move.append(3)
            else:
                next_move.append(0)
        move.extend(next_move)
    dragon_moves.append(move)

board = [[0 for _ in range(101)] for _ in range(101)]
for i in range(n):
    x, y = dragon_curves[i][1], dragon_curves[i][0]
    board[x][y] = 1
    for m in dragon_moves[i]:
        if m == 0:
            y += 1
        elif m == 1:
            x -= 1
        elif m == 2:
            y -= 1
        elif m == 3:
            x += 1
        board[x][y] = 1

answer = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1 and board[i][j+1] == 1 and board[i+1][j] == 1 and board[i+1][j+1] == 1:
            answer += 1

print(answer)