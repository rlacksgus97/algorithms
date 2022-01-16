import sys
n, s = map(int, sys.stdin.readline().split(' '))
nums = list(map(int, sys.stdin.readline().split(' ')))

answer = 0
def rec_func(k, value):
    global answer
    if k == n:
        if value == s:
            answer += 1
    else:
        rec_func(k+1, value+nums[k])
        rec_func(k+1, value)

rec_func(0, 0)
if s == 0:
    answer -= 1
print(answer)