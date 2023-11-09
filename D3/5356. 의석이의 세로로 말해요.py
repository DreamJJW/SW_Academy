t = int(input())
for test_case in range(t):
    temp = []
    max_length = 0
    for _ in range(5):
        s = input()
        if len(s) > max_length:
            max_length = len(s)
        temp.append(s)

    for i in range(5):
        if len(temp[i]) < max_length:
            temp[i] = temp[i].ljust(max_length, '!')

    new_s = ''
    for i in range(max_length):
        for j in range(5):
            if temp[j][i] != '!':
                new_s += temp[j][i]

    print(f'#{test_case+1} {new_s}')
