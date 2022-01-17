n = int(input())
coord = []
for _ in range(n):
    x, y = map(int, input().split())
    coord.append((x, y))

coord.sort()

for c in coord:
    print(c[0], c[1])