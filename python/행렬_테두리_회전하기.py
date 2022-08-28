from typing import *


def solution(rows: int, columns: int, queries: List[List[int]]) -> List[int]:
    matrix = [[y * columns + x + 1 for x in range(columns)] for y in range(rows)]
    answer = []

    for query in queries:
        x1, y1, x2, y2 = map(lambda n: n - 1, query)

        first_value = matrix[x1][y1]
        min_value = first_value

        for x in range(x1, x2):
            if (n := matrix[x][y1]) < min_value:
                min_value = n
            matrix[x][y1] = matrix[x + 1][y1]
        for y in range(y1, y2):
            if (n := matrix[x2][y]) < min_value:
                min_value = n
            matrix[x2][y] = matrix[x2][y + 1]
        for x in range(x2, x1, -1):
            if (n := matrix[x][y2]) < min_value:
                min_value = n
            matrix[x][y2] = matrix[x - 1][y2]
        for y in range(y2, y1, -1):
            if (n := matrix[x1][y]) < min_value:
                min_value = n
            matrix[x1][y] = matrix[x1][y - 1]

        matrix[x1][y1 + 1] = first_value
        answer.append(min_value)

    return answer


if __name__ == "__main__":
    rows = 100
    columns = 97
    queries = [[1, 1, 100, 97]]
    # rows = 3
    # columns = 3
    # queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
    # rows = 6
    # columns = 6
    # queries = [[2, 2, 5, 4],
    #            [3, 3, 6, 6],
    #            [5, 1, 6, 3]]
    print(solution(rows, columns, queries))
