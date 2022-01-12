import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split(' ')))
op = list(map(int, sys.stdin.readline().split(' ')))

min_v = 1e9
max_v = -1e9

def calculate(operand1, operator, operand2):
    if operator == 0:
        return operand1 + operand2
    if operator == 1:
        return operand1 - operand2
    if operator == 2:
        return operand1 * operand2
    if operator == 3:
        if operand1 < 0:
            return - ((-operand1) // operand2)
        else:
            return operand1 // operand2

def rec_func(k, value):
    global min_v
    global max_v
    if k == n-1:
        min_v = min(min_v, value)
        max_v = max(max_v, value)
    else:
        global op
        for cand in range(4):
            if op[cand] > 0:
                op[cand] -= 1
                value = calculate(value, cand, a[k+1])
                rec_func(k+1, value)
                op[cand] += 1

rec_func(0, a[0])
print(min_v)
print(max_v)

#fail