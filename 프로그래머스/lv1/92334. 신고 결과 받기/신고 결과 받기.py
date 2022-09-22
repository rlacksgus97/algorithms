from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    mailCount = defaultdict(int)
    reportList = defaultdict(set)
    reportCount = defaultdict(int)
    
    for r in report:
        a, b = r.split()
        if b not in reportList[a]:
            reportList[a].add(b)
            reportCount[b] += 1
    
    for key,value in reportList.items():
        count = 0
        for user in value:
            if reportCount[user] >= k:
                count += 1
        mailCount[key] = count
        
    for id in id_list:
        answer.append(mailCount[id])
    
    return answer