import hashlib

s = input()
encoded_s = s.encode()
answer = hashlib.sha256(encoded_s).hexdigest()
print(answer)