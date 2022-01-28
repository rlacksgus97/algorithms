import heapq

n = int(input())
card =[]
for i in range(n):
    c = int(input())
    heapq.heappush(card, c)

count = 0
while len(card) > 1:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    count += a+b
    heapq.heappush(card, a+b)
print(count)