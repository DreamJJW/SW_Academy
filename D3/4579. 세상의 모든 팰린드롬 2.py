t = int(input())
for test_case in range(t):
    s = input()
    new_s = ''
    if s[0] == '*' or s[-1] == '*':
        answer = 'Exist'
    else:
        for i in s:
            if i != '*':
                new_s += i
        if new_s != new_s[::-1]:
            answer = 'Not exist'
        else:
            answer = 'Exist'

    print(f'#{test_case+1} {answer}')
