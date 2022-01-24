n, m, k = map(int, input().split())
ground = [[5 for _ in range(n)] for _ in range(n)]
nutrition = []
for _ in range(n):
    nutrition.append(list(map(int, input().split())))
tree = []
for _ in range(m):
    x, y, z = map(int, input().split())
    tree.append([x-1,y-1,z])

def spring():
    for t in tree:
        if t[2] == -1:
            continue
        if ground[t[0]][t[1]] >= t[2]:
            ground[t[0]][t[1]] -= t[2]
            t[2] += 1 
        else:
            dead.append(t)
            t[2] = -1

def summer():
    for d in dead:
        ground[d[0]][d[1]] += d[2]//2

def fall():
    for t in tree:
        if t[2] % 5 == 0:
            x, y = t[0], t[1]
            for d in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                nx = x + d[0]
                ny = y + d[1]
                if 0<=nx<n and 0<=ny<n:
                    tree.append([nx,ny,1])

def winter():
    for i in range(n):
        for j in range(n):
            ground[i][j] += nutrition[i][j]

dead = []
for _ in range(k):
    tree.sort()
    spring()
    summer()
    dead = []
    fall()
    winter()

    # test = [[0 for _ in range(n)] for _ in range(n)]
    # for t in tree:
    #     if t[2] != -1:
    #         test[t[0]][t[1]] += 1

    for t in tree:
        print(t)
    print()

    print(dead)

    for i in range(n):
        print(ground[i])
    print()

    # for i in range(n):
    #     print(test[i])
    # print()
    


count = 0
for t in tree:
    if t[2] != -1:
        count += 1
print(count)
