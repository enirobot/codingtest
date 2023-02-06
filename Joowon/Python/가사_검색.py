def makeTrie(headNode, word):
    node = headNode

    for ele in word:
        if ele not in node:
            node[ele] = dict()
        node = node[ele]

        if 'length' not in node:
            node['length'] = dict()

        if len(word) not in node['length']:
            node['length'][len(word)] = 1
        else:
            node['length'][len(word)] += 1

def searchMatch(query, headNode):
    node = headNode

    for ele in query:
        if ele == '?':
            if len(query) not in node['length']:
                return 0
            else:
                return node['length'][len(query)]
        elif ele not in node:
            return 0

        node = node[ele]

def solution(words, queries):
    answer = []
    headNode = dict()
    headInvNode = dict()
    cntDict = dict()
    
    for word in words:
        makeTrie(headNode, word)
        makeTrie(headInvNode, word[::-1])
        
        if len(word) not in cntDict:
            cntDict[len(word)] = 1
        else:
            cntDict[len(word)] += 1
    
    for query in queries:
        if query[0] == '?' and query[-1] == '?':
            if len(query) not in cntDict:
                answer.append(0)
            else:
                answer.append(cntDict[len(query)])
        elif query[0] == '?':
            answer.append(searchMatch(query[::-1], headInvNode))
        else:
            answer.append(searchMatch(query, headNode))


    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?", "?????", "??????????????????"])) # 답: [3, 2, 4, 1, 0, 5, 0]