from ctypes import Union
from typing import List
from collections import deque


def solution(bridge_length: int, weight: int, truck_weights: List[int]) -> int:
    truck_weights = deque(truck_weights)
    # (트럭 무게, 도착 시간)
    trucks: Union(int, int) = deque()

    acceptable_weight = weight
    time = 0
    while trucks or truck_weights:
        time += 1

        # 맨 앞에서 달리고 있는 트럭이 다리를 완전히 건너간 시간이면
        if trucks and time == trucks[0][1]:
            acceptable_weight += trucks.popleft()[0]

        # 맨 앞에서 대기하는 트럭의 무게와 다리의 허용 무게 체크
        if truck_weights and truck_weights[0] <= acceptable_weight:
            acceptable_weight -= truck_weights[0]
            trucks.append(
                (truck_weights.popleft(), time + bridge_length)
            )
        print(f'time: {time}, acceptable_weight: {acceptable_weight}, trucks: {list(trucks)}')

    return time


# def solution(bridge_length: int, weight: int, truck_weights: List) -> int:
#     trucks = truck_weights[::-1]
#     # (트럭 무게, 도착 시간)
#     q: (int, int) = deque()
#
#     maximum_load = weight
#     time = 0
#     while q or trucks:
#         time += 1
#
#         if q and time == q[0][1]:
#             maximum_load += q.popleft()[0]
#
#         if trucks and trucks[-1] <= maximum_load:
#             maximum_load -= trucks[-1]
#             q.append(
#                 (trucks.pop(), time + bridge_length)
#             )
#
#     return time


if __name__ == "__main__":
    bridge_length = 2
    weight = 10
    truck_weights = [7, 4, 5, 6]
    print(solution(bridge_length, weight, truck_weights))