import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

count = [0 for _ in range(20001)]
for i in range(N):
    count[10000+A[i]] += 1

A.sort()
N = len(A)
answer = 0
for i in range(N-2):
    x = -A[i]
    l, r = i+1, N-1
    while l < r:
        num = A[l]+A[r]
        if num == x:
            if A[l] == A[r]:
                answer += r-l
            else:
                answer += count[10000+A[r]]
            l += 1
        elif num < x:
            l += 1
        else:
            r -= 1
print(answer)
