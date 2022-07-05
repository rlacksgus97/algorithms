#2022-01-09 13:00-

n, k = map(int, input().split())
coin = []
dp = [0]*(k+1)
for _ in range(n):
    c = int(input())
    coin.append(c)
    dp[c] = 1

for i in range(1, k+1):
    for c in coin:
        if i-c > 0:
            if i-c > c:
                dp[i] += dp[i-c] * dp[c]
            elif i-c < c:
                continue
            else:
                dp[i] += 1

print(dp)
