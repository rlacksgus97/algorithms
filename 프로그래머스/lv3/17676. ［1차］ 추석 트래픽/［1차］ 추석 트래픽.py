def get_time(end):
    e = end.split(':')
    hour = int(e[0])*3600
    minute = int(e[1])*60
    second = int(e[2].split('.')[0])
    millisecond = int(e[2].split('.')[1])
    return (hour+minute+second)*1000+millisecond

def solution(lines):
    answer = 0
    start_time = []
    end_time = []
    for line in lines:
        l = line.split()
        end = get_time(l[1])
        start = end-int(float(l[2][:-1])*1000)+1
        start_time.append(start)
        end_time.append(end)
    for i in range(len(lines)):
        count = 0
        current_time = end_time[i]
        for j in range(i, len(lines)):
            if current_time > start_time[j]-1000:
                count += 1
        answer = max(answer, count)
    return answer