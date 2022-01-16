import sys
l, c= map(int, sys.stdin.readline().split(' '))
chars = list(sys.stdin.readline().rstrip().split(' '))
chars.sort()

def rec_func(idx, password):
    if len(password) == l:
        consonant = 0
        vowel = 0
        for ch in password:
            if ch in ['a', 'e', 'i', 'o', 'u']:
                consonant += 1
            else:
                vowel += 1
        if consonant >= 1 and vowel >= 2:
            print(password)
        return
    if idx == c:
        return
    else:
        rec_func(idx+1, password+chars[idx])
        rec_func(idx+1, password)

rec_func(0, '')