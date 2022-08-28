from typing import List
from collections import deque


def solution(priorities: List[int], location: int) -> int:
    # 오름차순 정렬하여 끝에 큰 값이 오게 함
    sorted_priorities = sorted(priorities)
    q = deque([
        (index, priority) for (index, priority) in enumerate(priorities)
    ])

    order = 0
    while q:
        index, priority = q.popleft()
        # 가장 큰 값이면
        if priority == sorted_priorities[-1]:
            sorted_priorities.pop()
            order += 1

            # 내가 요청한 문서이면
            if index == location:
                break
        else:
            q.append((index, priority))
        print(f'index: {index}, priority: {priority}, sorted_priorities: {sorted_priorities}, q: {q}')

    return order


if __name__ == "__main__":
    # priorities = [1, 2, 3, 4, 5, 5]
    # location = 1
    priorities = [1, 1, 9, 1, 1, 1]
    location = 0
    print(solution(priorities, location))
