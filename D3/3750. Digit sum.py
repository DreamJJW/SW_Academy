t = int(input())
results = []
for test_case in range(t):
    n = int(input())
    s = str(n)
    a = 0
    b = 0
    c = 0
    answer = 0
    while True:
        for i in range(len(s)):
            a += int(s[i])
        if len(str(a)) == 1:
            answer = a
            results.append(answer)
            break
        a = str(a)
        for i in range(len(a)):
            b += int(a[i])
        if len(str(b)) == 1:
            answer = b
            results.append(answer)
            break
        b = str(b)
        for i in range(len(b)):
            c += int(b[i])
        if len(str(c)) == 1:
            answer = c
            results.append(answer)
            break

for tc in range(t):
    print(f'#{tc+1} {results[tc]}')
