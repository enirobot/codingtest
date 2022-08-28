import heapq
from collections import deque
from typing import List


def solution(jobs: List[List[int]]) -> int:
    # 요청 시간 기준 오름차순, 요청 시간 같으면 작업 시간 기준 오름차순
    q = deque(
        sorted(jobs, key=lambda x: (x[0], x[1]))
    )
    heap = []

    ms = 0
    total_ms = 0
    while q or heap:
        # print(f'ms: {ms}, total_ms: {total_ms}, q: {list(q)}, heap: {heap}')
        print(f'ms: {ms}, total_ms: {total_ms}')
        print(f'q: {list(q)}, heap: {heap}')
        # ms 이전에 들어온 요청이 있을 때, 작업 시간을 기준으로 최소 힙
        if q and q[0][0] <= ms:
            req_ms, time = q.popleft()
            heapq.heappush(
                heap,
                (time, req_ms)
            )
        else:
            if heap:
                time, req_ms = heapq.heappop(heap)
                total_ms += ms - req_ms + time
                ms += time
            # heap에 대기 중인 작업이 없으나 q에 대기 중인 작업이 있을 때
            else:
                req_ms, time = q.popleft()
                total_ms += time
                ms = req_ms + time
    # print(f'ms: {ms}, total_ms: {total_ms}, q: {list(q)}, heap: {heap}')
    print(f'ms: {ms}, total_ms: {total_ms}')
    print(f'q: {list(q)}, heap: {heap}')

    return total_ms // len(jobs)


if __name__ == '__main__':
    # jobs = [[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
    # jobs = [[0, 3], [1, 9], [2, 6], [3, 5], [4, 7], [31, 3], [32, 2], [35, 6]]
    # jobs = [[0, 3], [1, 9], [2, 6]]
    jobs = [[1, 9], [2, 6], [1, 3], [3, 5], [4, 7], [31, 3], [33, 6]]
    print(f'result: {solution(jobs)}')
