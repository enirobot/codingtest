from collections import deque

def solution(maps):
    answer = -1
    dq = deque()
    xLen = len(maps[0])
    yLen = len(maps)
    direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    dq.append([0, 0])
    
    while dq:
        y, x = dq.popleft()
        
        for ele in direction:
            nextY = y+ele[0]
            nextX = x+ele[1]
            if -1<nextY<yLen and -1<nextX<xLen and maps[nextY][nextX] == 1:
                dq.append([nextY, nextX])
                maps[nextY][nextX] = maps[y][x] + 1
        
    answer = -1 if not maps[yLen-1][xLen-1] > 1 else maps[yLen-1][xLen-1]
    return answer