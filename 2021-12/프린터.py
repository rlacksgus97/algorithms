def solution(priorities, location):
    answer = 0
    priorities = [(p, i) for i, p in enumerate(priorities)]
    
    while priorities:
        if priorities[0][0] == max(priorities, key=lambda x: x[0])[0]:
            answer += 1
            if priorities[0][1] == location:
                return answer
            else:
                priorities.pop(0)
        else:
            priorities.append(priorities.pop(0))