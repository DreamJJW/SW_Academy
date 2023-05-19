T = int(input())
from collections import Counter
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tc_num = int(input())
    a = list(map(int, input().split()))
    C = Counter(a)
    print("#{0} {1}".format(test_case, max(C, key=C.get)))





# 10 8 7 2 2 4 8 8 8 9 5 5 3
# Counter 함수에서 최대 빈도수 구하기
# max(C, key = C.get)