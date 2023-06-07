T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    hour = 0
    minute = 0
    hour1, minute1, hour2, minute2 = map(int, input().split())

    if minute1 + minute2 > 60:
        minute = minute1 + minute2 - 60
        hour += 1
    else:
        minute = minute1 + minute2

    if hour1 + hour2 > 12:
        hour = hour + hour1 + hour2 - 12
    else:
        hour = hour + hour1 + hour2

    print("#{0} {1} {2}".format(test_case, hour, minute))
