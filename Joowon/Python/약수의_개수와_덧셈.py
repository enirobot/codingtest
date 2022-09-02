def caculate_divisor(num):
    root_square = num**(1/2)
    check_square = False
    answer = 0
    
    if root_square == int(root_square):
        check_square = True
        root_square = int(root_square)
        answer += 1
    else:
        root_square = int(root_square) + 1
    
    for i in range(1, root_square):
        if num % i == 0:
            answer += 2
    
    return answer

def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        cd = caculate_divisor(i)
        if cd % 2 == 0:
            answer += i
        else:
            answer -= i
    
    
    return answer