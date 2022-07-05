n, m = map(int, input().split())
companies = [[1e9 for _ in range(n+1)] for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            companies[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    companies[a][b] = 1
    companies[b][a] = 1

x, k = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            companies[a][b] = min(companies[a][b], companies[a][k]+companies[k][b])

answer = companies[1][k] + companies[k][x]
if answer >= 1e9:
    print(-1)
else:
    print(answer)