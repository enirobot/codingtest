def solution(s):
    answer = ''
    
    numList = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for i, num in enumerate(numList):
        if num in s:
            s = s.replace(num, str(i))
    answer = s
    
    
    return int(answer)