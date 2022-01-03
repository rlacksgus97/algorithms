n, m = map(int, input().split())
dp = [10001]*10001
coin = []
for _ in range(n):
    coin.append(int(input()))

dp[0] = 0
for c in coin:
    for i in range(c, m+1):
        if dp[i-c] != 10001:
            dp[i] = min(dp[i], dp[i-c]+1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])