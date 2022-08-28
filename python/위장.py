# from typing import List
# from collections import Counter
# from functools import reduce


from typing import List
from collections import defaultdict
from functools import reduce


def solution(clothes: List[List[str]]) -> int:
    dictionary = defaultdict(int)

    # 옷 종류별로 카운트
    for name, kind in clothes:
        dictionary[kind] += 1

    print(f'dictionary: {dict(dictionary)}')

    values = dictionary.values()
    # (2(headgear의 수) + 1(안 입는 경우))
    # * (2(eyewear의 수) + 1)
    # * (3(face의 수) + 1)
    # - 1(적어도 하나의 옷은 입어야함) = 35
    # values가 [2, 2, 3]라고 하면  => (((1*(2+1))*(2+1))*(3+1)) - 1
    return reduce(lambda x, y: x*(y+1), values, 1) - 1


if __name__ == "__main__":
    clothes = [
        ["yellowhat", "headgear"],
        ["bluesunglasses", "eyewear"],
        ["green_turban", "headgear"],
        ["bluesunglasses", "eyewear"],
        ["crowmask", "face"],
        ["bluesunglasses", "face"],
        ["smoky_makeup", "face"]
    ]
    print(solution(clothes))