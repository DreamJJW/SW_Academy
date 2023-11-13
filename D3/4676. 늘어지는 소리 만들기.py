t = int(input())
for test_case in range(t):
    s = input()
    h = int(input())
    new_s = list(s)
    index = list(map(int, input().split()))
    index.sort(reverse=True)
    for i in index:
        new_s.insert(i, '-')

    new_s = ''.join(new_s)
    print(f'#{test_case+1} {new_s}')