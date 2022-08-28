# from typing import List
#
#
# def to_swap(n1: str, n2: str) -> bool:
#     return n1 + n2 < n2 + n1
#
#
# def solution(numbers: List[int]) -> str:
#     str_num = list(map(str, numbers))
#     str_num.sort(reverse=True)
#
#     for i in range(1, len(str_num)):
#         j = i
#         while j > 0 and to_swap(str_num[j - 1], str_num[j]):
#             str_num[j], str_num[j - 1] = str_num[j - 1], str_num[j]
#             j -= 1
#         i += 1
#
#     return str(int(''.join(str_num)))
from typing import List

"""
사전의 단어 순서로 내림차순하고 합치면
이어 붙여 만들 수 있는 가장 큰 수를 만들 수 있다.
"""


def solution(numbers: List[int]) -> str:
    nums = list(map(str, numbers))
    print(f'nums: {nums}')
    print(sorted(nums, reverse=True))
    # 숫자가 0 ~ 1000의 범위를 가지므로 최소한 3자리 이상으로 만들어 비교
    nums.sort(key=lambda x: x * 3, reverse=True)
    print(f'sorted_nums: {nums}')
    # 문자열이 숫자의 형태가 아닐 수 있으므로 숫자로 바꿔준 후 다시 문자열로 변환
    return str(int(''.join(nums)))


if __name__ == "__main__":
    # numbers = [6, 10, 2]
    numbers = [3, 30, 34, 5, 9]
    print(solution(numbers))
    print('33' > '323')
    print('A' > 'a')
    print(sorted(['A', 'a']))

    # 문자열이 ASCII 코드값을 기준으로 비교되는 점을 이용했다.
