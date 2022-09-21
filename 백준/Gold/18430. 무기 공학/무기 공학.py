N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cases = [[[-1, 0], [0, -1]], [[-1, 0], [0, 1]],
         [[1, 0], [0, -1]], [[1, 0], [0, 1]]]
visited = [[False for _ in range(M)] for _ in range(N)]
answer = 0


def dfs(x, y, result):
    global answer
    if y == M:
        x += 1
        y = 0
    if x == N:
        answer = max(answer, result)
        return
    if not visited[x][y]:
        for c in cases:
            nx1 = x + c[0][0]
            ny1 = y + c[0][1]
            nx2 = x + c[1][0]
            ny2 = y + c[1][1]
            if 0 <= nx1 < N and 0 <= nx2 < N and 0 <= ny1 < M and 0 <= ny2 < M:
                if not visited[nx1][ny1] and not visited[nx2][ny2]:
                    visited[x][y] = True
                    visited[nx1][ny1] = True
                    visited[nx2][ny2] = True
                    dfs(x, y+1, result + board[x][y] *
                        2+board[nx1][ny1]+board[nx2][ny2])
                    visited[x][y] = False
                    visited[nx1][ny1] = False
                    visited[nx2][ny2] = False
    dfs(x, y+1, result)


dfs(0, 0, 0)
print(answer)
