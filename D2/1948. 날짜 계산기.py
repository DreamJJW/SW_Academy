T = int(input())
days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    day_sum = 0
    month1, day1, month2, day2 = map(int, input().split())

    if month1 == month2:
        day_sum += day2 - day1 + 1
    else:
        day_sum += day2
        for i in range(month2 - 1, month1, -1):
            day_sum += days[i]
        day_sum += days[month1] - day1 + 1

    print("#{0} {1}".format(test_case, day_sum))



