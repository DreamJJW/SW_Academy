t = int(input())
for test_case in range(t):
    day = [11, 11, 11]
    d, h, m = map(int, input().split())
    day[0] = d - day[0]
    day[1] = h - day[1]
    day[2] = m - day[2]
    if day[0] * 1440 + day[1] * 60 + day[2] < 0:
        answer = -1
    else:
        answer = day[0] * 1440 + day[1] * 60 + day[2]

    print(f'#{test_case+1} {answer}')