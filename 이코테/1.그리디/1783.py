n, m = map(int, input().split())

x = 1
y = 1

if n == 1:
    print(1)
elif n == 2:
    print(min(4, (m+1)//2))
else:
    if m > 6:
        print(m-2)
    else:
        print(min(4, m))