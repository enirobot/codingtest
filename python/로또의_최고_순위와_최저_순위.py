def solution(lottos, win_nums):
    nums = [0 for _ in range(46)]
    rank = [6, 6, 5, 4, 3, 2, 1]
    zero = 0
    count = 0

    for i in win_nums:
        nums[i] = 1

    for i in lottos:
        if i == 0:
            zero += 1
            continue
        if nums[i] == 1:
            count += 1

    return [
        rank[count + zero],
        rank[count]
    ]


if __name__ == "__main__":
    lottos = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]
    print(solution(lottos, win_nums))