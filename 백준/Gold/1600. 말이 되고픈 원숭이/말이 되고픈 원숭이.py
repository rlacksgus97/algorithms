from collections import deque

K = int(input())
W, H = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]

horse = [[-2, -1], [-1, -2], [1, -2],
         [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1]]
monkey = [[-1, 0], [1, 0], [0, 1], [0, -1]]

answer = -1
q = deque([[0, 0, 0, K]])
visited = [[-1 for _ in range(W)] for _ in range(H)]
while q:
    x, y, d, k = q.popleft()
    if x == H-1 and y == W-1:
        answer = d
        break

    if k >= 1:
        for hx, hy in horse:
            nx = x + hx
            ny = y + hy
            if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] == 0:
                if visited[nx][ny] < k-1:
                    visited[nx][ny] = k-1
                    q.append([nx, ny, d+1, k-1])

    for mx, my in monkey:
        nx = x + mx
        ny = y + my
        if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] == 0:
            if visited[nx][ny] < k:
                visited[nx][ny] = k
                q.append([nx, ny, d+1, k])

print(answer)
