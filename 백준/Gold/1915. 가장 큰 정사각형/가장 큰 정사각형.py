n, m = map(int, input().split())
dp = [list(map(int, list(input()))) for _ in range(n)]

answer = 0
for i in range(n):
    if dp[i][0] == 1:
        answer = 1
        break

for i in range(m):
    if dp[0][i] == 1:
        answer = 1
        break

for i in range(1, n):
    for j in range(1, m):
        if dp[i][j] > 0 and dp[i-1][j-1] > 0 and dp[i-1][j] > 0 and dp[i][j-1] > 0:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
            answer = max(answer, dp[i][j])
print(answer**2)
