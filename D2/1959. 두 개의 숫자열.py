T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    shorter = min(N, M) # N과 M중에 짧은 쪽을 판별
    longer = max(N, M)
    temp = []

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for j in range(longer - shorter + 1):
        sum = 0
        for i in range(shorter):
            sum += (A[i] * B[i])
        temp.append(sum)
        if len(A) > len(B):
            A.pop(0)
        else:
            B.pop(0)

    print("#{0} {1}".format(test_case, max(temp)))
