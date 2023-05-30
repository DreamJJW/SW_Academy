T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = []
    N = int(input())
    for i in range(N):
        lst = list(map(int, input().split()))
        arr.append(lst)

    turn90 = list(map(list, zip(*arr[::-1])))
    turn180 = list(map(list, zip(*turn90[::-1])))
    turn270 = list(map(list, zip(*turn180[::-1])))

    print("#{0}".format(test_case))
    for i in range(N):
        for j in range(N):
            print(turn90[i][j], end='')
        print('', end =' ')
        for k in range(N):
            print(turn180[i][k], end='')
        print('', end=' ')
        for l in range(N):
            print(turn270[i][l], end='')
        print('', end=' ')
        print('')