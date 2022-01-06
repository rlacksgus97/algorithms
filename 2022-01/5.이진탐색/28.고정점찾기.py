n = int(input())
d = list(map(int, input().split()))

start = 0
end = n-1

ans = -1
while start <= end:
    mid = (start+end)//2
    if d[mid] == mid:
        ans = mid
        break
    elif d[mid] > mid:
        end = mid-1
    else:
        start = mid+1

print(ans)