n, m = map(int, input().split())
d = list(map(int, input().split()))

start = 0
end = max(d)

answer = 0
while start <= end:
    mid = (start+end)//2
    sum = 0
    for t in d:
        if mid < t:
            sum += t-mid
    if sum < m:
        end = mid-1
    else:
        answer = mid
        start = mid+1

print(answer)
