from itertools import combinations
t = int(input())
for test_case in range(t):
    nums = list(map(int, input().split()))
    temp = list(combinations(nums, 3))
    for i in range(len(temp)):
        temp[i] = sum(temp[i])

    temp = list(set(temp))
    temp.sort(reverse=True)
    print(f'#{test_case+1} {temp[4]}')