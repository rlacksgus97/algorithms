def solution(str1, str2):
    answer = 0
    a1 = {}
    a2 = {}
    frag_count1 = 0
    frag_count2 = 0
    for i in range(len(str1)):
        frag = str1[i:i+2].lower()
        if len(frag) == 2 and frag.isalpha():
            frag_count1 += 1
            if frag in a1:
                a1[frag] += 1
            else:
                a1[frag] = 1
    for i in range(len(str2)):
        frag = str2[i:i+2].lower()
        if len(frag) == 2 and frag.isalpha():
            frag_count2 += 1
            if frag in a2:
                a2[frag] += 1
            else:
                a2[frag] = 1
    
    kyo = 0
    hap = 0
    if len(a1) > len(a2):
        for a in a2:
            if a in a1:
                kyo += min(a1[a], a2[a])
            else:
                hap += a2[a]
    else:
        for a in a1:
            if a in a2:
                kyo += min(a1[a], a2[a])
            else:
                hap += a1[a]
        
    hap = kyo+(frag_count1-kyo)+(frag_count2-kyo)
    
    if len(a1) == 0 and len(a2) == 0:
        answer = 65536
    else:
        answer = int((kyo/hap)*65536)
    
    return answer