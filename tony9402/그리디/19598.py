import sys
import heapq
input = sys.stdin.readline

N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]
times.sort()

q = []
for t in times:
    if q == []:
        heapq.heappush(q, t[1])
    else:
        if q[0] > t[0]:
            heapq.heappush(q, t[1])
        else:
            heapq.heappop(q)
            heapq.heappush(q, t[1])
print(len(q))