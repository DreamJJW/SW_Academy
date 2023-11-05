t = int(input())
for test_case in range(t):
    n, a, b = map(int, input().split())
    if n - (a+b) < 0:
        min_num = a + b - n
    else:
        min_num = 0

    if a > b:
        max_num = b
    else:
        max_num = a

    print(f'#{test_case+1} {max_num} {min_num}')