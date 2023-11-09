t = int(input())
for test_case in range(t):
    cnt = 0
    a, b, c = map(int, input().split())
    breads = [a, b]
    breads.sort()
    while True:
        if c < breads[0]:
            break
        c -= breads[0]
        cnt += 1
    print(f'#{test_case+1} {cnt}')
