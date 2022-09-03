N, S = map(int, input().split())
numbers = list(map(int, input().split()))

prefixSum = [0 for _ in range(N+1)]
for i in range(1, N+1):
    prefixSum[i] += prefixSum[i-1] + numbers[i-1]

length = N+1
l, r = 1, 1
while True:
    if prefixSum[r]-prefixSum[l-1] >= S:
        length = min(length, r-l+1)
        l += 1
    else:
        r += 1
        if r > N:
            r -= 1
            break
while l <= r:
    l += 1
    if prefixSum[r]-prefixSum[l-1] >= S:
        length = min(length, r-l+1)

if length == N+1:
    print(0)
else:
    print(length)