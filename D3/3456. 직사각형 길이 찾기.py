t = int(input())
for test_case in range(t):
    answer = 0
    a, b, c = map(int, input().split())
    if a == b == c:
        answer = a
    elif a == b and a != c:
        answer = c
    elif a == c and a != b:
        answer = b
    elif b == c and b != a:
        answer = a

    print(f'#{test_case+1} {answer}')