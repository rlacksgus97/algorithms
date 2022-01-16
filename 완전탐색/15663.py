import sys
n, m = map(int, sys.stdin.readline().split(' '))
nums = list(map(int, sys.stdin.readline().split(' ')))
nums.sort()

used = [0 for _ in range(n)]
selected = [0 for _ in range(m)]
def rec_func(k):
    if k == m:
        for s in selected:
            print(s, end=' ')
        print()
    else:
        last_cand = 0
        for cand in range(n):
            if used[cand] == 1 or nums[cand] == last_cand:
                print(selected, last_cand)
                continue
            last_cand = nums[cand]

            selected[k] = nums[cand]
            used[cand] = 1
            rec_func(k+1)
            selected[k] = 0
            used[cand] = 0

rec_func(0)

#fail