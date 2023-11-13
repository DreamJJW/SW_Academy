t = int(input())
for test_case in range(t):
    answer = 0
    n, k = map(int, input().split())
    score = list(map(int, input().split()))
    score.sort(reverse=True)
    for i in range(k):
        answer += score[i]
    print(f'#{test_case+1} {answer}')
