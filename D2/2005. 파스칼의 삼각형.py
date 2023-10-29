t = int(input())
for test_case in range(t):
    n = int(input())

    data = [[1 for _ in range(i)] for i in range(1, n+1)]
    for i in range(2, n):
        for j in range(1, i):
            data[i][j] = data[i-1][j-1] + data[i-1][j]

    print(f'#{test_case+1}')
    for i in data:
        for j in i:
            print(j, end=' ')
        print()


