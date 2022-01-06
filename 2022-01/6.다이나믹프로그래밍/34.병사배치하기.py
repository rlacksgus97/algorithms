n = int(input())
soldiers = list(map(int, input().split()))

dp = [[0, 0]*n]
dp[0][0] = soldiers[0]
dp[0][1] = -1
for i in range(1, n):
    if soldiers[i-1] > soldiers[i]:
        dp[i][0] = dp[i-1] + soldiers[i]
        dp[i][1] = i-1
    else:
        idx = i-1
        while idx != -1:
            if soldiers[idx] > soldiers[i]:
                dp[i][0] = dp[idx] + soldiers[i]
                dp[i][1] = idx
                break
            idx = dp[idx][1]
        dp[i] = soldiers[i]