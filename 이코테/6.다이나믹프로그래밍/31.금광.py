t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    gold = list(map(int, input().split()))

    dp = [[0]*m for _ in range(n)]
    idx = 0
    for i in range(n):
        for j in range(m):
            dp[i][j] = gold[idx]
            idx += 1

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j-1])+dp[i][j]
            elif i == n-1:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j-1])+dp[i][j]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j-1], dp[i-1][j-1])+dp[i][j]

    answer = 0    
    for i in range(n):
        answer = max(answer, dp[i][-1])
