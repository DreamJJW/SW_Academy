t = int(input())
for test_case in range(t):
    s = input()
    answer = ''
    for i in s:
        if i == 'p':
            answer += 'q'
        elif i == 'q':
            answer += 'p'
        elif i == 'b':
            answer += 'd'
        else:
            answer += 'b'

    print(f'#{test_case+1} {answer[::-1]}')