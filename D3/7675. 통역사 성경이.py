t = int(input())
for test_case in range(t):
    n = int(input())
    answer = []
    a = 0
    while a < n:
        s = input()
        s = s.replace('.', '.').replace('?', '.').replace('!', '.')
        s = s.split('.')
        s = s[:-1]
        for i in s:
            cnt = 0
            for j in i.split(' '):
                if j == j.capitalize() and j.isalpha():
                    cnt += 1

            answer.append(cnt)
            a += 1

    print(f'#{test_case+1}', *answer)