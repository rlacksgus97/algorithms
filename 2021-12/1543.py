document = list(input())
word = list(input())

doc_i = 0
count = 0
while doc_i < len(document)-len(word)+1:
    # if document[doc_i:doc_i+len(word)] == word:
    if document[doc_i] == word[0]:
        flag = True
        for j in range(len(word)):
            if document[doc_i+j] != word[j]:
                flag = False
        if flag:
            count += 1
            doc_i = doc_i+len(word)
        else:
            doc_i += 1
    else:
        doc_i += 1

print(count)