#fail

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

pick = [0 for _ in range(n)]
shipped = [False for _ in range(m)]

cranes.sort(reverse=True)
boxes.sort(reverse=True)

if cranes[0] < boxes[0]:
    print(-1)
    exit(0)

time = 0
count = 0
while True:
    if count == m:
        break
    for i in range(n):
        while pick[i] < m:
            if not shipped[pick[i]] and cranes[i] >= boxes[pick[i]]:
                shipped[pick[i]] = True
                count += 1
                break
            pick[i] += 1
    time += 1
print(time)