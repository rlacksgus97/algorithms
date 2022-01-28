import heapq

n = int(input())
array = []
result = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if len(array) == 0:
            result.append(0)
        else:
            y = heapq.heappop(array)
            result.append(y)
    else:
        heapq.heappush(array, x)

for x in result:
    print(x)