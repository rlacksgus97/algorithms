import copy

n, m = map(int, input().split())
room = []
for _ in range(n):
    room.append(list(map(int, input().split())))

cctv = []
for i in range(n):
    for j in range(m):
        if room[i][j] not in [0, 6]:
            cctv.append((room[i][j], i, j))

direction = [
    [[0], [1], [2], [3]],
    [[0,2], [1,3]],
    [[0,1], [1,2], [2,3], [3,0]],
    [[0,1,2], [1,2,3], [2,3,0], [3,0,1]],
    [[0,1,2,3]]
]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def watch(x, y, dir, temp):
    for d in dir:
        nx = x
        ny = y
        while True:
            nx += dx[d]
            ny += dy[d]
            if 0<=nx<n and 0<=ny<m and temp[nx][ny] != 6:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = '#'
            else:
                break

answer = n*m
def dfs(room, index):
    global answer

    temp = copy.deepcopy(room)
    if index == len(cctv):
        count = 0
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 0:
                    count += 1
        answer = min(answer, count)
        return
    t, x, y = cctv[index]
    for dir in direction[t-1]:
        watch(x, y, dir, temp)
        dfs(temp, index+1)
        temp = copy.deepcopy(room)

dfs(room, 0)
print(answer)