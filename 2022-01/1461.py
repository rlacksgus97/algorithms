n, m = map(int, input().split())
books = list(map(int, input().split()))
books.sort()

minus = []
plus = []
for b in books:
    if b < 0:
        minus.append(-b)
    else:
        plus.append(b)
minus.sort()

walks = []

for i in range(len(minus)-1, -1, -m):
    walks.append(minus[i])
for i in range(len(plus)-1, -1, -m):
    walks.append(plus[i])

print(sum(walks)*2-max(max(books), -min(books)))