from typing import List


def solution(progresses: List[int], speeds: List[int]) -> List[int]:
    # python list는 pop(0)을 하면 모든 값이 한 칸씩 시프팅되어
    # O(n)이 걸리므로 리스트를 뒤집어 사용 (pop()은 O(1))
    progresses = progresses[::-1]
    speeds = speeds[::-1]
    answer = []

    day = 0
    count = 0
    while progresses:
        print(f'day: {day}, count: {count}, progress: {progresses[-1] + speeds[-1] * day}, answer: {answer}')

        # 진도율이 100%를 넘어가면
        if (progresses[-1] + speeds[-1] * day) >= 100:
            count += 1
            progresses.pop()
            speeds.pop()
        else:
            day += 1
            # 기능 개선 완료된 것들이 있으면
            if count > 0:
                answer.append(count)
                count = 0


    answer.append(count)

    return answer


if __name__ == "__main__":
    # progresses = [95, 90, 99, 99, 80, 99]
    # speeds = [1, 1, 1, 1, 1, 1]
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]
    print(solution(progresses, speeds))