def dfs(i, result):
    global answer
    if i == 11:
        answer = max(answer, result)
        return
    for j in range(11):
        stat = players[i][j]
        if stat != 0 and visited[j] == False:
            visited[j] = True
            dfs(i+1, result+stat)
            visited[j] = False


C = int(input())
for _ in range(C):
    players = [list(map(int, input().split())) for _ in range(11)]
    visited = [False for _ in range(11)]
    answer = 0
    dfs(0, 0)
    print(answer)
