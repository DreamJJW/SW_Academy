t = int(input())
for test_case in range(t):
    a, b = map(int, input().split())
    if a + b == 24:
        answer = 0
    elif a + b > 24:
        answer = a + b - 24
    else:
        answer = a + b

    print(f'#{test_case+1} {answer}')