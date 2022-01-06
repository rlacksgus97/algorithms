p = input()

dx = [-2, -2, 2, 2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

x = int(ord(p[0])-ord('a'))
y = int(p[1])-1

count = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx <= 7 and nx >= 0 and ny <= 7 and ny >= 0:
        count += 1

print(count)
