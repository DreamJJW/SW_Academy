t = int(input())
for test_case in range(t):
    s = input()
    cards = []
    answer = ''
    temp = [13, 13, 13, 13]
    for i in range(0, len(s), 3):
        cards.append(s[i:i+3])

    if len(list(set(cards))) != len(cards):
        answer = 'ERROR'
    else:
        for i in cards:
            if i[0] == 'S':
                temp[0] -= 1
            elif i[0] == 'D':
                temp[1] -= 1
            elif i[0] == 'H':
                temp[2] -= 1
            else:
                temp[3] -= 1

    if answer == 'ERROR':
        print(f'#{test_case+1} {answer}')
    else:
        print(f'#{test_case+1}', *temp)
