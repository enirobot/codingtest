def solution(board, moves):
    stack = []
    x_list = []
    count = 0

    for y in range(len(board)):
        for x in range(len(board)):
            if board[x][y] != 0:
                x_list.append(x)
                break
        if len(x_list) != y + 1:
            x_list.append(None)

    for move in moves:
        y = move - 1
        x = x_list[y]

        if x is None:
            continue

        doll = board[x][y]
        x_list[y] = x + 1 if x != len(board) - 1 else None

        if not stack or stack[-1] != doll:
            stack.append(doll)
            continue

        stack.pop()
        count += 2

    return count


if __name__ == "__main__":
    # board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
    # moves = [1, 5, 3, 5, 1, 2, 1, 4]
    board = [[0, 0, 0, 0, 0],
             [0, 0, 1, 0, 3],
             [0, 2, 5, 0, 1],
             [4, 2, 4, 4, 2],
             [3, 5, 1, 3, 1]]
    moves = [1, 5, 3, 5, 1, 2, 5, 1, 4, 3]
    # board = [[0, 0, 1, 0, 0],
    #          [0, 0, 1, 0, 0],
    #          [0, 2, 1, 0, 0],
    #          [0, 2, 1, 0, 0],
    #          [0, 2, 1, 0, 0]]
    # moves = [1, 2, 3, 3, 2, 3, 1]

    print(solution(board, moves))
