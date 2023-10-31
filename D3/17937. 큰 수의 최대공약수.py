import math
t = int(input())
for test_case in range(t):
    a, b = map(int, input().split())

    answer = 0
    if a == b:
        answer = a
    else:
        answer = 1

    print(f'#{test_case+1} {answer}')