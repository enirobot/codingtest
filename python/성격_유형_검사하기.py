from typing import List
from collections import defaultdict

def solution(survey: List[str], choices: List[int]) -> str:
    personality_inventory = ["RT", "CF", "JM", "AN"]

    checked = defaultdict(int)

    for types, choice in zip(survey, choices):
        quotient = choice // 4
        remainder = choice % 4
        personality_type = types[quotient];

        checked[personality_type] += 4 - remainder if quotient < 1 else remainder

    answer = ""
    for first_type, second_type in map(lambda x: [*x], personality_inventory):
        first_count, second_count = checked[first_type], checked[second_type]
        
        if first_count > second_count:
            answer += first_type
        elif first_count < second_count:
            answer += second_type
        else:
            if first_type > second_type:
                answer += second_type
            else:
                answer += first_type

    return answer


if __name__ == "__main__":
    # survey = ["AN", "CF", "MJ", "RT", "NA"]
    # choices = [5, 3, 2, 7, 5]
    survey = ["TR", "RT", "TR"]
    choices = [7, 1, 3]
    print(solution(survey, choices))
