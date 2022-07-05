def solution(s):
    answer = []
    time = 0
    cnt = 0
    while True:
        if s == "1":
            break
        time += 1
        ns = ""
        for c in s:
            if c == '1':
                ns += c
            else:
                cnt += 1
        l = len(ns)
        s = bin(l)[2:]
    answer.append(time)
    answer.append(cnt)
    return answer
