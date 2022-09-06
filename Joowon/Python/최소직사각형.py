def solution(sizes):
    answer = max(sum(sizes, [])) * max([min(size) for size in sizes])
    
    
    return answer