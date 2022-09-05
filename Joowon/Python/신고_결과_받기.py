def solution(id_list, report, k):
    answer = [0 for i in id_list]
    notifyDict = {name: 0 for name in id_list}
    
    for name in set(report):
        notifyDict[name.split()[1]] += 1
    
    for name in set(report):
        if notifyDict[name.split()[1]] >= k:
            answer[id_list.index(name.split()[0])] += 1
    
    return answer