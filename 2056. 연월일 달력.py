T = int(input())

for test_case in range(1, T + 1):
    a = list(input())
    # 월이 12가 넘어가는 경우
    if int(a[4] + a[5]) > 12:
        print("#{0} {1}".format(test_case, -1))
    # 월이 00인 경우
    elif a[4] == '0' and a[5] == '0':
        print("#{0} {1}".format(test_case, -1))
    # 2월인데 28일 넘어가는 경우
    elif a[5] == '2' and int(a[6] + a[7]) > 28:
        print("#{0} {1}".format(test_case, -1))
    # 일이 31이 넘어가는 경우
    elif int(a[6] + a[7]) > 31:
        print("#{0} {1}".format(test_case, -1))
    # 일이 00인 경우
    elif a[6] == '0' and a[5] == '0':
        print("#{0} {1}".format(test_case, -1))
    # 4월이 31일인 경우
    elif a[5] == '4' and int(a[6] + a[7]) > 30:
        print("#{0} {1}".format(test_case, -1))
    # 6월이 31일인 경우
    elif a[5] == '6' and int(a[6] + a[7]) > 30:
        print("#{0} {1}".format(test_case, -1))
    # 9월이 31일 경우:
    elif a[5] == '9' and int(a[6] + a[7]) > 30:
        print("#{0} {1}".format(test_case, -1))
    # 11월이 31일 경우:
    elif a[5] == '11' and int(a[6] + a[7]) > 30:
        print("#{0} {1}".format(test_case, -1))

    # 조건 만족하면 년/월/일 출력
    else:
        print("#{0} {1}/{2}/{3}".format(test_case, str(a[0])+str(a[1])+str(a[2])+str(a[3]), str(a[4]) + str(a[5]),
                                        str(a[6]) + str(a[7])))

