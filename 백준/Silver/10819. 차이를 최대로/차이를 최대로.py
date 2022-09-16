import sys
sys.setrecursionlimit(10**6)
n = int(input())
a = list(map(int, input().split()))
ans = []
a.sort()
def pmt(n, a):
    sum = 0
    for x in range(n-1):
        sum += abs(a[x]-a[x+1])
    ans.append(sum)
    i = n-1
    while i>0 and a[i-1]>=a[i]:
        i -= 1
    if i <= 0:
        return
    j = n-1
    while a[j] <= a[i-1]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]
    j = n-1
    while (i < j):
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    pmt(n,a)

pmt(n,a)
print(max(ans))
