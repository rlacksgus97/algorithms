exp = input().split('-')
parts = []

for e in exp:
    part = 0
    x = list(map(int, e.split('+')))
    part += sum(x)
    parts.append(part)

ans = parts[0]
for i in range(1, len(parts)):
    ans -= parts[i]

print(ans)
