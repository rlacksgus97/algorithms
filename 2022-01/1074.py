n, r, c= map(int, input().split())
l = 2**n

answer = 0
def z(l, a, b):
    global answer
    if l == 1:
        return 1
    l = l // 2
    if a <= l and b <= l:
        answer += z(l, a, b)
    elif a <= l and b > l:
        answer += l*l + z(l, a, b-l)
    elif a > l and b <= l:
        answer += l*l*2 + z(l, a-l, b)
    elif a > l and b > l:
        answer += l*l*3 + z(l, a-l, b-l)
    return answer

z(l, r+1, c+1)
print(answer-1)