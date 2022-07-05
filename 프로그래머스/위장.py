def solution(clothes):
    answer = 1
    closet = dict()
    for c in clothes:
        if c[1] in closet:
            closet[c[1]] += 1
        else:
            closet[c[1]] = 1
    for k,v in closet.items():
        answer *= v+1
    return answer-1