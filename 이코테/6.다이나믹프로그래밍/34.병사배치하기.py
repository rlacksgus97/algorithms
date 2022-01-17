n = int(input())
s = list(map(int, input().split()))
s.reverse()

dp = [1]*n
for i in range(1, n):
    for j in range(0, i):
        if s[j] < s[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))

#fail