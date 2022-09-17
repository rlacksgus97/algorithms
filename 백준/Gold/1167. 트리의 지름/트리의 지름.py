# 10:00 - 10:50
# 트리의 지름
# 한 노드에서 가장 멀리 떨어진 노드를 찾고
# 그 노드에서 가장 멀리 떨어진 노드를 다시 찾으면 그것이 트리의 지름
import sys
from collections import deque
input = sys.stdin.readline

V = int(input())
edges = [[] for _ in range(V+1)]
for _ in range(V):
    info = list(map(int, input().split()))[:-1]
    for i in range(1, len(info), 2):
        edges[info[0]].append([info[i], info[i+1]])


def bfs(start):
    max_dist = 0
    max_node = 0
    q = deque([[start, 0]])
    visited = [False for _ in range(V+1)]
    visited[start] = True
    while q:
        x, dist = q.popleft()
        for y, cost in edges[x]:
            if not visited[y]:
                new_dist = dist + cost
                if new_dist > max_dist:
                    max_dist = new_dist
                    max_node = y
                q.append([y, new_dist])
                visited[y] = True
    return [max_dist, max_node]


max_node = bfs(1)[1]
print(bfs(max_node)[0])
