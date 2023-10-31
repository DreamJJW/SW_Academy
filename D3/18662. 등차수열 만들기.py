t = int(input())
for test_case in range(t):
    a,b,c = map(int,input().split())
    dif_left = b - a
    dif_right = c - b
    if dif_left == dif_right:
        print(f'#{test_case} {0.0}')
    else:
        print(f"#{test_case} {abs((dif_right) - (dif_left)) / 2}")













