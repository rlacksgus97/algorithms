def rotate(t):
    n = len(t)
    m = len(t[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-1-i] = t[i][j]
    return result

def reflect(t):
    n = len(t)
    m = len(t[0])
    result = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[i][m-1-j] = t[i][j]
    return result

def moveAndmatch(b, t):
    sum = 0
    for x in range(len(b)-len(t)+1):
        for y in range(len(b[0])-len(t[0])+1):
            sum = max(match(x, y, b, t), sum)
    return sum

def match(x, y, b, t):
    sum = 0
    for i in range(len(t)):
        for j in range(len(t[0])):
            if t[i][j] == 1:
                sum += b[x+i][y+j]
    return sum

tet1 = [[1, 1, 1, 1]]
tet2 = [[1, 1],
        [1, 1]]
tet3 = [[1, 0],
        [1, 0],
        [1, 1]]
tet4 = [[1, 0],
        [1, 1],
        [0, 1]]
tet5 = [[1, 1, 1],
        [0, 1, 0]]

tetlist = [tet1, tet2, tet3, tet4, tet5]

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

sum = 0
for tet in tetlist:
    for _ in range(2):
        tet = reflect(tet)
        for _ in range(4):
            tet = rotate(tet)
            sum = max(moveAndmatch(board, tet), sum)
