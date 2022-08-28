# from typing import List
#
#
# def solution(participant: List[str], completion: List[str]) -> str:
#     sorted_participant = sorted(participant)
#     sorted_completion = sorted(completion)
#
#     for index in range(len(sorted_completion)):
#         if sorted_participant[index] != sorted_completion[index]:
#             return sorted_participant[index]
#
#     return sorted_participant[-1]


# from typing import List
# from collections import defaultdict
#
#
# def solution(participant: List[str], completion: List[str]) -> str:
#     participant_dic = defaultdict(int)
#
#     for name in participant:
#         participant_dic[name] += 1
#
#     for name in completion:
#         participant_dic[name] -= 1
#         if participant_dic[name] == 0:
#             del participant_dic[name]
#
#     print(participant_dic)
#
#     return list(participant_dic)[0]


# from typing import List
# from collections import defaultdict
#
#
# def solution(participant: List[str], completion: List[str]) -> str:
#     dictionary = defaultdict(int)
#     answer = str()
#
#     for name in participant:
#         dictionary[name] += 1
#
#     for name in completion:
#         dictionary[name] -= 1
#
#     for name in participant:
#         if dictionary[name] > 0:
#             answer = name
#             break
#
#     return answer


# from typing import List
# from collections import defaultdict
#
#
# def solution(participant: List[str], completion: List[str]) -> str:
#     dictionary = defaultdict(int)
#     answer = str()
#
#     # 완주자 카운트
#     for name in completion:
#         dictionary[name] += 1
#
#     print(f'dictionary: {dict(dictionary)}')
#
#     # 참가자 카운트
#     for name in participant:
#         dictionary[name] -= 1
#
#         # 참가자가 완주하지 못 했으면
#         if dictionary[name] < 0:
#             answer = name
#             break
#
#     print(f'dictionary: {dict(dictionary)}')
#
#     return answer


from typing import List
from collections import Counter


def solution(participant: List[str], completion: List[str]) -> str:
    answer = Counter(participant) - Counter(completion)
    return list(answer)[0]


if __name__ == "__main__":
    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["stanko", "ana", "mislav"]
    print(f'result: {solution(participant, completion)}')