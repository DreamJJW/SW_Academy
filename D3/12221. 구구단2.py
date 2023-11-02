t = int(input())
for test_case in range(t):
    a, b = map(int, input().split())
    if a > 9 or b > 9:
        answer = -1
    else:
        answer = a * b

    print(f'#{test_case+1} {answer}')