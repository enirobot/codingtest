from collections import deque

def solution(numbers, target):
    answer = 0
    length = len(numbers)
    dq = deque()
    dq.append([numbers[0], 0])
    dq.append([-1 * numbers[0], 0])
    
    while dq:
        num, idx = dq.popleft()
        if idx == length-1:
            if num == target:
                answer += 1
        else:
            dq.append([num + numbers[idx+1], idx+1])
            dq.append([num + -1 * numbers[idx+1], idx+1])
    
    
    return answer