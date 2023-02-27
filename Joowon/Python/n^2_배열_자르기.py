def solution(n, left, right):
    answer = [max(i//n, i%n) + 1 for i in range(left, right+1)]


    return answer

print(solution(3, 2, 5)) # 답: [3,2,2,3]
print(solution(4, 7, 14)) # 답: [4,3,3,3,4,4,4,4]