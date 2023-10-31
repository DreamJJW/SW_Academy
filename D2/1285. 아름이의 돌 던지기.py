import sys
t = int(input())
for test_case in range(t):
    n = int(input())
    stones = list(map(int, sys.stdin.readline().split()))

    stones = sorted(stones)
    plus = 0
    minus = 0
    for i in range(1, len(stones)+1):
        if stones[i] > 0:
            plus = stones[i]
            minus = stones[i-1]
            break

    dis = min(abs(plus), abs(minus))
    cnt = stones.count(dis) + stones.count(-dis)

    print(f'#{test_case+1} {dis} {cnt}')





