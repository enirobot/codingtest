from math import isqrt, sqrt


def solution(left: int, right: int) -> int:
    total_number = 0
    for number in range(left, right+1):
        if isqrt(number) == sqrt(number):
            total_number -= number
        else:
            total_number += number

    return total_number


if __name__ == "__main__":
    left = 13
    right = 17
    print(solution(left, right))