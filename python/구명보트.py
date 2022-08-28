from typing import List


def solution(people: List[int], limit: int) -> int:
    sorted_people = sorted(people)
    print(f'sorted_people: {sorted_people}')

    count = 0
    left, right = 0, len(sorted_people) - 1
    while left <= right:
        print(f'left: {left}, right: {right}, sorted_people: {sorted_people}')
        if sorted_people[left] <= limit - sorted_people[right]:
            left += 1
        right -= 1
        count += 1

    return count


if __name__ == "__main__":
    people = [70, 50, 80, 50]
    limit = 100
    # people = [70, 80, 50]
    # limit = 100
    print(solution(people, limit))