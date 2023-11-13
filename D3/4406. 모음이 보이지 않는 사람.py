t = int(input())
vowel = ['a', 'e', 'o', 'u', 'i']
for test_case in range(t):
    s = input()
    answer = ''
    for i in s:
        if i not in vowel:
            answer += i

    print(f'f#{test_case+1} {answer}')
