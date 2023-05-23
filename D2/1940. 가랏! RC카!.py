T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    dis = 0
    speed = 0
    a = int(input())
    for i in range(a):
        command = list(map(int, input().split()))
        if command[0] == 1:
            speed += command[1]
            dis += speed
        elif command[0] == 2:
            if command[1] > speed:
                speed = 0
            else:
                speed -= command[1]
            dis += speed
        else:
            dis += speed

    print("#{0} {1}".format(test_case, dis))
