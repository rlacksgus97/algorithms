n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
ans = 0

while True:
    for _ in range(k):
        if m == 0:
            break
        ans += data[-1]
        m -= 1
    if m == 0:
        break
    ans += data[-2]
    m -= 1

print(ans)
