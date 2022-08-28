from typing import List
from random import randint


# def solution(citations: List[int]) -> int:
#     print(f'citations: {citations}')
#     sorted_citations = sorted(citations)
#     citations_len = len(sorted_citations)
#     print(f'sorted_citations: {sorted_citations}')
#
#     for i in range(citations_len):
#         paper_num = citations_len - i
#         print(f'i: {i}, paper_num: {paper_num}, sorted_citations[{i}]: {sorted_citations[i]}')
#
#         if paper_num <= sorted_citations[i]:
#             return paper_num
#
#     return 0


def solution(citations: List[int]) -> int:
    sorted_citations = sorted(citations)
    paper_num_range = range(len(citations), 0, -1)
    # paper_num_range = reversed(range(1, len(citations) + 1))
    print(f'citations: {citations}')
    print(f'sorted_citations: {sorted_citations}')
    for citation, paper_num in zip(sorted_citations, paper_num_range):
        print(f'citation: {citation}, paper_num: {paper_num}')
        if citation >= paper_num:
            return paper_num

    return 0



if __name__ == "__main__":
    # citations = [3, 3, 0, 6, 1, 5]
    # citations = [66, 18, 5, 21, 87]
    # citations = [randint(0, 10001) for _ in range(randint(1, 1001))]
    # citations = [randint(0, 100) for _ in range(randint(1, 20))]
    # citations = [20,21,22,23]
    # citations = [8, 3, 5, 3, 25]
    citations = [3, 0, 6, 1, 5]
    # citations = [0]
    print(solution(citations))
