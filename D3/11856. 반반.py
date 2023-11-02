t = int(input())
for test_case in range(t):
    s = input()
    temp = list(set(s))
    answer = 'Yes'

    for i in temp:
        if s.count(i) != 2:
            answer = 'No'

    if len(temp) != 2:
        answer = 'No'

    print(f'#{test_case+1} {answer}')