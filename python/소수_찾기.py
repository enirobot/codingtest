from itertools import permutations
from math import sqrt


# 소수임을 판정하기 위해선 number의 제곱근까지 수 중 1을 제외하고 그 자연수의 약수가 있는지 확인
def is_prime_number(number):
    if number < 2:
        return False

    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


def solution(numbers: str) -> int:
    # 중복 제거를 위해 set 사용
    nums = set()

    print(f'numbers: {numbers}')
    # numbers로 만들 수 있는 모든 숫자 생성
    for i in range(len(numbers)):
        nums.update(
            map(lambda x: int(''.join(x)),
                permutations(numbers, i + 1))   # 순열
        )
        print(f'i: {i}, nums: {nums}, permutations: {list(map(lambda x: int("".join(x)), permutations(numbers, i + 1)))}')
    print(f'nums: {nums}')

    # 소수인지 판별
    prime_numbers = [num for num in nums if is_prime_number(num)]
    print(f'prime_numbers: {prime_numbers}')

    return len(prime_numbers)


if __name__ == "__main__":
    # numbers = "17"
    numbers = "011"
    print(solution(numbers))
    #
    # # a = "123456789"
    # a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # print(a)
    # print(a[1:])
    # print(a[2:])
    # print(a[1:2])
    # a[1:] = a[2:] + a[1:2]
    # print(a)
