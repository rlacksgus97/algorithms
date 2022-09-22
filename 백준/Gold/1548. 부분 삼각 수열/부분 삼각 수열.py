# 13:50 -
N = int(input())
A = list(map(int, input().split()))
A.sort()


def dfs(a, i):
    global answer
    answer = max(answer, len(a))
    if i >= N:
        return
    if a[0]+a[1] > A[i]:
        dfs(a+[A[i]], i+1)


if N < 3:
    print(len(A))
else:
    answer = 0
    for i in range(N-1):
        dfs([A[i], A[i+1]], i+2)
    print(answer)
