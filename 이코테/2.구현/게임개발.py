n, m = map(int, input().split())
a, b, d = map(int, input().split())
p = []
for _ in range(n):
    p.append(list(map(int, input().split())))

v = [[False] * m for _ in range(n)]
v[a][b] = True

da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]

def turn():
    global d
    if d == 0:
        d = 3
    else:
        d -= 1

count = 1
turn_count = 0
while True:
    turn()
    na = a + da[d]
    nb = b + db[d]
    if p[na][nb] == 0 and v[na][nb] == False:
        a = na
        b = nb
        v[na][nb] = True
        count += 1
        turn_count = 0
        continue
    else:
        turn_count += 1
    if turn_count == 4:
        na = a - da[d]
        nb = b - db[d]
        if p[na][nb] == 0:
            a = na
            b = nb
        else:
            break
        turn_count = 0

print(count)