#Disjoint Sets, Union-Find
#fail

def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x, y):
    a = find(x)
    b = find(y)

    if a != b:
        parent[b] = a
        number[a] += number[b]

t = int(input())
for _ in range(t):
    f = int(input())
    parent = dict()
    number = dict()

    for _ in range(f):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1
        
        union(a, b)
        print(number[find(a)])