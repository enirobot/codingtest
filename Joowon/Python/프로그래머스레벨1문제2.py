# from heapq import heappush, heappop

# def solution(k, score):
#     answer = []
#     honorList = []

#     for ele in score:
#         heappush(honorList, ele)
#         if len(honorList) > k:
#             heappop(honorList)
#             answer.append(honorList[0])
#         else:
#             answer.append(honorList[0])


#     return answer

# print(solution(3, [10, 100, 20, 150, 1, 100, 200])) # 답: [10, 10, 10, 20, 20, 100, 100]
# print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000])) # 답: [0, 0, 0, 0, 20, 40, 70, 70, 150, 300]

import heapq  # 우선순위 큐 구현을 위함

def combinations(arr, selectNumber):
    result = []
    
    if selectNumber == 1:
        return [[ele] for ele in arr]
    
    for i, ele in enumerate(arr):
        restArr = arr[i+1:]
        comSubList = combinations(restArr, selectNumber-1)
        combineEle = [[ele] + comSub for comSub in comSubList]
        result.extend(combineEle)
    
    return result








graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

# def dijkstra(graph, start):
#   distances = {node: float('inf') for node in graph}  # start로 부터의 거리 값을 저장하기 위함
#   distances[start] = 0  # 시작 값은 0이어야 함
#   queue = []
#   heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

#   while queue:  # queue에 남아 있는 노드가 없으면 끝
#     current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.

#     if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
#       continue
    
#     for new_destination, new_distance in graph[current_destination].items():
#       distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
#       if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
#         distances[new_destination] = distance
#         heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
    
#   return distances

# def dijkstra(graph, startNode):
#     distances = {node: float('inf') for node in graph}
#     distances[startNode] = 0
#     dq = []
#     heapq.heappush(dq, [startNode, distances[startNode]])

#     while dq:
#         currentNode, currentDistance = heapq.heappop(dq)

#         if distances[currentNode] < currentDistance:
#             continue
        
#         for node, distance in graph[currentNode].items():
#             nextDistance = currentDistance + distance
            
#             if nextDistance < distances[node]:
#                 distances[node] = nextDistance
#                 heapq.heappush(dq, [node, nextDistance])
    
#     return distances

def dijkstra(graph, startNode):
    distanceList = {node: float('inf') for node in graph.keys()}
    distanceList[startNode] = 0
    queue = []
    heapq.heappush(queue, [0, startNode])

    while queue:
        currentDistance, currentNode = heapq.heappop(queue)

        if distanceList[currentNode] < currentDistance:
            continue
        
        for nextNode, nextDistance in graph[currentNode].items():
            distance = currentDistance + nextDistance

            if distance < distanceList[nextNode]:
                distanceList[nextNode] = distance
                heapq.heappush(queue, [distance, nextNode])
    
    return distanceList

def solution(people, limit):
    answer = 0
    a = [1, 2, 3, 4]
    print(combinations(a, 3))
    print(dijkstra(graph, 'A'))
    
    
    return answer

solution(1, 1)