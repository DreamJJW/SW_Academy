t = int(input())
prime_number = []
n = 1000001
prime = [False] + [False] + [True] * (n - 1)
for i in range(2, n + 1):
    if prime[i]:
        for j in range(i + i, n + 1, i):
            prime[j] = False

for test_case in range(t):
    d, a, b = map(int, input().split())
    cnt = 0
    for i in range(a, b+1):
        if str(d) in str(i) and prime[i]:
            cnt += 1

    print(f'#{test_case+1} {cnt}')
