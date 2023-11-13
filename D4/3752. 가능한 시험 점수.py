t = int(input())
for test_case in range(t):
    n = int(input())
    score = list(map(int, input().split()))
    dp = [True] + [False] * sum(score)

    for i in score:
        dp[i] = True
        for j in range(len(dp) - i, -1, -1):
            if dp[i]:
                dp[i + j] = True

    answer = dp.count(True)
    print(dp)
    print(answer)