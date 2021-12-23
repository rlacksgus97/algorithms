n = int(input())
rank = []
for _ in range(n):
    rank.append(int(input()))
rank.sort()

answer = 0
for i in range(1, n+1):
    answer += abs(rank[i-1]-i)
print(answer)