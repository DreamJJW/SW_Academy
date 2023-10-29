import heapq
t = int(input())
for test_case in range(t):
    n = int(input())
    sales = list(map(int, input().split()))

    profit = 0
    q = []
    for i in sales:
        heapq.heappush(q, (-i, i))

    cnt = 0; buy = 0
    for i in range(n):
        if sales[i] < q[0][1]:
            buy -= sales[i]
            cnt += 1
            q.remove((-sales[i], sales[i]))

        elif sales[i] == q[0][1]:
            profit += (cnt * q[0][1]) + buy
            cnt = 0; buy = 0
            heapq.heappop(q)
        print(q)

    print(f'#{test_case+1} {profit}')