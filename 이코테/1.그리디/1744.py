n = int(input())
d= []
for _ in range(n):
    d.append(int(input()))

ans = 0
d.sort()

while d:
    x = d.pop()
    if x > 0:
        if d:
            y = d.pop()
            if y > 0:
                ans += x*y
            else:
                d.append(y)
                d.append(x)
                break
        else:
            d.append(x)
            break
    else:
        d.append(x)
        break

d.sort(reverse=True)

while d:
    x = d.pop()
    if x < 0:
        if d:
            y = d.pop()
            if y < 0:
                ans += x*y
            else:
                d.append(y)
                d.append(x)
                break
        else:
            d.append(x)
            break
    else:
        d.append(x)
        break

while d:
    ans += d.pop()

print(ans)