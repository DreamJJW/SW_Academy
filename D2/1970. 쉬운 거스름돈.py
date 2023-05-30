T = int(input())
money_arr = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    money_dic = {50000: 0, 10000: 0, 5000: 0, 1000: 0, 500: 0, 100: 0, 50: 0, 10: 0}
    N = int(input())

    if N % 10 != 0:   # input N의 일의 자리 수가 0이 아닐 때 일의 자리 수를 버림.
        N = N // 10 * 10

    while N != 0:
        for i in money_arr:
            if N // i != 0:
                money_dic[i] += N // i
                N -= i * (N // i)

    a = list(money_dic.values())
    print("#{0}".format(test_case))
    for i in a:
        print(i, end = ' ')
    print('')
