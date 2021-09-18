import sys

n = int(sys.stdin.readline())
d = []
count = 0
for _ in range(n):
    temp = sys.stdin.readline().split()
    temp.append(count)
    count += 1
    d.append(temp)
d.sort(key=lambda x:(int(x[0]), int(x[2])))

for p in d:
    print(p[0], p[1])