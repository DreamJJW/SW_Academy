t = int(input())
for test_case in range(t):
    n, m = map(int, input().split())
    for i in range(1, m+1):
        if 2 * i + 1 * (m - i) == n:
            answer = [m - i, i]
            break

    print(f'#{test_case+1}', *answer)
