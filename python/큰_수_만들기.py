def solution(number: str, k: int) -> str:
    stack = []
    for n in number:
        print(n)
        while stack and k > 0 and stack[-1] < n:
            stack.pop()
            k -= 1
        stack.append(n)
        print(f'k: {k}, stk: {stack}')

    return "".join(stack[:len(stack) - k])


# def solution(number: str, k: int) -> str:
#     ciphers = len(number) - k
#     max_number = []
#     print(number)
#
#     left = 0
#     for i in range(ciphers):
#         right = k + i + 1
#         sub_num = number[left:right]
#         max_val = max(sub_num)
#         left = left + sub_num.index(max_val) + 1
#         max_number.append(max_val)
#         print(f'left: {left}, right: {right}, max_val: {max_val}, sub_num: {sub_num}')
#     return ''.join(max_number)


if __name__ == "__main__":
    # number = "4177252841"
    # k = 4
    # number = "1924"
    # k = 2
    # number = "1231234"
    # k = 3
    number = "1000"
    k = 2
    print(solution(number, k))