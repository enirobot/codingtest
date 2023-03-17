N = int(input())
hList = []
answer = [1 for i in range(N)]

for i in range(N):
    ele = list(map(int, input().split()))
    hList.append((ele[0], ele[1]))

for i in range(N-1):
    for j in range(i+1, N):
        if hList[i][0] < hList[j][0] and hList[i][1] < hList[j][1]:
            answer[i] += 1
        elif hList[i][0] > hList[j][0] and hList[i][1] > hList[j][1]:
            answer[j] += 1

for i in range(N):
    print(answer[i], end=' ')