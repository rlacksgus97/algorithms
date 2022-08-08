import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    minQ = []
    maxQ = []
    check = [False for _ in range(k)]
    for i in range(k):
        op, num = input().split()
        num = int(num)
        if op == 'I':
            heapq.heappush(minQ, [num,i])
            heapq.heappush(maxQ, [-num,i])
        else:
            if num == 1:
                while maxQ and check[maxQ[0][1]]:
                    heapq.heappop(maxQ)
                if maxQ:
                    n, index = heapq.heappop(maxQ)
                    check[index] = True
            else:
                while minQ and check[minQ[0][1]]:
                    heapq.heappop(minQ)
                if minQ:
                    n, index = heapq.heappop(minQ)
                    check[index] = True

    while maxQ and check[maxQ[0][1]]:
        heapq.heappop(maxQ)

    while minQ and check[minQ[0][1]]:
        heapq.heappop(minQ)

    if minQ == []:
        print('EMPTY')
    else:
        print(-maxQ[0][0], minQ[0][0])