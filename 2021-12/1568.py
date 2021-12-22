n = int(input())
k = 1
t = 0

while n>0:
    if k>n:
        k = 1
    else:
        n -= k
        k += 1
        t += 1

print(t)