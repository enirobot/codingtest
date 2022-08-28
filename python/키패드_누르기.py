def solution(numbers, hand):
    keypad = [(3, 1), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    left, right = (3, 0), (3, 2)

    answer = ""
    for num in numbers:
        if num % 3 == 1:
            answer += 'L'
            left = keypad[num]
            continue
        if num % 3 == 0 and num != 0:
            answer += 'R'
            right = keypad[num]
            continue

        l_distance = abs(keypad[num][0] - left[0]) + abs(keypad[num][1] - left[1])
        r_distance = abs(keypad[num][0] - right[0]) + abs(keypad[num][1] - right[1])

        if l_distance < r_distance:
            left = keypad[num]
            answer += 'L'
        elif r_distance < l_distance:
            right = keypad[num]
            answer += 'R'
        else:
            if hand.startswith('l'):
                left = keypad[num]
                answer += 'L'
            else:
                right = keypad[num]
                answer += 'R'

    return answer


if __name__ == "__main__":
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand = "right"
    print(solution(numbers, hand))
