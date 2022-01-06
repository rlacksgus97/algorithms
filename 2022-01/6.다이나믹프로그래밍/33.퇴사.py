n = int(input())
tp = []
for _ in range(n):
    tp.append(list(map(int, input().split())))

dp = [0]*(n+1)

