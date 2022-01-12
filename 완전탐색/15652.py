import sys
n, m = map(int, sys.stdin.readline().split(' '))

selected= [0 for _ in range(m)]

def rec_func(k):
    if k == m:
        for x in selected:
            sys.stdout.write(str(x)+' ')
        sys.stdout.write('\n')
        return
    else:
        if k == 0:
            start = 1
        else:
            start = selected[k-1]
        for cand in range(start, n+1):
            selected[k] = cand
            rec_func(k+1)
            selected[k] = 0

rec_func(0)