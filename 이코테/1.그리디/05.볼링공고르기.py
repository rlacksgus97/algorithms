n, m = map(int, input().split())
d = list(map(int, input().split()))

num = [0] * 11
count = 0

for x in d:
    num[x] += 1

for i in range(1, m+1):
    n -= num[i]
    count += num[i] * n

print(count)
