t = int(input())
for test_case in range(t):
    a, b = map(int, input().split())
    answer = 0
    if a == b:
        answer = 1
    elif b == 1:
        answer = a ** 2
    else:
        answer = (a // b) ** 2

    print(f'#{test_case+1} {answer}')