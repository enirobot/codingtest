from collections import deque

check = 0
number = deque([i+1 for i in range(int(input()))])

while len(number) > 1:
    num = number.popleft()

    if check:
        number.append(num)
        check -= 1
    else:
        check += 1

print(number[0])