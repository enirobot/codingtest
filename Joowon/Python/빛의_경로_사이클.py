def solution(grid):
    answer = []
    lengthX = len(grid[0])
    lengthY = len(grid)
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    visited = [[[False] * 4 for i in range(lengthX)] for j in range(lengthY)]

    for i in range(lengthY):
        for j in range(lengthX):
            for d in range(4):
                if visited[i][j][d]:
                    continue
                
                cnt = 0
                nx = j
                ny = i
                nd = d
                while not visited[ny][nx][nd]:
                    visited[ny][nx][nd] = True
                    cnt += 1

                    nx = (nx + dx[nd]) % lengthX
                    ny = (ny + dy[nd]) % lengthY

                    if grid[ny][nx] == 'L':
                        nd = (nd - 1) % 4
                    elif grid[ny][nx] == 'R':
                        nd = (nd + 1) % 4
            
                answer.append(cnt)


    return sorted(answer)


print(solution(["SL","LR"])) # 답: [16]
print(solution(["S"])) # 답: [1,1,1,1]
print(solution(["R","R"])) # 답: [4,4]