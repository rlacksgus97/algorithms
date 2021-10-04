n, x = map(int, input().split())
d = list(map(int, input().split()))

def first(start, end, x):
    while start<=end:
        mid = (start+end)//2
        if d[mid] == x:
            if d[mid-1] < x or mid == 0:
                return mid
            else:
                end = mid-1
        elif d[mid] > x:
            end = mid-1
        else:
            start = mid+1
    return None

def last(start, end, x):
    while start<=end:
        mid = (start+end)//2
        if d[mid] == x:
            if d[mid+1] > x or mid == n-1:
                return mid
            else:
                start = mid+1
        elif d[mid] > x:
            end = mid-1
        else:
            start = mid+1

start = first(0, n-1, x)
if start is None:
    print(-1)
else:
    end = last(0, n-1, x)
    print(end-start+1)
