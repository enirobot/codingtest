def dfs(preNode, currentNode, sumList, lineNum, visited, graph):
    currentList = graph[currentNode]
    
    for i in range(len(currentList)):
        nextNode, weight = currentList[i]
        
        if nextNode in visited:
            continue
        
        visited.append(nextNode)
        lineNum[currentNode] += dfs(currentNode, nextNode, sumList, lineNum, visited, graph)
        sumList[currentNode]
        
    return lineNum[currentNode]

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

    visited = [1]
    lineNum = [1 for i in range(N+1)]
    sumList = [1 for i in range(N+1)]
    dfs(1, 1, sumList, lineNum, visited, graph)
    print(sum(sumList))