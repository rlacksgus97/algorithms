def press(a, index):
    if index == 0:
        a[index] = 1- a[index]
        a[index+1] = 1- a[index+1]
    elif index == n-1:
        a[index-1] = 1- a[index-1]
        a[index] = 1- a[index]
    else:
        a[index-1] = 1- a[index-1]
        a[index] = 1- a[index]
        a[index+1] = 1- a[index+1]

def check(a, b):
    cnt = 0
    for i in range(0, n-1):
        if a[i] != b[i]:
            press(a, i+1)
            cnt += 1
    if a != b:
        cnt = -1
        return (False, -1)
    else:
        return (True, cnt)
        
n = int(input())
a1 = list(map(int, input()))
a2 = a1.copy()
b = list(map(int, input()))
press(a1, 0)

(x1, y1) = check(a1, b)
if x1:
    y1 = y1 + 1
(x2, y2) = check(a2, b)

if x1 and x2:
    print(min(y1, y2))
elif x1:
    print(y1)
elif x2:
    print(y2)
else:
    print(-1)
