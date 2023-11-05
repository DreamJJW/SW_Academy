t = int(input())
for test_case in range(t):
    n = int(input())
    earn = list(map(int, input().split()))
    avg_earn = sum(earn) // n
    answer = 0

    for i in earn:
        if i <= avg_earn:
            answer += 1

    print(f'{test_case+1} {answer}')