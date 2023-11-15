t = int(input())
for test_case in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if a[i] > a[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(dp)
    print(f'#{test_case+1} {max(dp)}')