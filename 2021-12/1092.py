n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

if cranes[0] < boxes[0]:
    print(-1)
    exit(0)

pointer = [0]*n
check = [False]*m

time = 0
count = 0

while True:
    if count == m:
        break
    for i in range(n):
        while pointer[i] < m:
            if not check[pointer[i]] and cranes[i] >= boxes[pointer[i]]:
                check[pointer[i]] = True
                pointer[i] += 1
                count += 1
                break
            pointer[i] += 1
    time += 1

print(time)

#fail