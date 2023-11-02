t = int(input())
for test_case in range(t):
    s = input()
    root_node = [1, 1]
    for i in s:
        if i == 'L':
            root_node[0] = root_node[0]
            root_node[1] = root_node[0] + root_node[1]
        else:
            root_node[0] = root_node[0] + root_node[1]
            root_node[1] = root_node[1]

    print(f'#{test_case+1} {root_node[0]} {root_node[1]}')