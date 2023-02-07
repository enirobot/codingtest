def solution(clothes):
    answer = 1
    clothDict = dict()
    
    for cloth in clothes:
        if cloth[1] not in clothDict:
            clothDict[cloth[1]] = 1
        else:
            clothDict[cloth[1]] += 1
    
    for key, value in clothDict.items():
        # nCr조합 수식 = n!/((n-r)! * r!)
        # 여기서 조합 수식을 풀면 2C1, 3C1 이런식으로 옷가지 수 중 최소 한 개를 입는 경우의 수를 알 수 있음
        # 근데 그 경우의 수가 각각의 옷 개수와 같음(옷이 3개면 3개 중에 1개 고르는 가지수는 3개)
        # 그래서 아래와 같이 answer * value 가 되는 것임
        # 근데 뒤에 + 1 은 그럼 뭐냐고 생각할 수 있는데
        # 이것은 옷을 입지 않은 경우도 있으므로 그 경우를 더해준 것임
        # 그래서 최종적으로 answer를 구하고 마지막에 모두 입지 않은 경우의 수를 제거하기 위해 - 1 을 한 것임
        answer *= (value + 1)
    
    
    return answer - 1

    print(solution())