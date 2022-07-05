import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
ground = []
for _ in range(n):
    ground.append(list(map(int, input().split())))

min_t = 1e9
height = -1
for h in range(257):
    need = 0
    remain = 0
    for i in range(n):
        for j in range(m):
            if ground[i][j] >= h:
                remain += ground[i][j]-h
            else:
                need += h-ground[i][j]
    if need <= remain+b:
        time = need + remain*2
        if min_t >= time:
            min_t = time
            height = h

print(min_t, height)
