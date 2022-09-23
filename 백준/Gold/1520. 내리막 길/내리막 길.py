import sys
sys.setrecursionlimit(10**9)


def dfs(x, y):
    if x == M-1 and y == N-1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < M and 0 <= ny < N and road[x][y] > road[nx][ny]:
            dp[x][y] += dfs(nx, ny)
    return dp[x][y]


M, N = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)]
print(dfs(0, 0))
