n = int(input())
trophies = []
for _ in range(n):
    trophies.append(int(input()))

tallest = 0
count = 0
for i in range(n):
    if tallest < trophies[i]:
        count += 1
        tallest = trophies[i]
print(count)

tallest = 0
count = 0
for i in range(n-1, -1, -1):
    if tallest < trophies[i]:
        count += 1
        tallest = trophies[i]
print(count)