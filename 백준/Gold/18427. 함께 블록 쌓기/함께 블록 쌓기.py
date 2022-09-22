N, M, H = map(int, input().split())
students = [[]]
for _ in range(N):
    students.append([0] + list(map(int, input().split())))

dp = [[0 for _ in range(H+1)] for _ in range(N+1)]
for i in range(N+1):
    dp[i][0] = 1

for i in range(1, N+1):
    for j in range(1, H+1):
        for k in students[i]:
            if j-k >= 0:
                dp[i][j] += dp[i-1][j-k]

print(dp[-1][-1] % 10007)
