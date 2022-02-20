from collections import deque

rl, cl, ml = map(int, input().split())
answer = 0
sharks = deque([])
for _ in range(ml):
    sharks.append(list(map(int, input().split())))

def place():
    for shark in sharks:
        r, c, s, d, z = shark
        if water[r][c] == 0:
            water[r][c] = [s,d,z]
        else:
            if water[r][c][2] < z:
                water[r][c] = [s,d,z]

def catch(pos):
    global answer
    for i in range(1, rl+1):
        if water[i][pos] != 0:
            s, d, z = water[i][pos]
            answer += z
            sharks.remove([i, pos, s, d, z])
            break

def move(shark):
    r, c, s, d, z = shark
    for _ in range(s):
        if d == 1:
            r -= 1
        elif d == 2:
            r += 1
        elif d == 3:
            c += 1
        else:
            c -= 1

        if r == 0:
            r = 2
            d = 2
        elif r == rl+1:
            r = rl-1
            d = 1

        if c == 0:
            c = 2
            d = 3
        elif c == cl+1:
            c = cl-1
            d = 4
    return [r, c, s, d, z]

for pos in range(1, cl+1):
    water = [[0 for _ in range(cl+1)] for _ in range(rl+1)]
    place()
    catch(pos)
    for _ in range(len(sharks)):
        sharks.append(move(sharks.popleft()))

print(answer)