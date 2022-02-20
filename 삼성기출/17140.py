r, c, k = map(int, input().split())
a = []
for _ in range(3):
    a.append(list(map(int, input().split())))

def roperation(a):
    result = []
    for i in range(len(a)):
        num_count = dict()
        for j in range(len(a[0])):
            if a[i][j] != 0:
                if a[i][j] in num_count:
                    num_count[a[i][j]] += 1
                else:
                    num_count[a[i][j]] = 1
        row_result = []
        for k, v in num_count.items():
            row_result.append((v, k))
        row_result.sort()

        row = []
        for rr in row_result:
            row.append(rr[1])
            row.append(rr[0])
        result.append(row)
    return result

def coperation(a):
    result = []
    for j in range(len(a[0])):
        num_count = dict()
        for i in range(len(a)):
            if a[i][j] != 0:
                if a[i][j] in num_count:
                    num_count[a[i][j]] += 1
                else:
                    num_count[a[i][j]] = 1
        col_result = []
        for k, v in num_count.items():
            col_result.append((v, k))
        col_result.sort()

        col = []
        for cr in col_result:
            col.append(cr[1])
            col.append(cr[0])
        result.append(col)
    return result

def resize_row(result):
    max_size = 0
    for i in range(len(result)):
        max_size = max(max_size, len(result[i]))
    
    b = [[0 for _ in range(max_size)] for _ in range(len(result))]
    for i in range(len(result)):
        for j in range(len(result[i])):
            b[i][j] = result[i][j]
    return b

def resize_col(result):
    max_size = 0
    for i in range(len(result)):
        max_size = max(max_size, len(result[i]))

    b = [[0 for _ in range(len(result))] for _ in range(max_size)]
    for i in range(len(result)):
        for j in range(len(result[i])):
            b[j][i] = result[i][j]
    return b

time = 0
while True:
    if len(a) >= r and len(a[0]) >= c and a[r-1][c-1] == k:
        print(time)
        break
    if len(a) >= len(a[0]):
        result = roperation(a)
        a = resize_row(result)
    else:
        result = coperation(a)
        a = resize_col(result)
    time += 1
    if time == 101:
        print(-1)
        break