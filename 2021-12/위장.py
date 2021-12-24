def solution(clothes):
    answer = 1
    table = {}
    for item in clothes:
        if item[1] in table:
            table[item[1]] += 1
        else:
            table[item[1]] = 1
    for i in table.values():
        answer *= (i+1)
    return answer-1