def solution(s):
    answer = len(s)
    for l in range(1, len(s)//2+1):
        count = 1
        compressed = ""
        prev = s[0:l]
        for i in range(l, len(s), l):
            if prev == s[i:i+l]:
                count += 1
            else:
                if count > 1:
                    compressed += str(count) + prev
                else:
                    compressed += prev
                count = 1
                prev = s[i:i+l]
        if count > 1:
            compressed += str(count) + prev
        else:
            compressed += prev
        answer = min(answer, len(compressed))
    return answer