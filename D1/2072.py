T = int(input())

for test_case in range(1, T + 1):
    answer = 0
    x = list(map(int, input().split()))

    for nums in x:
        if nums % 2 != 0:
            answer += nums
    print("#{0} {1}" .format(test_case,  answer))



