from collections import defaultdict
from math import ceil

def toMinutes(time):
    t = time.split(':')
    return int(t[0])*60 + int(t[1])

def solution(fees, records):
    answer = []
    cars = defaultdict(list)
    result = defaultdict(int)
    for record in records:
        rec = record.split()
        cars[rec[1]].append(toMinutes(rec[0]))
    
    for k, v in cars.items():
        if len(v) % 2 == 1:
            v.append(toMinutes('23:59'))
            
    for k, v in cars.items():
        time = 0
        for i in range(0, len(v), 2):
            time += v[i+1] - v[i]
        f = fees[1]
        if time > fees[0]:
            f += ceil((time-fees[0])/fees[2])*fees[3]
        result[k] = f
    
    charge = []
    for k,v in result.items():
        charge.append([k,v])
    charge.sort()
    
    for c in charge:
        answer.append(c[1])
    return answer