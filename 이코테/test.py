tet3 = [[1, 0],
        [1, 0],
        [1, 1]]

tet4 = [[1, 0],
        [1, 1],
        [0, 1]]

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

for _ in range(2):
    tet3 = reflect(tet3)
    for _ in range(4):
        tet3 = rotate(tet3)
        for i in range(len(tet3)):
            for j in range(len(tet3[0])):
                print(tet3[i][j], end=' ')
            print()
