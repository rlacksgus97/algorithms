n, m, k = map(int, input().split())

cnt = 0
if n > m*2:
    cnt = m
    n -= m*2
    m -= cnt
else:
    cnt = n//2
    n -= cnt*2
    m -= cnt

if k > n+m:
    k = k-n-m
    cnt -= k//3
    if k%3 != 0:
        cnt -= 1

print(cnt)