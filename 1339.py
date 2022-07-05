n = int(input())
words = []
for _ in range(n):
    words.append(input())

count = [[]*10]
for w in words:
    for i in range(len(w)):
        count[n-1-i].append(w[i])

print()
