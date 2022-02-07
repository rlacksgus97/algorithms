def solution(msg):
    answer = []
    lzw = dict()
    for i in range(26):
        lzw[chr(ord('A')+i)] = i+1
        
    ptr = 0
    next_ptr = 0
    index = 27
    while ptr<len(msg):
        goal = ''
        for l in range(1, len(msg)-ptr+1):
            target = msg[ptr:ptr+l]
            if target in lzw:
                goal = lzw[target]
                next_ptr = ptr+l
            else:
                answer.append(goal)#색인 번호 출력
                lzw[target] = index#다음 글자 포함 등록
                index += 1#색인 번호 증가
                break
        ptr = next_ptr
    
    if goal != '':
        answer.append(goal)
    return answer