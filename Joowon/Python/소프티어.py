def dfs(answer, nodeList, sumList, visited, graph):
    cpNodeList = nodeList[:]
    
    while cpNodeList:
        nextNode, nextDistance = cpNodeList.pop()

        if nextNode in visited:
            continue
        
        visited.append(nextNode)
        sumList.append(answer + nextDistance)
        dfs(answer + nextDistance, graph[nextNode], sumList, visited, graph)

if __name__ == '__main__':
    N = 7
    graph = {
        1: [[2, 5], [3, 2], [4, 8]],
        2: [[1, 5]],
        3: [[1, 2], [5, 4], [6, 1]],
        4: [[1, 8], [7, 6]],
        5: [[3, 4]],
        6: [[3, 1]],
        7: [[4, 6]]
    }
    
    for i in range(1, 7):
        visited = [i]
        sumList = []
        dfs(0, graph[i], sumList, visited, graph)
        print(sum(sumList))