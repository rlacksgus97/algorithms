def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    for i in range(len(A)):
        if A[i] < B[0]:
            answer += 1
            B.pop(0)
    return answer