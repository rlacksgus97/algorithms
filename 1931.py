n = int(input())
time = []
for _ in range(n):
    time.append(list(map(int, input().split())))

time.sort(key=lambda x:(x[1], x[0]))
count = 0
now = 0
for t in time:
    if now <= t[0]:
        count += 1
        now = t[1]

print(count)