t = int(input())
for test_case in range(t):
    n = int(input())
    answer = 0
    dp = []
    a = ''
    while True:
        a += "".join(map(str, input().split()))
        if len(a) == n:
            break

    start = 0
    while True:
        if str(start) not in a:
            answer = start
            break
        start += 1

    print(f'#{test_case+1} {answer}')

