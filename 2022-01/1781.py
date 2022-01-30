import heapq

n = int(input())
questions = []
for _ in range(n):
    questions.append(tuple(map(int, input().split())))
questions.sort()
solve = []
for q in questions:
    deadline, ramen = q[0], q[1]
    heapq.heappush(solve, ramen)
    if len(solve) > deadline:
        heapq.heappop(solve)
print(sum(solve))
