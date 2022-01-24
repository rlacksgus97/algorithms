import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
city = [[] for _ in range(n+1)]
bridge = []
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    city[a].append((b, c))
    city[b].append((a, c))
    bridge.append(c)
plantA, plantB = map(int, sys.stdin.readline().split())

def bfs(start):
    q = deque([start])
    visited = [0 for _ in range(n+1)]
    visited[start] = 1
    while q:
        x = q.popleft()
        for c in city[x]:
            if c[1] >= mid and visited[c[0]] == 0:
                q.append(c[0])
                visited[c[0]] = 1
                if c[0] == plantB:
                    return True
    return False

answer = 0
start = min(bridge)
end = max(bridge)
while start <= end:
    mid = (start + end) // 2
    if bfs(plantA):
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)