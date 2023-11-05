t = int(input())
for test_case in range(t):
    n = int(input())
    pay = 0
    for _ in range(n):
        p, x = map(float, input().split())
        pay += p * x

    print(f'#{test_case+1} {pay:.6f}')