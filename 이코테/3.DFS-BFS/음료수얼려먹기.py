n, m = map(int, input.split())

tray = []
for _ in range(n):
    tray.append(list(map(int, input().split())))


def dfs(i, j):
    if i >= n or i < 0 or j >= m or j < 0:
        return False
    if tray[i][j] == False:
        tray[i][j] = True
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i+1, j)
        dfs(i, j-1)
        return True
    return False


answer = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            answer += 1

print(answer)
