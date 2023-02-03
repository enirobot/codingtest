from collections import deque

def compareWord(word1, word2):
    cnt = 0
    length = len(word1)
    for i in range(length):
        if word1[i] != word2[i]:
            if cnt:
                return False
            cnt += 1
    
    return True

def solution(begin, target, words):
    answer = []
    dq = deque()
    visited = []
    dq.append([begin, 0])
    
    while dq:
        word, cnt = dq.popleft()
        if word not in visited:
            visited.append(word)
            
            for ele in words:
                if compareWord(word, ele):
                    if ele == target:
                        answer.append(cnt+1)
                    else:
                        dq.append([ele, cnt+1])
    
    answer = 0 if not answer else min(answer)
    return answer