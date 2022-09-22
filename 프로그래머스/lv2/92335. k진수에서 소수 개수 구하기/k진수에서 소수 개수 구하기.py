def nToK(n, k):
    result = ''
    while n > 0:
        result = str(n%k) + result
        n = n // k
    return result

def isPrime(x):
    for i in range(2, int(x**(0.5))+1):
        if x % i == 0 :
            return False
    return True

def solution(n, k):
    answer = 0
    result = nToK(n,k)
    candidates = result.split('0')
    # print(result)
    # print(candidates)
    for cand in candidates:
        if len(cand) == 0 or int(cand) == 1:
            continue
        if isPrime(int(cand)):
            answer += 1
    return answer