from typing import List


# def solution(prices: List[int]) -> List[int]:
#     answer = [0] * len(prices)
#     stack = []
#
#     for i, price in enumerate(prices):
#         while stack and price < prices[stack[-1]]:
#             last = stack.pop()
#             answer[last] = i - last
#         stack.append(i)
#
#     while stack:
#         last = stack.pop()
#         answer[last] = len(prices) - last - 1
#
#     return answer


def solution(prices: List[int]) -> List[int]:
    # 끝날 때까지 모든 값들의 가격이 떨어지지 않는 경우를 포함하여 리스트 만듦
    answer = [len(prices) - i - 1 for i in range(len(prices))]
    stack = []

    for i, price in enumerate(prices):
        # 가격이 떨어지는 경우
        while stack and price < prices[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last

        # 현재의 가격도 나중에 나올 값들과 비교를 위해 스택에 넣음
        stack.append(i)
        # print(f'index: {i}, price: {price}, answer: {answer}, stack: {stack}')

    return answer


if __name__ == "__main__":
    prices = [1, 2, 3, 2, 3]
    print(solution(prices))