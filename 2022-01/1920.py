n = int(input())
a = set(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

for num in find:
    if num in a:
        print(1)
    else:
        print(0)