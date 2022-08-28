from typing import List


def solution(n: int, lost: List[int], reserve: List[int]) -> int:
    # KeyError를 피하기 위한 0, n + 1의 더미 데이터도 포함
    students = {i: 1 for i in range(n + 2)}
    ready = n

    print(students)
    for i in reserve:
        students[i] += 1
    # print(f'student + reserve: {students}')
    print(students)

    for i in lost:
        students[i] -= 1
    # print(f'student - lost: {students}')
    print(students)

    for i in lost:
        # 여벌 체육복을 가져왔지만 도난을 당한 경우 패스
        if students[i] > 0:
            continue

        left, right = i - 1, i + 1
        if students[left] > 1:
            students[left] -= 1
        elif students[right] > 1:
            students[right] -= 1
        else:
            ready -= 1
    # print(f'student: {students}')
    print(students)
    return ready


# def solution(n: int, lost: List[int], reserve: List[int]) -> int:
#     # KeyError를 피하기 위한 0, n + 1의 더미 데이터도 포함
#     students = {i: 1 for i in range(n + 2)}
#     ready = n
#
#     for i in reserve:
#         students[i] += 1
#
#     for i in lost:
#         students[i] -= 1
#
#     for i in lost:
#         # 여벌 체육복을 가져왔지만 도난을 당한 경우 패스
#         if students[i] > 0:
#             continue
#
#         left, right = i - 1, i + 1
#         if students[left] > 1:
#             students[left] -= 1
#
#         elif students[right] > 1:
#             students[right] -= 1
#
#         else:
#             ready -= 1
#
#     return ready


if __name__ == "__main__":
    # n = 5
    # lost = [2, 4, 5]
    # # reserve = [1, 3, 5]
    # reserve = [2, 3]
    # n = 3
    # lost = [3]
    # reserve = [1]
    # n = 5
    # lost = [2, 3]
    # reserve = [1]
    n = 5
    lost = [5, 3, 1]
    reserve = [2, 4]
    print(solution(n, lost, reserve))
