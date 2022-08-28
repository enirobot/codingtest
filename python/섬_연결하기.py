from typing import List

# Kruskal 알고리즘


def earrangement(costs: List[int]) -> int:
    if costs[0] > costs[1]:
        costs[0], costs[1] = costs[1], costs[0]

    return costs[-1]


def solution(n: int, costs: List[List[int]]) -> int:
    sorted_costs = sorted(costs, key=earrangement, reverse=True)
    union = [-i for i in range(n)]
    print(sorted_costs)
    print(union)

    edges = 0
    total_min_cost = 0
    while sorted_costs and edges < n - 1:
        a, b, cost = sorted_costs.pop()
        print(f'edges: {edges}, a: {a}, b: {b}, cost: {cost}')
        if union[a] != union[b]:
            parent = max(union[a], union[b])

            if parent < 0:
                parent = max(a, b)

            union[a], union[b] = parent, parent
            total_min_cost += cost
            edges += 1

    print(union)
    return total_min_cost


# def solution(n: int, costs: List[List[int]]) -> int:
#     sorted_costs = sorted(costs, key=lambda x: x[-1], reverse=True)
#     union = [-i for i in range(n)]
#     print(sorted_costs)
#     print(union)
#
#     edges = 0
#     total_min_cost = 0
#     while sorted_costs and edges < n - 1:
#         a, b, cost = sorted_costs.pop()
#         print(f'edges: {edges}, a: {a}, b: {b}, cost: {cost}')
#         if union[a] != union[b]:
#             parent = max(union[a], union[b])
#
#             if parent < 0:
#                 parent = max(a, b)
#
#             union[a], union[b] = parent, parent
#             total_min_cost += cost
#             edges += 1
#
#     print(union)
#     return total_min_cost


# def solution(n: int, costs: List[List[int]]) -> int:
#     sorted_costs = sorted(costs, key=lambda x: x[-1], reverse=True)
#     union = [-i for i in range(n)]
#     print(sorted_costs)
#     print(union)
#
#     edges = 0
#     total_min_cost = 0
#     while sorted_costs and edges < n - 1:
#         a, b, cost = sorted_costs.pop()
#         print(f'edges: {edges}, a: {a}, b: {b}, cost: {cost}')
#         if union[a] != union[b]:
#             parent = max(union[a], union[b])
#             child = min(union[a], union[b])
#
#             if parent < 0:
#                 parent = max(a, b)
#                 child = min(a, b)
#
#             for i in range(n):
#                 if union[i] == union[child]:
#                     union[i] = parent
#
#             # union[a], union[b] = parent, parent
#             total_min_cost += cost
#             edges += 1
#
#     print(union)
#     return total_min_cost


# def solution(n, costs):
#     answer = 0
#     costs.sort(key=lambda x: x[2])
#     visited = [True] + [False] * (n - 1)
#
#     while not all(visited):
#         print("while 순환")
#         for cur_node, next_node, cost in costs:
#             print(f'cur: {cur_node}, next: {next_node}, cost: {cost}, visited: {visited}')
#             if visited[cur_node] and visited[next_node]:
#                 continue
#             if visited[cur_node] or visited[next_node]:
#                 visited[cur_node] = visited[next_node] = True
#                 answer += cost
#                 break
#     return answer


if __name__ == "__main__":
    # n = 4
    # costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
    # n = 5
    # costs = [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]]
    # n = 5
    # costs = [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]]
    # n = 4
    # costs = [[0, 1, 5], [1, 2, 3], [2, 3, 3], [1, 3, 2], [0, 3, 4]]
    # n = 5
    # costs = [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]]
    # n = 5
    # costs = [[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]]
    # n = 6
    # costs = [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]
    # n = 5
    # costs = [[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]]
    # n = 5
    # costs = [[0, 1, 1], [0, 4, 5], [2, 4, 1], [2, 3, 1], [3, 4, 1]]
    # n = 5
    # costs = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 3, 1]]

    # n = 4
    # costs = [[0,1,1],[0,2,1],[1,2,1],[1,3,1],[2,3,8]]
    # n = 5
    # costs = [[1,2,3],[0,1,1],[0,4,5],[2,4,1],[2,3,1],[3,4,1]]
    # n = 5
    # costs = [[0,1,5],[1,2,3],[2,3,3],[3,1,2],[3,0,4],[2,4,6],[4,0,7]]
    # n = 5
    # costs = [[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]]
    # n = 4
    # costs = [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4]]
    # n = 4
    # costs = [[0,1,1],[0,2,2],[2,3,1]]
    # n = 7
    # costs = [[1,0,1],[3,2,1],[4,5,1],[3,5,9],[3,6,10],[1,6,1],[6,5,1]]
    # n = 6
    # costs = [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]
    # n = 6
    # costs = [[0,1,1],[3,1,1],[2,3,3],[2,4,4],[5,4,5]]
    # n = 5
    # costs = [[0,1,1],[3,4,1],[1,2,2],[2,3,4]]
    n = 4
    costs = [[0,1,1],[0,2,2],[2,3,1]]
    print(solution(n, costs))