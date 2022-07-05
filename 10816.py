n = int(input())
cards = list(map(int, input().split()))
m = int(input())
guesses = list(map(int, input().split()))

cards.sort()

def first(target):
    start = 0
    end = n-1
    while start<=end:
        mid = (start+end)//2
        if cards[mid] == target:
            if  mid == 0 or cards[mid-1] < target:
                return mid
            else:
                end = mid-1
        elif cards[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return -1

def last(target):
    start = 0
    end = n-1
    while start<=end:
        mid = (start+end)//2
        if cards[mid] == target:
            if mid == n-1 or cards[mid+1] > target:
                return mid
            else:
                start = mid+1
        elif cards[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return -1

answer = []
for g in guesses:
    head = first(g)
    if head == -1:
        answer.append(0)
    else:
        tail = last(g)
        answer.append(tail-head+1)

for a in answer:
    print(a, end=' ')