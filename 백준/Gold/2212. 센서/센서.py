n = int(input())
k = int(input())
sensors = list(map(int, input().split()))
sensors.sort()

if n <= k:
    print(0)
    exit(0)

distance = []
for i in range(n-1):
    distance.append(sensors[i+1]-sensors[i])
distance.sort(reverse=True)

answer = sum(distance)
for i in range(k-1):
    answer -= distance[i]

print(answer)