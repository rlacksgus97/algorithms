n = int(input())
d = list(map(int, input().split()))
d.sort()

print(d[(n-1)//2])
