#2022-01-07 18:40-
n, l = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

set_r = set()
for i in range(n):
    same = 1
    for j in range(n-1):
        if board[i][j] - board[i][j+1] < -1:
            set_r.add(i)
            print('case1 = i,j', i,j)
            break
        elif board[i][j] - board[i][j+1] == -1:
            if same >= l:
                same = 1
            else:
                set_r.add(i)
                print('case2 = i,j', i,j,same)
                break
        else:
            same += 1

print(n, set_r)

for i in range(n):
    same = 1
    for j in range(n-1, 0, -1):
        if board[i][j] - board[i][j-1] < -1:
            set_r.add(i)
            print('case1 = i,j', i,j)
            break
        elif board[i][j] - board[i][j-1] == -1:
            if same >= l:
                same = 1
            else:
                set_r.add(i)
                print('case2 = i,j', i,j,same)
                break
        else:
            same += 1

print(n, set_r)

set_c = set()