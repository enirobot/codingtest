from typing import List


def solution(array: List[int], commands: List[List[int]]) -> List[int]:
    answer = []

    for command in commands:
        start, end, index = command
        sub_array = array[start - 1: end]
        sub_array.sort()
        answer.append(sub_array[index - 1])
        print(f'sorted_sub_array: {sub_array}, {index}번째 수: {sub_array[index - 1]}')

    return answer


if __name__ == "__main__":
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    print(solution(array, commands))
