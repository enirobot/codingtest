from typing import List
from collections import defaultdict

def solution(survey: List[str], choices: List[int]) -> str:
    personality_inventory = ["RT", "CF", "JM", "AN"]

    checked = defaultdict(int)

    for word, choice in zip(survey, choices):
        quotient = choice // 4
        remainder = choice % 4

        checked[word[quotient]] += 4 - remainder if quotient < 1 else remainder

    answer = ""
    for word in personality_inventory:
        first_word, second_word = word[0], word[-1]
        first_count, second_count = checked[first_word], checked[second_word]
        
        if first_count > second_count:
            answer += first_word
        elif first_count == second_count:
            if first_word > second_word:
                answer += second_word
            else:
                answer += first_word
        else:
            answer += second_word

    return answer


if __name__ == "__main__":
    # survey = ["AN", "CF", "MJ", "RT", "NA"]
    # choices = [5, 3, 2, 7, 5]
    survey = ["TR", "RT", "TR"]
    choices = [7, 1, 3]
    print(solution(survey, choices))
