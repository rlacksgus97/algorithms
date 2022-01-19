n, m = map(int, input().split())
castle = []
for _ in range(n):
    castle.append(list(input()))

row = 0
for i in range(n):
    if 'X' not in castle[i]:
        row += 1

col = 0
for i in range(m):
    flag = True
    for j in range(n):
        if castle[j][i] == 'X':
            flag = False
            break
    if flag:
        col += 1

print(max(row, col))