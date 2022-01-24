import sys

n, c = map(int, sys.stdin.readline().split())
house = []
for _ in range(n):
    house.append(int(sys.stdin.readline()))
house.sort()

answer = 0
start = 1
end = house[-1] - house[0]
while start <= end:
    mid = (start + end) // 2
    count = 1
    tmp = house[0]
    for h in house:
        if h >= tmp + mid:
            tmp = h
            count += 1
    if count < c:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)