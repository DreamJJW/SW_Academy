t = int(input())
answer = [0 * i for i in range(t)]
for test_case in range(t):
    a, b = map(int, input().split())
    answer[test_case] = a + b

for i in range(t):
    print(f'#{i+1}', answer[i])


