from collections import defaultdict
t = int(input())
for test_case in range(t):
    n, m = map(int, input().split())
    # 그래프 (정점 기준)
    graph = defaultdict(set)
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].add(y)
        graph[y].add(x)

    total = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                if i in graph[j] and j in graph[k] and k in graph[i]:
                    total += 1

    print(graph)
