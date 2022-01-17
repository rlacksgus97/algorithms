n = int(input())
k = int(input())

if k>=n:
    print(0)
    exit(0)

sensors = list(map(int, input().split()))
sensors.sort()

distance = []
for i in range(n-1):
    distance.append(abs(sensors[i]-sensors[i+1]))
distance.sort()

for _ in range(k-1):
    distance.pop()

print(sum(distance))

#fail