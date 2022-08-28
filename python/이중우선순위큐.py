# import heapq
# from typing import List, Tuple
#
#
# # 동기화에 사용할 string object의 주소가 담긴 변수
# REMOVED = 'REMOVED'
# LIVE = 'LIVE'
#
#
# def get(_heap: List[Tuple[int, int, List[str]]]) -> Tuple[int, int, List[str]]:
#     """ heap[0] 값이 다른 heap에서 이미 지워진 값이면 삭제하고 아니면 return """
#     while _heap:
#         priority, val, is_removed = _heap[0]
#         if is_removed[0] is REMOVED:
#             heapq.heappop(_heap)
#         else:
#             return _heap[0]
#
#
# def pop(_heap: List[Tuple[int, int, List[str]]]) -> Tuple[int, int, List[str]]:
#     """ pop한 값이 다른 heap에서 지워진 값이 아니면, 다른 heap과 동기화 후 return """
#     while _heap:
#         entry = heapq.heappop(_heap)
#         priority, val, is_removed = entry
#         if is_removed[0] is not REMOVED:
#             is_removed[0] = REMOVED
#             return entry
#
#
# def solution(operations: List[str]) -> List[int]:
#     min_heap, max_heap = [], []
#     q_len = 0
#
#     for line in operations:
#         cmd, attr = line.split()
#         if cmd == 'I':
#             val = int(attr)
#             min_priority, max_priority = val, -val
#             # 서로 다른 heap을 동기화할 때 사용할 리스트
#             is_removed = [LIVE]
#             heapq.heappush(min_heap, (min_priority, val, is_removed))
#             heapq.heappush(max_heap, (max_priority, val, is_removed))
#             q_len += 1
#         elif cmd == 'D' and q_len > 0:
#             if attr == '1':
#                 pop(max_heap)
#             elif attr == '-1':
#                 pop(min_heap)
#             q_len -= 1
#         print(f'q_len: {q_len}, line: {line}')
#         print(f'min_heap: {min_heap}')
#         print(f'max_heap: {max_heap}')
#
#     if q_len > 0:
#         _, max_val, _ = get(max_heap)
#         _, min_val, _ = get(min_heap)
#         print(f'q_len: {q_len}')
#         print(f'min_heap: {min_heap}')
#         print(f'max_heap: {max_heap}')
#         return [max_val, min_val]
#
#     print(f'q_len: {q_len}')
#     print(f'min_heap: {min_heap}')
#     print(f'max_heap: {max_heap}')
#
#     return [0, 0]


# import heapq
# from typing import List, Tuple
#
#
# def get(_heap: List[Tuple[int, int, List[bool]]]) -> Tuple[int, int, List[bool]]:
#     """ heap[0] 값이 다른 heap에서 이미 지워진 값이면 삭제하고 아니면 return """
#     while _heap:
#         priority, val, is_removed = _heap[0]
#         if is_removed[0]:
#             heapq.heappop(_heap)
#         else:
#             return _heap[0]
#
#
# def pop(_heap: List[Tuple[int, int, List[bool]]]) -> Tuple[int, int, List[bool]]:
#     """ pop한 값이 다른 heap에서 지워진 값이 아니면, 다른 heap과 동기화 후 return """
#     while _heap:
#         entry = heapq.heappop(_heap)
#         priority, val, is_removed = entry
#         if not is_removed[0]:
#             is_removed[0] = True
#             return entry
#
#
# def solution(operations: List[str]) -> List[int]:
#     min_heap, max_heap = [], []
#     q_len = 0
#
#     for line in operations:
#         cmd, attr = line.split()
#         if cmd == 'I':
#             val = int(attr)
#             min_priority, max_priority = val, -val
#             # 서로 다른 heap에 있는 값을 동기화할 때 사용할 리스트
#             is_removed = [False]
#             heapq.heappush(min_heap, (min_priority, val, is_removed))
#             heapq.heappush(max_heap, (max_priority, val, is_removed))
#             q_len += 1
#         elif cmd == 'D' and q_len > 0:
#             if attr == '1':
#                 pop(max_heap)
#             elif attr == '-1':
#                 pop(min_heap)
#             q_len -= 1
#         print(f'q_len: {q_len}, line: {line}')
#         print(f'min_heap: {min_heap}')
#         print(f'max_heap: {max_heap}')
#
#     if q_len > 0:
#         _, max_val, _ = get(max_heap)
#         _, min_val, _ = get(min_heap)
#         print(f'q_len: {q_len}')
#         print(f'min_heap: {min_heap}')
#         print(f'max_heap: {max_heap}')
#         return [max_val, min_val]
#
#     print(f'q_len: {q_len}')
#     print(f'min_heap: {min_heap}')
#     print(f'max_heap: {max_heap}')
#
#     return [0, 0]


import heapq
from typing import List, Tuple


def get(_heap: List[Tuple[int, int, List[bool]]]) -> Tuple[int, int, List[bool]]:
    """ heap[0] 값이 다른 heap에서 이미 지워진 값이면 삭제하고 아니면 return """
    while _heap:
        priority, val, is_removed = _heap[0]
        if is_removed[0]:
            heapq.heappop(_heap)
        else:
            return _heap[0]


def pop(_heap: List[Tuple[int, int, List[bool]]]) -> Tuple[int, int, List[bool]]:
    """ pop한 값이 다른 heap에서 지워진 값이 아니면, 다른 heap과 동기화 후 return """
    while _heap:
        entry = heapq.heappop(_heap)
        priority, val, is_removed = entry
        if not is_removed[0]:
            is_removed[0] = True
            return entry


def solution(operations: List[str]) -> List[int]:
    min_heap, max_heap = [], []
    q_len = 0

    for line in operations:
        cmd, attr = line.split()
        if cmd == 'I':
            val = int(attr)
            min_priority, max_priority = val, -val
            # 서로 다른 heap에 있는 값을 동기화할 때 사용할 리스트
            is_removed = [False]
            heapq.heappush(min_heap, (min_priority, val, is_removed))
            heapq.heappush(max_heap, (max_priority, val, is_removed))
            q_len += 1
        elif cmd == 'D' and q_len > 0:
            if attr == '1':
                pop(max_heap)
            elif attr == '-1':
                pop(min_heap)
            q_len -= 1

            if q_len <= 0 and (min_heap or max_heap):
                min_heap, max_heap = [], []

        print(f'q_len: {q_len}, line: {line}')
        print(f'min_heap: {min_heap}')
        print(f'max_heap: {max_heap}')

    if q_len > 0:
        _, max_val, _ = get(max_heap)
        _, min_val, _ = get(min_heap)
        print(f'q_len: {q_len}')
        print(f'min_heap: {min_heap}')
        print(f'max_heap: {max_heap}')
        return [max_val, min_val]

    print(f'q_len: {q_len}')
    print(f'min_heap: {min_heap}')
    print(f'max_heap: {max_heap}')

    return [0, 0]


if __name__ == '__main__':
    operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
    # operations = ["I 7","I 5","I -5","D -1"]
    # operations = ["I 16","D 1"]
    # operations = ["I 2", "I 4", "D -1", "I 1", "D 1"]
    print(f'result: {solution(operations)}')
