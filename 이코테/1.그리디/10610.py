n = list(map(int, input()))

if sum(n)%3 != 0:
    print(-1)
else:
    if 0 not in n:
        print(-1)
    else:
        n.sort(reverse=True)
        for x in n:
            print(str(x), end='')
