def solution(a, b, g, s, w, t):
    answer = 10**16
    start, end = 0, answer

    while start <= end:
        mid = (start + end) // 2
        carryG = 0
        carryS = 0
        total = 0

        for i in range(len(t)):
            count = mid // (t[i]*2)
            count = mid // t[i] - count
            carry = w[i] * count
            tempCarryG = 0
            tempCarryS = 0

            if carry < g[i]:
                tempCarryG += carry
            else:
                tempCarryG += g[i]
            
            if carry < s[i]:
                tempCarryS += carry
            else:
                tempCarryS += s[i]
            
            carryG += tempCarryG
            carryS += tempCarryS

            if tempCarryG + tempCarryS >= carry:
                total += carry
            else:
                total += tempCarryG + tempCarryS
        
        if carryG >= a and carryS >= b and total >= a + b:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    
    
    return answer


print(solution(10, 10, [100], [100], [7], [10])) # 답 : 50
print(solution(90, 500, [70,70,0], [0,0,500], [100,100,2], [4,8,1])) # 답: 499