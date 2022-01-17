t = int(input())

for _ in range(t):
    n = int(input())
    exp = [0 for _ in range(n-1)]
    op = [' ', '+', '-']
    def rec_func(x):
        if x == n-1:
            result = '1'
            for i in range(n-1):
                if exp[i] != ' ':
                    result += exp[i]
                result += str(i+2)
            value = eval(result)
            if value == 0:
                result = '1'
                for i in range(n-1):
                    result += exp[i]
                    result += str(i+2)
                print(result)
        else:
            for i in range(3):
                exp[x] = op[i]
                rec_func(x+1)
                exp[x] = 0

    rec_func(0)
    print()
