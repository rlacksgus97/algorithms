#2022-01-07 13:50-
from collections import deque

n, m = map(int, input().split())
edges = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[b].append(a)

def bfs(x):
    q = deque([x])
    visited = [False]*(n+1)
    visited[x] = True
    count = 1
    while q:
        v = q.popleft()
        for e in edges[v]:
            if visited[e] == False:
                visited[e] = True
                q.append(e)
                count += 1
    return count    

result = []
max_c = -1
for i in range(1, n+1):
    c = bfs(i)
    if c > max_c:
        result = [i]
        max_c = c
    elif c == max_c:
        result.append(i)
        max_c = c

for i in result:
    print(i, end=' ')
    