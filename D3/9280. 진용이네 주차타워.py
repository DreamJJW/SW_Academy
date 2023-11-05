from collections import deque
t = int(input())
for test_case in range(t):
    n, m = map(int, input().split())  # n = 주차공간 개수, m  = 차의 개수
    place = []
    cars = []
    order = []
    wait = []
    money = 0
    queue = deque()

    for i in range(n):
        place.append(int(input()))
    for i in range(m):
        cars.append(int(input()))
    for i in range(m*2):
        order.append(int(input()))

    for i in order:
        if i > 0:
            queue.append(cars[i-1])
            money += cars[i-1] * place[queue.index(cars[i-1])]
        else:
            queue.popleft()


