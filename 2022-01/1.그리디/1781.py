import heapq

n = int(input())
cups = []
for _ in range(n):
    cups.append(tuple(map(int, input().split())))
cups.sort()

q = []
for c in cups:
    deadline = c[0]
    heapq.heappush(q, c[1])
    if deadline < len(q):
        heapq.heappop(q)

print(sum(q))

#fail