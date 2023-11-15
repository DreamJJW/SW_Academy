t = int(input())
for test_case in range(t):
    a, b, c, d = list(map(int, input().split()))
    answer = []
    if b / a > d / c:
        answer.append('BOB')
    elif b / a < d / c:
        answer.append('ALICE')
    else:
        answer.append('DRAW')

    for i in answer:
        print(f'#{test_case+1}', i)
