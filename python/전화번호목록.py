from typing import List
from collections import defaultdict


# def solution(phone_book: List[str]) -> bool:
#     _phone_book = {phone_number: 0 for phone_number in phone_book}
#     sorted_phone_book = sorted(phone_book, key=len, reverse=True)
#
#     for phone_number in sorted_phone_book:
#         search_value = str()
#         for number in phone_number:
#             search_value += number
#             if search_value in _phone_book and search_value != phone_number:
#                 return False
#     return True


# def solution(phone_book: List[str]) -> bool:
#     dictionary = {phone_number: 0 for phone_number in phone_book}
#     print(f'dictionary: {dictionary}')
#
#     for phone_number in dictionary:
#         temp_number = str()
#         # 전화번호 맨 앞부터 for문 순회할 때마다 하나씩 이어붙이며 검사
#         for number in phone_number:
#             temp_number += number
#             print(f'phone_number: {phone_number}, temp_number: {temp_number}')
#             # 순회할 때마다 하나씩 이어붙인 번호가 dictionary에 존재하고 자기 자신이 아니면
#             if (temp_number in dictionary
#                     and temp_number != phone_number):
#                 return False
#     return True


def solution(phone_book: List[str]) -> bool:
    # 사전식 순서로 정렬하여 비슷한 값끼리 뭉치도록 함
    sorted_phone_book = sorted(phone_book)
    print(f'phone_book: {phone_book}')
    print(f'sorted_phone_book: {sorted_phone_book}')

    for first, second in zip(sorted_phone_book, sorted_phone_book[1:]):
        print(f'first: {first}, second: {second}')
        # 문자열 시작 부분부터 검사, in과는 다르게 앞부분부터 일치하지 않으면 바로 False 반환
        if second.startswith(first):
            return False
    return True


if __name__ == '__main__':
    phone_book = ["119", "97674223", "1195524421"]
    print(solution(phone_book))
    a = "129845723985798"
    if "457" in a:
        print('있음')
    else:
        print('없음')

    print("457" in "12435457")
    print("12435457".startswith("457"))