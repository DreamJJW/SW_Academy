t = int(input())
for test_case in range(t):
    time = list(map(int, input().split()))
    answer = min(time[1], time[3]) - max(time[0], time[2])
    if answer > 0:
        answer = 0
    print(f'#{test_case+1} {answer}')