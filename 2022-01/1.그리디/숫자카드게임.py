n, m = map(int, input().split())

ans = 0

for _ in range(n):
    data = list(map(int, input().split()))
    row_min = min(data)
    ans = max(ans, row_min)

print(ans)
