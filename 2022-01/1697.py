#2022-01-07 11:35-11:50
from collections import deque

n, k = map(int, input().split())
visited = [False]*(100001)

q = deque([(n, 0)])
while q:
    x, t = q.popleft()
    if x == k:
        print(t)
        break
    visited[x] = True
    if x+1 <= 100000 and visited[x+1] == False:
        q.append((x+1, t+1))
    if x-1 >= 0 and visited[x-1] == False:
        q.append((x-1, t+1))
    if x*2 <= 100000 and visited[x*2] == False:
        q.append((x*2, t+1))
