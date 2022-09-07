def solution(lottos, win_nums):
    answer = []
    zeroNum = lottos.count(0)
    a = len(list(filter(lambda x: x in win_nums, lottos)))
    answer = [6 if 6-(a+zeroNum)+1 > 6 else 6-(a+zeroNum)+1, 6 if 6-a+1 >= 6 else 6-a+1]
    
    return answer