import sys

n, c = map(int, input().split())
d = []
for _ in range(n):
    d.append(int(sys.stdin.readline().rstrip()))
d.sort()

start = 1
end = d[-1]-d[0]
ans = 0

while start <= end:
    gap = (start+end)//2
    count = 1
    temp = d[0]
    for x in d:
        if x >= temp + gap:
            temp = x
            count += 1
    if count >= c:
        ans = gap
        start = gap+1
    else:
        end = gap-1

print(ans)