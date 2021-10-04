n = int(input())
have = list(map(int, input().split()))
m = int(input())
request = list(map(int, input().split()))

have.sort()
request.sort()

def binary_search(start, end, have, request):
    while start <= end:
        mid = (start+end)//2
        if have[mid] == request:
            return True
        elif have[mid] > request:
            end = mid-1
        else:
            start = mid+1
    return False

for i in range(len(request)):
    if binary_search(0, len(have)-1, have, request[i]):
        print("yes", end=' ')
    else:
        print("no", end=' ')
