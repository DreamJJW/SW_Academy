t = int(input())
for test_case in range(t):
    answer = 0
    l, u, x = map(int, input().split())
    if u < x:
        answer = -1
    elif l > x:
        answer = l - x

    print(f'#{test_case+1} {answer}')
