def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        cd = i**(1/2)
        
        if cd == int(cd): answer -= i
        else: answer += i
    
    return answer