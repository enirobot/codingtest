from collections import deque
import timeit
from random import randint


# 상하 이동거리 중 가장 짧은 거리 반환
def min_up_down(char: str) -> int:
    ord_char = ord(char)
    up = ord_char - 65      # 65 = 'A'
    down = 91 - ord_char    # 91 = 'Z' + 1
    return min(up, down)


def solution(name: str) -> int:
    # (인덱스, 문자), 시작지점이 0이므로 첫번째는 제외
    char_list = deque((i + 1, char) for i, char in enumerate(name[1:]) if char != 'A')
    name_len = len(name)
    print(f'name: {name}')
    print(f'char_list: {list(char_list)}')
    print('# while문 맨 마지막 부분에서 print')

    index = 0
    total = min_up_down(name[0])    # 첫번째는 상하 이동 거리만 포함
    # print(f'total: {total}, index: {index}, char: {name[0]}')
    while char_list:

        left = (name_len + index - char_list[-1][0]) % name_len     # 왼쪽 이동 거리
        right = (name_len - index + char_list[0][0]) % name_len     # 오른쪽 이동 거리

        # 오른쪽 이동 거리가 짧거나 같으면 deque의 왼쪽 원소 뽑고 그 위치로 이동
        # 왼쪽이 짧으면 deque의 오른쪽 원소 뽑고 그 위치로 이동
        index, char = char_list.popleft() if right <= left else char_list.pop()

        # 좌우 이동 거리 중 최소 값 + 상하 이동 거리 중 최소 값
        total += min(left, right) + min_up_down(char)
        print(f'char_list: {list(char_list)}')
        print(f'total: {total}, index: {index}, char: {char} left: {left}, right: {right}')

    return total


if __name__ == "__main__":
    # name = "JEROEN"
    # name = "JAN"
    # name = "ABBAAB"
    # name = "ABBAAAABA"
    name = "BABAAAAB"
    # name = "BBABAAAB"
    # name = "ABABAAAAAAABA"
    # name = ''.join([chr(randint(65, 90)) for _ in range(randint(1, 10000))])
    start_time = timeit.default_timer()
    print(solution(name))
    terminate_time = timeit.default_timer()
    print("%f초 걸렸습니다." % (terminate_time - start_time))
