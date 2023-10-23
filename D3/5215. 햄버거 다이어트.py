t = int(input())
for test_case in range(t):
    temp = []
    n, limit_cal = map(int, input().split())
    for _ in range(n):
        score, cals = map(int, input().split())
        temp.append((score, cals))

    # dp 테이블 선언
    dp = [[0] * ((limit_cal // 100) + 1) for _ in range(n+1)]
    for i in range(n):
        for j in range(1, (limit_cal // 100) + 1):
            score = temp[i][0]
            cal = temp[i][1]
            if j * 100 < cal:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i][j-(cal // 100)] + score)

    print(f"#{test_case+1} {dp[-1][-1]}")

                


