t = int(input())
for test_case in range(t):
    n = int(input())
    s1 = ((n+1) * n) // 2
    s3 = n * (n+1)
    s2 = n * n
    print(f'#{test_case+1} {s1} {s2} {s3}')