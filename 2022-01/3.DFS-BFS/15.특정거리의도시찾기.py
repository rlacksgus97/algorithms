from collections import deque

n, m, k, x = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    g[s].append(e)

check = [-1]*(n+1)

def bfs(start):
    queue = deque([])
    queue.append(start)
    check[start] = 0

    while queue:
        i = queue.popleft()
        for j in g[i]:
            if check[j] == -1:
                queue.append(j)
                check[j] = check[i] + 1

bfs(x)
find = False
for i in range(n+1):
    if check[i] == k:
        print(i)
        find = True
if find == False:
    print(-1)