def solution(arr):
    answer = [arr[0]]
    [answer.append(a) for a in arr if answer[-1] != a]
    
    return answer