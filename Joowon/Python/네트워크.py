from collections import deque

def solution(n, computers):
    answer = 0
    visited = []
    dq = deque()
    dq.append(0)
    
    while len(visited) != n:
        for i in range(len(computers)):
            if i not in visited:
                dq.append(i)
                
                break
        while dq:
            connectIdx = dq.popleft()
            if connectIdx not in visited:
                visited.append(connectIdx)
                for idx, ele in enumerate(computers[connectIdx]):
                    if connectIdx == idx:
                        continue
                    if ele:
                        dq.append(idx)
        answer += 1
    
    
    return answer