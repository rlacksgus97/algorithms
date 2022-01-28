#Topological Sort
import sys
import heapq

n, m = map(int, sys.stdin.readline().split())

edge = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    edge[a].append(b)
    indegree[b] += 1

q = []
for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(q, i)

result = []
while q:
    x = heapq.heappop(q)
    result.append(x)
    for y in edge[x]:
        indegree[y] -= 1
        if indegree[y] == 0:
            heapq.heappush(q, y)

for x in result:
    print(x, end=' ')