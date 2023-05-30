T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    temp = []
    for i in range(N):
        a, b = input().split()
        for j in range(int(b)):
            temp.append(a)

    print("#{0}".format(test_case))
    cnt = 0
    for k in range(len(temp)):
        print(temp[k], end = '')
        cnt += 1
        if cnt == 10:
            print('')
            cnt = 0
    print('')
