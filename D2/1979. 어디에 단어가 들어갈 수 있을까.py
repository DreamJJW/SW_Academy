t = int(input())
for test_case in range(t):
    paper = []
    n, k = map(int, input().split())
    for _ in range(n):
        paper.append(list(map(int, input().split())))

    # 빈 칸 = 1, 빈 칸이 아닌 칸 = 0
    answer = 0
    cnt = 0
    # 가로 판별
    for i in range(n):
        if cnt == k:
            answer += 1
        cnt = 0
        for j in range(n):
            if paper[i][j] == 1:
                cnt += 1
            else:
                if cnt == k:
                    answer += 1
                cnt = 0

    # 세로 판별
    for i in range(n):
        if cnt == k:
            answer += 1
        cnt = 0
        for j in range(n):
            if paper[j][i] == 1:
                cnt += 1
                print(cnt, end=' ')
            else:
                if cnt == k:
                    answer += 1
                cnt = 0

    print(f'#{test_case + 1} {answer}')
