n = int(input())
book = []
for _ in range(n):
    age, name = input().split()
    book.append((int(age), name))

book.sort(key=lambda x: x[0])

for b in book:
    print(b[0], b[1])