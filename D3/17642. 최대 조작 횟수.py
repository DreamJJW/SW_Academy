t = int(input())
for test_case in range(t):
    a, b = map(int, input().split())
    answer = 0
    diff = b - a
    if a == b:
        answer = 0
    elif diff <= 1:
        answer = -1
    else:
        if diff % 2 == 0:
            answer = diff // 2
        else:
            answer = (diff - 3) // 2
            answer += 1


    print(f'#{test_case+1} {answer}')
