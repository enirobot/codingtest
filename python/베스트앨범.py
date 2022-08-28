from typing import List
from collections import defaultdict


def solution(genres: List[str], plays: List[int]) -> List[int]:
    # 장르 별로 총 재생된 횟수를 보관
    top_genres = defaultdict(int)
    # 각각의 음악 정보(고유번호, 재생된 횟수)를 카테고리(장르)별로 보관
    category = defaultdict(list)

    for id in range(len(genres)):
        genre, play_num = genres[id], plays[id]
        top_genres[genre] += play_num
        category[genre].append(
            (id, play_num)
        )

    print(f'top_genres: {dict(top_genres)}')
    print(f'category: {dict(category)}')

    # 가장 많이 재생된 장르가 앞에 오도록 내림차순
    sorted_top_genres = sorted(
        top_genres,
        key=lambda x: top_genres[x],
        reverse=True
    )
    print(f'sorted_top_genres: {sorted_top_genres}')

    answer = []
    for genre in sorted_top_genres:
        # 재생 횟수로 내림차순 정렬, 재생 횟수가 같으면 고유번호 기준으로 오름차순 정렬
        sorted_genre = sorted(
            category[genre],
            key=lambda x: (-x[-1], x[0])
        )
        print(f'genre: {genre}, sorted_genre: {sorted_genre}')
        # 상위 2개 이하의 노래만 순서대로 id를 추출하여 리스트로 만듦
        answer += [
            id for (id, count) in sorted_genre[:2]
        ]
        print(f'answer: {answer}')

    return answer


# def solution(genres: List, plays: List) -> List:
#     genres_plays = []
#
#     for item in zip(genres, plays):
#         genres_plays.append(item)
#
#     genres_plays.sort(key=lambda music: (music[0], -music[-1]))
#
#     print(genres_plays)
#
#     answer = []
#     return answer


if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    print(solution(genres, plays))
