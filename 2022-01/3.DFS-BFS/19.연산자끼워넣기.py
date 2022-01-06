n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))

max_result = -1000000000
min_result = 1000000000
def dfs(result, idx):
    global max_result
    global min_result
    if idx == n:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return

    for i in range(4):
        if op[i] > 0:
            op[i] -= 1
            if i == 0:
                dfs(result+num[idx], idx+1)
            elif i == 1:
                dfs(result-num[idx], idx+1)
            elif i == 2:
                dfs(result*num[idx], idx+1)
            else:
                dfs(int(result/num[idx]), idx+1)
            op[i] += 1

dfs(num[0], 1)
print(max_result)
print(min_result)