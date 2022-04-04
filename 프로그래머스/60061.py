def check(answer):
    for x,y,a in answer:
        #기둥
        if a == 0:
            if y == 0 or ((x,y-1,0) in answer) or ((x,y,1) in answer or (x-1,y,1) in answer):
                continue
            return False
        #보
        else:
            if ((x,y-1,0) in answer or (x+1, y-1,0) in answer) or ((x-1,y,1) in answer and (x+1,y,1) in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for o in build_frame:
        x, y, a, b = o
        #설치
        if b == 1:
            answer.append((x,y,a))
            if not check(answer):
                answer.remove((x,y,a))
        #삭제
        else:
            answer.remove((x,y,a))
            if not check(answer):
                answer.append((x,y,a))
    answer.sort()
    return answer
