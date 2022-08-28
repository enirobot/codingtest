from typing import *


def prime_list(n: int) -> List[int]:
    prime_numbers = [True for _ in range(n + 1)]

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if prime_numbers[i]:
            for j in range(i + i, n + 1, i):
                prime_numbers[j] = False

    return prime_numbers


def solution(nums: List[int]) -> int:
    _nums = sorted(nums, reverse=True)
    max = sum(_nums[:3])

    prime_numbers = prime_list(max)

    count = 0
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                num = nums[i] + nums[j] + nums[k]
                if prime_numbers[num]:
                    count += 1

    return count


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    # nums = [1,2,7,6,4]
    print(solution(nums))
