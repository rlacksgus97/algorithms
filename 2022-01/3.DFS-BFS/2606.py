#2022-01-07 13:20-13:30
from collections import deque

n = int(input())
m = int(input())
edges = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    edges[x].append(y)
    edges[y].append(x)
visited = [False]*(n+1)

count = 0
q = deque([1])
visited[1] = True
while q:
    v = q.popleft()
    count += 1
    for a in edges[v]:
        if visited[a] == False:
            visited[a] = True
            q.append(a)

print(count-1)