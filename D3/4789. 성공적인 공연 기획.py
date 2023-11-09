t = int(input())

for tc in range(1, t + 1) :
    data = list(str(input()))
    clap = 0
    result = 0

    for i in range(len(data)):
        if data[i] != 0:
            if clap >= i:
                clap += int(data[i])
            else:
                result += i - clap
                clap = i + int(data[i])

    print('#%d %d' % (tc, result))