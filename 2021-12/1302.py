n = int(input())
counter = dict()
for _ in range(n):
    book = input()
    if book in counter:
        counter[book] += 1
    else:
        counter[book] = 1

# max_count = max(counter.values())
max_count = 0
max_name = []
for i, v in enumerate(counter):
    if counter[v] > max_count:
        max_count = counter[v]

for i, v in enumerate(counter):
    if counter[v] == max_count:
        max_name.append(v)

max_name.sort()
print(max_name[0])