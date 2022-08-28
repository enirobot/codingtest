from typing import List
from collections import defaultdict


def solution(answers: List[int]) -> List[int]:
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    grades = defaultdict(int)
    for i, answer in enumerate(answers):
        if a[i % len(a)] == answer:
            grades[1] += 1
        if b[i % len(b)] == answer:
            grades[2] += 1
        if c[i % len(c)] == answer:
            grades[3] += 1

    print(f'grades: {dict(grades)}')
    highest_score_student = max(grades, key=lambda x: grades[x])
    print(f'highest_score_student: {highest_score_student}')

    return sorted(
        [student for student in grades
         if grades[highest_score_student] == grades[student]]
    )


if __name__ == "__main__":
    answers = [1, 2, 3, 4, 5]
    # answers = [1, 3, 2, 4, 2]
    print(solution(answers))

