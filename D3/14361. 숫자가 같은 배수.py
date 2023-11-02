t = int(input())
for test_case in range(t):
    n = int(input())
    a = list(map(int, str(n)))  # [1,0,3,5]
    answer = ''

    if n < 10:
        answer = 'impossible'
    else:
        for i in range(2, 10):
            temp = n * i
            b = list(map(int, str(temp)))
            if sorted(a) == sorted(b):
                answer = 'possible'
                break
            else:
                answer = 'impossible'

    print(f'#{test_case+1} {answer}')
