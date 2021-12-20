n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
ans = 0

for x in range(n-2):
    for y in range(x+1, n-1):
        for z in range(y+1, n):
            sum_v = a[x]+a[y]+a[z]
            if sum_v <= m:
                ans = max(ans, sum_v)

print(ans)
