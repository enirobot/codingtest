def solution(citations):
    answer = 0
    length = len(citations)
    citations.sort()

    st, et = 0, len(citations) - 1
    while st <= et:
        mid = (st + et) // 2

        if length - mid <= citations[mid]:
            et = mid - 1
            answer = length - mid
        else:
            st = mid + 1


    return answer

print(solution([3, 0, 6, 1, 5])) # 답: 3