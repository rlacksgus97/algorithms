gears = []
for _ in range(4):
    gears.append(list(map(int, input())))

k = int(input())
rotate = []
for _ in range(k):
    rotate.append(list(map(int, input().split())))

def run(gears, index, direction):
    if direction == 1:
        tmp = gears[index][-1]
        gears[index].pop()
        gears[index].insert(0, tmp)
    else:
        tmp = gears[index][0]
        gears[index].pop(0)
        gears[index].append(tmp)

def operate(gears, index, direction):
    if index == -1 or index == 4:
        return
    left = False
    right = False
    if index < 3:
        if gears[index][2] != gears[index+1][6]:
            right = True
    if index > 0:
        if gears[index][6] != gears[index-1][2]:
            left = True
    run(gears, index, direction)
    print(gears)
    if right:
        operate(gears, index+1, -direction)
    if left:
        operate(gears, index-1, -direction)

def point(gears):
    p = 0
    for i in range(4):
        if gears[i][0] == 1:
            p += 2**i
    return p

for rot in rotate:
    operate(gears, rot[0]-1, rot[1])

print(point(gears))