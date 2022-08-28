# from typing import List
#
#
# def solution(routes: List[List[int]]) -> int:
#     sorted_routes = sorted(routes, key=lambda x: (x[0], x[-1]))
#     print(f'sorted_routes: {sorted_routes}')
#
#     count = 1
#     previous_route = sorted_routes[0]
#     for route in sorted_routes[1:]:
#         print(f'start_point: {previous_route}, count: {count}')
#         if previous_route[-1] >= route[0]:
#             if previous_route[-1] >= route[-1]:
#                 previous_route = route
#         else:
#             count += 1
#             previous_route = route
#
#     return count


from typing import List


def solution(routes: List[List[int]]) -> int:
    sorted_routes = sorted(routes, key=lambda x: x[-1])
    print(f'sorted_routes: {sorted_routes}')

    count = 1
    previous_route = sorted_routes[0]
    for route in sorted_routes[1:]:
        if previous_route[-1] < route[0]:
            previous_route = route
            count += 1

    return count


if __name__ == "__main__":
    routes = [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]
    # routes = [[-10, 10], [-9, -3], [-8, -2], [-7, -1]]
    print(solution(routes))