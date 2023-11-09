t = int(input())
for test_case in range(t):
    s = input()
    print('..', end='')
    for _ in range(len(s)-1):
        print('#...', end='')
    print('#..')

    print('.', end='')
    for _ in range(len(s)*2-1):
        print('#.', end='')
    print('#.')

    print('#', end='')
    for i in range(len(s)):
        print('.' + s[i] + '.#', end='')
    print()

    print('.', end='')
    for _ in range(len(s) * 2 - 1):
        print('#.', end='')
    print('#.')

    print('..', end='')
    for _ in range(len(s) - 1):
        print('#...', end='')
    print('#..')




