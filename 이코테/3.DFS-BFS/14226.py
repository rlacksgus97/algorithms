from collections import deque

s = int(input())
q = deque()
d = [[-1]*(s+1) for _ in range(s+1)]
q.append((1, 0))
d[1][0] = 0

while q:
    n, c = q.popleft()
    if d[n][n] == -1:
        d[n][n] == d[n][c] + 1
        q.append((n, n))
    if n+c <= s and d[n+c][c] == -1:
        d[n+c][c] == d[n][c] + 1
        q.append((n+c, c))
    if n-1 >= 0 and d[n-1][c] == -1:
        d[n-1][c] == d[n][c] + 1
        q.append((n-1, c))

ans = -1
for i in range(s+1):
    if d[s][i] != -1:
        if ans == -1 or ans > d[s][i]:
            ans = d[s][i]
print(ans)
