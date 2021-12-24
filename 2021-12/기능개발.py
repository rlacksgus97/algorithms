def solution(progresses, speeds):
    answer = []
    
    while progresses:
        for i in range(len(progresses)):
            if progresses[i] < 100:
                if progresses[i] + speeds[i] > 100:
                    progresses[i] = 100
                else:
                    progresses[i] += speeds[i]
        count = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        if count != 0:
            answer.append(count)
    
    return answer