t = int(input())
for test_case in range(t):
    p = input()
    q = input()
    p_cnt = 0
    q_cnt = 0
    for i in p:
        p_cnt += ord(i) - 96
    for j in q:
        q_cnt += ord(j) - 96

    if p == q:
        answer = 'N'
    else:
        if q_cnt - p_cnt == 1:
            answer = 'N'
        else:
            answer = 'Y'

    print(f'#{test_case + 1} {answer}')
