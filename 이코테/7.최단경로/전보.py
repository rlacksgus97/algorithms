import heapq

n, m, c = map(int, input().split())
cities = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    cities[x].append([y,z])

time = [1e9 for _ in range(n+1)]

def dijkstra(start):
    q= []
    heapq.heappush(q, (0, start))
    time[start] = 0
    while q:
        t, now = heapq.heappop(q)
        if time[now] < t:
            continue
        for i in cities[now]:
            cost = t + i[1]
            if cost < time[i[0]]:
                time[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

cnt = 0
total = 0
for i in range(n):
    if time[i] != 1e9:
        cnt += 1
        total = max(total, time[i])
print(cnt, total)