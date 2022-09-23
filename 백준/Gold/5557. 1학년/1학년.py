N = int(input())
num = list(map(int, input().split()))

dp = [[0 for _ in range(21)] for _ in range(N)]
dp[0][num[0]] = 1
for i in range(N-2):
    for j in range(21):
        if 0 <= j+num[i+1] <= 20:
            dp[i+1][j+num[i+1]] += dp[i][j]
        if 0 <= j-num[i+1] <= 20:
            dp[i+1][j-num[i+1]] += dp[i][j]
print(dp[N-2][num[-1]])
