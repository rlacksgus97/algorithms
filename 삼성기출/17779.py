n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

def calculate(r, c, d1, d2, section):
    section = draw(r, c, d1, d2, section)
    section = group(r, c, d1, d2, section)
    population = [0 for _ in range(5)]
    for i in range(n):
        for j in range(n):
            if section[i][j] == 1:
                population[0] += a[i][j]
            if section[i][j] == 2:
                population[1] += a[i][j]
            if section[i][j] == 3:
                population[2] += a[i][j]
            if section[i][j] == 4:
                population[3] += a[i][j]
            if section[i][j] == 5:
                population[4] += a[i][j]
    return max(population)-min(population)

def draw(r, c, d1, d2, section):
    section[r][c] = 5
    for i in range(d1+1):
        if r+i < n and c-i >= 0:
            section[r+i][c-i] = 5
    for i in range(d2+1):
        if r+i < n and c+i < n:
            section[r+i][c+i] = 5
    for i in range(d2+1):
        if r+d1+i < n and c-d1+i<n:
            section[r+d1+i][c-d1+i] = 5
    for i in range(d1+1):
        if r+d2+i < n and c+d2-i >= 0:
            section[r+d2+i][c+d2-i] = 5
    section = fill(r, c, d1, d2, section)
    return section

def fill(r, c, d1, d2, section):
    for i in range(r+1, r+d1+d2):
        for j in range(n):
            if section[i][j] == 5:
                x = i
                y = j+1
                break
        while section[x][y] == 0:
            section[x][y] = 5
            y += 1
    return section

def group(r, c, d1, d2, section):
    for i in range(n):
        for j in range(n):
            if section[i][j] != 5:
                if 0<=i<r+d1 and 0<=j<=c:
                    section[i][j] = 1
                if 0<=i<=r+d2 and c<j<n:
                    section[i][j] = 2
                if r+d1<=i<n and 0<=j<c-d1+d2:
                    section[i][j] = 3
                if r+d2<i<n and c-d1+d2<=j<n:
                    section[i][j] = 4
    return section

answer = 100*400
for x in range(n):
    for y in range(n):
        for z1 in range(1, n):
            for z2 in range(1, n):
                if 0<=x<x+z1+z2<n and 0<=y-z1<y<y+z2<n:
                    section = [[0 for _ in range(n)] for _ in range(n)]
                    answer = min(answer, calculate(x,y,z1,z2,section))
print(answer)