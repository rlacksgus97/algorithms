import sys

n = int(sys.stdin.readline())
d = []
for _ in range(n):
    d.append(sys.stdin.readline().split())
d.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for s in d:
    print(s[0])