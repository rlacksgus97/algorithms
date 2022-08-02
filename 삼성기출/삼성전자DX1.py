from collections import deque

def bfs(land, visited, i, j, year):
    visited[i][j] = True
    q = deque([(i,j)])
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<len(land) and 0<=ny<len(land) and land[nx][ny] > year and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx,ny))
    return visited

T = int(input())
for t in range(T):
    answer = 1
    N = int(input())
    land = [list(map(int, input().split())) for _ in range(N)]
    for year in range(1, 100):
        cnt = 0
        visited = [[False for _ in range(len(land))] for _ in range(len(land))]
        for i in range(N):
            for j in range(N):
                if land[i][j] > year and visited[i][j] == False:
                    cnt += 1
                    visited = bfs(land, visited, i, j, year)
        answer = max(answer, cnt)
    print(t+1, answer)