def solution(array, commands):
    answer = []
    
    for ele in commands:
        answer.append(sorted(array[ele[0]-1:ele[1]])[ele[2]-1])
    
    
    return answer