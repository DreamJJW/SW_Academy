t = int(input())
for test_case in range(t):
    n, d = map(int, input().split())
    answer = 0
    garden = [0] * n
    cnt = 0
    for i in range(n-1, -1, -1):
        cnt += 1
        if cnt == d+1:
            garden[i] = 1
            cnt = 0 - d

    answer = garden.count(1)
    if garden[:d+1].count(1) == 0:
        answer += 1

    print(f'#{test_case+1} {answer}')