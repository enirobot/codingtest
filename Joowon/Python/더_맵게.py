from heapq import heappush, heappop, heapify

def solution(scoville, K):
    answer = -1
    cnt = 0
    heapify(scoville)
    
    if scoville[0] >= K:
        return 0
    
    while scoville[0] < K and len(scoville) > 1:
        ele1 = heappop(scoville)
        ele2 = heappop(scoville)
        sumEle = ele1 + (ele2 * 2)
        heappush(scoville, sumEle)
        cnt += 1
    
    if scoville[0] >= K:
        answer = cnt
    
    
    return answer