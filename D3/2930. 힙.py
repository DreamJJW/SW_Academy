import heapq
t = int(input())
for test_case in range(t):
    q = []
    n = int(input())
    results = []
    for _ in range(n):
        order = list(map(int, input().split()))

        if order[0] == 1:
            heapq.heappush(q, (-order[1], order[1]))
        elif order[0] == 2:
            if q:
                a = heapq.heappop(q)
                results.append(a[1])
            else:
                results.append(-1)

    print(f'#{test_case+1}', *results)