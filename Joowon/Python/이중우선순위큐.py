from heapq import heappush, heappop, heapify

def solution(operations):
    answer = []
    maxHeap = []
    minHeap = []

    for ele in operations:
        command, number = ele.split()
        number = int(number)
        if command == 'I':
            heappush(maxHeap, (-1 * number, number))
            heappush(minHeap, number)
        elif command == 'D' and number < 0 and minHeap:
            minNumber = heappop(minHeap)
            maxHeap.remove((-1 * minNumber, minNumber))
            heapify(maxHeap)
        elif command == 'D' and number > 0 and maxHeap:
            maxNumber = heappop(maxHeap)[1]
            minHeap.remove(maxNumber)
            heapify(minHeap)
    
    if maxHeap:
        answer.append(heappop(maxHeap)[1])
    else:
        answer.append(0)
    if minHeap:
        answer.append(heappop(minHeap))
    else:
        answer.append(0)

    return answer

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])) # 답: [0, 0]
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])) # 답: [333, -45]