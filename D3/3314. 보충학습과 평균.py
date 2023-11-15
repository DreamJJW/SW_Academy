t = int(input())
for test_case in range(t):
    score = list(map(int, input().split()))
    answer = 0
    for i in score:
        if i < 40:
            answer += 40
        else:
            answer += i

    print(f'#{test_case+1} {answer // 5}')
