N, M, K = map(int, input().split())
grid = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    grid[r-1][c-1].append([m, s, d])

direction = [[-1, 0], [-1, 1], [0, 1], [1, 1],
             [1, 0], [1, -1], [0, -1], [-1, -1]]


def move():
    newGrid = [[[] for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            while grid[x][y]:
                m, s, d = grid[x][y].pop()
                nx = (x + direction[d][0]*s) % N
                ny = (y + direction[d][1]*s) % N
                newGrid[nx][ny].append([m, s, d])
    return newGrid


def change():
    newGrid = [[[] for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if len(grid[x][y]) == 0:
                continue
            if len(grid[x][y]) == 1:
                newGrid[x][y].append(grid[x][y][0])
                continue
            total_m, total_s, total_d = 0, 0, []
            for m, s, d in grid[x][y]:
                total_m += m
                total_s += s
                total_d.append(d)
            odd = 0
            even = 0
            for td in total_d:
                if td % 2 == 1:
                    odd += 1
                else:
                    even += 1

            if total_m//5 < 1:
                continue

            if odd == len(total_d) or even == len(total_d):
                for i in [0, 2, 4, 6]:
                    newGrid[x][y].append(
                        [total_m//5, total_s//len(total_d), i])
            else:
                for i in [1, 3, 5, 7]:
                    newGrid[x][y].append(
                        [total_m//5, total_s//len(total_d), i])
    return newGrid


for _ in range(K):
    grid = move()
    grid = change()

answer = 0
for x in range(N):
    for y in range(N):
        for z in range(len(grid[x][y])):
            answer += grid[x][y][z][0]
print(answer)
