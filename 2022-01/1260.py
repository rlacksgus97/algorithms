#2022-01-07 11:10-11:30
from collections import deque

n, m, v = map(int, input().split())
edges = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    edges[x].append(y)
    edges[y].append(x)

for i in range(n+1):
    edges[i].sort()

visited = [False]*(n+1)

def dfs(x):
    visited[x] = True
    print(x, end=' ')
    for v in edges[x]:
        if visited[v] == False:
            dfs(v)

dfs(v)
visited = [False]*(n+1)

def bfs(x):
    q = deque([x])
    visited[x] = True
    print(x, end=' ')
    while q:
        a = q.popleft()
        for v in edges[a]:
            if visited[v] == False:
                q.append(v)
                visited[v] = True
                print(v, end=' ')

print()
bfs(v)