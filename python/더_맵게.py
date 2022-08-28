import heapq
from typing import List


def solution(scoville: List[int], K: int) -> int:
    heap = scoville[:]
    # heap의 특성을 가지도록 만듦
    heapq.heapify(heap)
    print(f'heap: {heap}')

    count = 0
    # 가장 맵지 않은 음식의 스코빌 지수가 K보다 작으면
    while heap[0] < K:
        # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
        if len(heap) < 2:
            return -1
        least = heapq.heappop(heap)
        second = heapq.heappop(heap)
        mix = least + second * 2
        heapq.heappush(heap, mix)
        count += 1
        print(f'count: {count}, least: {least}, second: {second}, mix: {mix}')
        print(f'heap: {heap}')

    return count


if __name__ == '__main__':
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    print(f'result: {solution(scoville, K)}')
