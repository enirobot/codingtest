from typing import *


def target_number(numbers: List[int], target: int, depth: int) -> int:
    if len(numbers) != depth:
        num = numbers[depth]
        next_depth = depth + 1
        return target_number(numbers, target - num, next_depth) + target_number(numbers, target + num, next_depth)

    return 1 if target == 0 else 0


def solution(numbers: List[int], target: int) -> int:
    return target_number(numbers, target, 0)


if __name__ == "__main__":
    numbers = [1, 1, 1, 1, 1]
    target = 3
    print(solution(numbers, target))