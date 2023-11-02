t = int(input())
for test_case in range(t):
    D, L, N = map(int, input().split())
    damage = 0
    for i in range(N):
        attack = D * (1 + i * (L * 0.01))
        damage += attack

    print(f'#{test_case+1} {int(damage)}')

