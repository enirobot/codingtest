def solution(n: int) -> str:
    num = ['1','2','4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer


if __name__ == "__main__":
    n = 4
    print(solution(n))