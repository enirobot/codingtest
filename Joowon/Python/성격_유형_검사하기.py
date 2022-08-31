def solution(survey, choices):
    answer = ''
    score = [3, 2, 1, 0, 1, 2, 3]

    mind_dict = dict()
    mind_dict['R'] = 0
    mind_dict['T'] = 0
    mind_dict['C'] = 0
    mind_dict['F'] = 0
    mind_dict['J'] = 0
    mind_dict['M'] = 0
    mind_dict['A'] = 0
    mind_dict['N'] = 0

    for i, ele in enumerate(choices):
        mind_dict[survey[i][(ele-1)//4]] += score[ele-1]

    answer += 'R' if mind_dict['R'] >= mind_dict['T'] else 'T'
    answer += 'C' if mind_dict['C'] >= mind_dict['F'] else 'F'
    answer += 'J' if mind_dict['J'] >= mind_dict['M'] else 'M'
    answer += 'A' if mind_dict['A'] >= mind_dict['N'] else 'N'


    return answer