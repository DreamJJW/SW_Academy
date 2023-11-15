a = [True] * 1000001
a[0] = False
a[1] = False
primes = []
for i in range(2, 1000001):
    if a[i] == True:
        print(i, end=' ')
        for j in range(i+i, 1000001, i):
            a[j] = False


