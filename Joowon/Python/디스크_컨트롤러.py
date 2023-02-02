from heapq import heappush
from heapq import heappop

def solution(jobs):
    answer = 0
    heap = []
    length = len(jobs)
    st, current, cnt = -1, 0, 0 # 이전 프로세스 시작 시간 / 현재 시간 / 몇 개의 프로세스가 실행되었는지 카운트

    while cnt < length:
        for ele in jobs:
            if st < ele[0] and current >= ele[0]:
                heappush(heap, [ele[1], ele[0]])

        if len(heap) > 0:
            minValue = heappop(heap)
            st = current
            current += minValue[0]
            cnt += 1

            answer += (current - minValue[1])
        else:
            current += 1

    answer //= length


    return answer