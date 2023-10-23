t = int(input())
for test_case in range(t):
    s = input()
    stack = []
    ball_cnt = 0
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                if stack[-1] == '(' or stack[-1] == '|':
                    ball_cnt += 1
                    stack.pop()
        elif i == '|':
            if stack:
                if stack[-1] == '(':
                    ball_cnt += 1
                    stack.pop()
            else:
                stack.append(i)

    print(f'#{test_case+1} {ball_cnt}')
