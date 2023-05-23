T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    temp = []
    N = int(input())
    cnt = 0
    num = 0
    for j in range(1, 100):
        num += N
        for i in list(str(num)):
            if i not in temp:
                temp.append(i)
        cnt += 1
        if nums == sorted(temp):
            print("#{0} {1}".format(test_case, cnt*N))
            break




