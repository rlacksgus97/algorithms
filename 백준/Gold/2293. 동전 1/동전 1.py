import sys
sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
coin.sort()

dp = [0 for _ in range(k+1)]
dp[0] = 1

for c in coin:
    for i in range(c, k+1):
        dp[i] += dp[i-c]
print(dp[k])
