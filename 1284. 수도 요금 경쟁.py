T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    bill_B = 0
    bill_A = 0
    P, Q, R, S, W = map(int, input().split())
    if W <= R:
        bill_B = Q
    else:
        bill_B = Q + (W - R) * S

    bill_A = P * W

    if bill_B > bill_A:
        print("#{0} {1}".format(test_case, bill_A))
    else:
        print("#{0} {1}".format(test_case, bill_B))
