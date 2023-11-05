t = int(input())
for test_case in range(t):
    s = input()
    if int(s[:2]) > 12 >= int(s[2:4]):
        answer = 'YYMM'
    elif int(s[2:4]) > 12 >= int(s[:2]):
        answer = 'MMYY'
    elif int(s[:2]) > 12 and int(s[2:4]) > 12:
        answer = 'NA'
    else:
        answer = 'AMBIGUOUS'

    print(f'#{test_case+1} {answer}')

