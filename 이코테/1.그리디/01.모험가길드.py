n = int(input())
d = list(map(int, input().split()))

d.sort()
group = 0
member = 0

for x in d:
    member += 1
    if x <= member:
        group += 1
        member = 0

print(group)