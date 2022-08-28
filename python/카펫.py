# from typing import List
#
#
# """
# yellow의 넓이를 기준으로 brown의 갯수를 구하여 카펫의 크기를 알아냄
# width * height = yellow
# 2width + 2height + 4 = brown
# """
#
#
# def solution(brown: int, yellow: int) -> List[int]:
#     # yellow로 만들 수 있는 세로 길이
#     for height in range(1, yellow + 1):
#         print(height)
#         if yellow % height == 0:
#             width = yellow // height
#             if 2 * (width + height) + 4 == brown:
#                 return [width + 2, height + 2]
#     return []


from typing import List
import timeit

"""
yellow의 넓이를 기준으로 brown의 갯수를 구하여 카펫의 크기를 알아냄
width * height = yellow
2 * (width + height) + 4 = brown
"""


# def solution(brown: int, yellow: int) -> List[int]:
#     for height in range(1, yellow + 1):
#         width = yellow / height
#         if 2 * (width + height) + 4 == brown:
#             return [width + 2, height + 2]


def solution(brown: int, yellow: int) -> List[int]:
    for height in range(1, yellow + 1):
        # width는 자연수이므로 나머지가 없어야 함
        # width = yellow / height
        if yellow % height == 0:
            width = yellow // height
            print(f'width: {width}, height: {height}, 2*({width}+{height})+4 = {2 * (width + height) + 4}, brown: {brown}')
            if 2 * (width + height) + 4 == brown:
                return [width + 2, height + 2]


# def solution(brown: int, yellow: int) -> List[int]:
#     for height in range(1, yellow + 1):
#         width, remainder = divmod(yellow, height)
#         if remainder == 0:
#             if 2 * (height + width) + 4 == brown:
#                 return [width + 2, height + 2]


if __name__ == "__main__":
    brown = 10
    yellow = 2
    start_time = timeit.default_timer()
    print(solution(brown, yellow))
    terminate_time = timeit.default_timer()
    print("%f초 걸렸습니다." % (terminate_time - start_time))

