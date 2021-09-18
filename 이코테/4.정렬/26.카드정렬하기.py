import heapq

n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))

ans = 0

while len(heap) > 1:
    x1 = heapq.heappop(heap)
    x2 = heapq.heappop(heap)
    ans += x1+x2
    heapq.heappush(heap, x1+x2)

print(ans)
